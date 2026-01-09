"""
API routes for review submissions.
Handles user review creation and retrieval.
"""

from flask import Blueprint, request, jsonify
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import Review
from schemas import ReviewSubmissionSchema, ReviewResponseSchema, ErrorResponseSchema
from services.gemini_service import GeminiService

reviews_bp = Blueprint('reviews', __name__)


def init_reviews_routes(app, db_session_factory):
    """
    Initializes review routes with database session factory.
    """
    gemini_service = GeminiService()
    
    @reviews_bp.route('/api/reviews', methods=['POST'])
    def submit_review():
        """
        Endpoint for submitting a new review.
        """
        try:
            data = request.get_json()
            
            if not data:
                error = ErrorResponseSchema("invalid_request", "Request body must be JSON")
                return jsonify(error.to_dict()), 400
            
            schema = ReviewSubmissionSchema(data)
            is_valid, error_message = schema.validate()
            
            if not is_valid:
                error = ErrorResponseSchema("validation_error", error_message)
                return jsonify(error.to_dict()), 400
            
            db = db_session_factory()
            
            try:
                user_rating = schema.user_rating
                user_review = schema.user_review
                
                ai_response, ai_summary, recommended_actions = gemini_service.generate_all(
                    user_rating, user_review
                )
                
                new_review = Review(
                    user_rating=user_rating,
                    user_review=user_review,
                    ai_response=ai_response,
                    ai_summary=ai_summary,
                    recommended_actions=recommended_actions,
                    created_at=datetime.utcnow()
                )
                
                db.add(new_review)
                db.commit()
                db.refresh(new_review)
                
                response_schema = ReviewResponseSchema(
                    review_id=new_review.id,
                    user_rating=new_review.user_rating,
                    user_review=new_review.user_review,
                    ai_response=new_review.ai_response,
                    created_at=new_review.created_at.isoformat()
                )
                
                return jsonify(response_schema.to_dict()), 201
                
            except Exception as e:
                db.rollback()
                error = ErrorResponseSchema("server_error", f"Failed to process review: {str(e)}")
                return jsonify(error.to_dict()), 500
            finally:
                db.close()
                
        except Exception as e:
            error = ErrorResponseSchema("server_error", f"Unexpected error: {str(e)}")
            return jsonify(error.to_dict()), 500
    
    app.register_blueprint(reviews_bp)
