"""
Service for interacting with Google Gemini API.
Handles all LLM operations including response generation, summarization, and action recommendations.
"""

import os
import google.generativeai as genai
from typing import Optional


class GeminiService:
    """
    Wrapper class for Gemini API operations.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initializes the Gemini service with API key.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY must be provided")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_user_response(self, user_rating: int, user_review: str) -> str:
        """
        Generates a user-facing response based on their review and rating.
        """
        prompt = f"""A user submitted a review with a {user_rating}-star rating.

Review: {user_review}

Generate a brief, friendly, and professional response (2-3 sentences) that:
- Acknowledges their feedback
- Shows appreciation for their input
- Is appropriate for the rating they gave

Keep it concise and natural."""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Thank you for your {user_rating}-star review. We appreciate your feedback and will use it to improve our service."
    
    def generate_summary(self, user_rating: int, user_review: str) -> str:
        """
        Generates a concise summary of the review for admin dashboard.
        """
        prompt = f"""Summarize this customer review in 1-2 sentences for an admin dashboard.

Rating: {user_rating} stars
Review: {user_review}

Provide a brief summary highlighting the main points."""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"{user_rating}-star review: {user_review[:100]}..."
    
    def generate_recommended_actions(self, user_rating: int, user_review: str) -> str:
        """
        Generates recommended actions for the admin based on the review.
        """
        prompt = f"""Based on this customer review, suggest 2-3 specific actions the business should take.

Rating: {user_rating} stars
Review: {user_review}

Provide actionable recommendations. Format as a bulleted list."""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            if user_rating <= 2:
                return "• Follow up with the customer to address concerns\n• Review service quality and staff training\n• Consider offering compensation or apology"
            elif user_rating == 3:
                return "• Monitor similar feedback patterns\n• Identify areas for improvement\n• Consider follow-up communication"
            else:
                return "• Thank the customer publicly if appropriate\n• Share positive feedback with staff\n• Use as testimonial material if permitted"
    
    def generate_all(self, user_rating: int, user_review: str) -> tuple[str, str, str]:
        """
        Generates all three AI outputs at once.
        Returns (user_response, summary, recommended_actions)
        """
        user_response = self.generate_user_response(user_rating, user_review)
        summary = self.generate_summary(user_rating, user_review)
        recommended_actions = self.generate_recommended_actions(user_rating, user_review)
        
        return user_response, summary, recommended_actions
