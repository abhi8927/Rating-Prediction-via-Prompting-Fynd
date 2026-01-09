"""
JSON schemas for request and response validation.
Defines the structure for API payloads.
"""

from typing import Optional


class ReviewSubmissionSchema:
    """
    Schema for review submission requests.
    """
    def __init__(self, data: dict):
        self.user_rating = data.get("user_rating")
        self.user_review = data.get("user_review", "")
    
    def validate(self) -> tuple[bool, Optional[str]]:
        """
        Validates the submission data.
        Returns (is_valid, error_message).
        """
        if self.user_rating is None:
            return False, "user_rating is required"
        
        if not isinstance(self.user_rating, int):
            return False, "user_rating must be an integer"
        
        if self.user_rating < 1 or self.user_rating > 5:
            return False, "user_rating must be between 1 and 5"
        
        if not isinstance(self.user_review, str):
            return False, "user_review must be a string"
        
        if len(self.user_review.strip()) == 0:
            return False, "user_review cannot be empty"
        
        if len(self.user_review) > 5000:
            return False, "user_review is too long (maximum 5000 characters)"
        
        return True, None


class ReviewResponseSchema:
    """
    Schema for review submission responses.
    """
    def __init__(self, review_id: int, user_rating: int, user_review: str, 
                 ai_response: str, created_at: str):
        self.review_id = review_id
        self.user_rating = user_rating
        self.user_review = user_review
        self.ai_response = ai_response
        self.created_at = created_at
    
    def to_dict(self) -> dict:
        """
        Converts to dictionary for JSON serialization.
        """
        return {
            "review_id": self.review_id,
            "user_rating": self.user_rating,
            "user_review": self.user_review,
            "ai_response": self.ai_response,
            "created_at": self.created_at
        }


class AdminReviewSchema:
    """
    Schema for admin dashboard review data.
    """
    def __init__(self, review_id: int, user_rating: int, user_review: str,
                 ai_summary: str, recommended_actions: str, created_at: str):
        self.review_id = review_id
        self.user_rating = user_rating
        self.user_review = user_review
        self.ai_summary = ai_summary
        self.recommended_actions = recommended_actions
        self.created_at = created_at
    
    def to_dict(self) -> dict:
        """
        Converts to dictionary for JSON serialization.
        """
        return {
            "review_id": self.review_id,
            "user_rating": self.user_rating,
            "user_review": self.user_review,
            "ai_summary": self.ai_summary or "",
            "recommended_actions": self.recommended_actions or "",
            "created_at": self.created_at
        }


class ErrorResponseSchema:
    """
    Schema for error responses.
    """
    def __init__(self, error: str, message: str):
        self.error = error
        self.message = message
    
    def to_dict(self) -> dict:
        """
        Converts to dictionary for JSON serialization.
        """
        return {
            "error": self.error,
            "message": self.message
        }
