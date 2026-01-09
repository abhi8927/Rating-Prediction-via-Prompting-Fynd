"""
API routes for admin dashboard.
Handles retrieval of all reviews and analytics.
"""

from flask import Blueprint, request, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import Review
from schemas import AdminReviewSchema, ErrorResponseSchema
from sqlalchemy import func

admin_bp = Blueprint('admin', __name__)


def init_admin_routes(app, db_session_factory):
    """
    Initializes admin routes with database session factory.
    """
    
    @admin_bp.route('/api/admin/reviews', methods=['GET'])
    def get_all_reviews():
        """
        Endpoint for retrieving all reviews for admin dashboard.
        """
        try:
            db = db_session_factory()
            
            try:
                reviews = db.query(Review).order_by(Review.created_at.desc()).all()
                
                reviews_data = []
                for review in reviews:
                    schema = AdminReviewSchema(
                        review_id=review.id,
                        user_rating=review.user_rating,
                        user_review=review.user_review,
                        ai_summary=review.ai_summary,
                        recommended_actions=review.recommended_actions,
                        created_at=review.created_at.isoformat() if review.created_at else ""
                    )
                    reviews_data.append(schema.to_dict())
                
                return jsonify({"reviews": reviews_data}), 200
                
            except Exception as e:
                error = ErrorResponseSchema("server_error", f"Failed to retrieve reviews: {str(e)}")
                return jsonify(error.to_dict()), 500
            finally:
                db.close()
                
        except Exception as e:
            error = ErrorResponseSchema("server_error", f"Unexpected error: {str(e)}")
            return jsonify(error.to_dict()), 500
    
    @admin_bp.route('/api/admin/stats', methods=['GET'])
    def get_stats():
        """
        Endpoint for retrieving analytics statistics.
        """
        try:
            db = db_session_factory()
            
            try:
                total_reviews = db.query(Review).count()
                
                rating_counts = db.query(
                    Review.user_rating,
                    func.count(Review.id).label('count')
                ).group_by(Review.user_rating).all()
                
                stats = {
                    "total_reviews": total_reviews,
                    "rating_distribution": {
                        str(rating): count for rating, count in rating_counts
                    }
                }
                
                return jsonify(stats), 200
                
            except Exception as e:
                error = ErrorResponseSchema("server_error", f"Failed to retrieve stats: {str(e)}")
                return jsonify(error.to_dict()), 500
            finally:
                db.close()
                
        except Exception as e:
            error = ErrorResponseSchema("server_error", f"Unexpected error: {str(e)}")
            return jsonify(error.to_dict()), 500
    
    app.register_blueprint(admin_bp)
