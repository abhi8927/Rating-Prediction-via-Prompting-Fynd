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
        Generates a professional and detailed user-facing response based on their review and rating.
        """
        prompt = f"""You are a professional customer service representative responding to a customer review. 

Customer Rating: {user_rating} out of 5 stars
Customer Review: {user_review}

Generate a professional, warm, and detailed response (4-6 sentences) that:
1. Acknowledges the specific feedback mentioned in their review
2. Shows genuine appreciation for taking the time to share their experience
3. Addresses any concerns or highlights positive aspects mentioned
4. Demonstrates that their feedback is valued and will be used for improvement
5. Maintains a professional yet personable tone appropriate for the rating given

For positive reviews (4-5 stars): Express gratitude, highlight what made their experience great, and invite them back.
For neutral reviews (3 stars): Thank them, acknowledge their balanced perspective, and show commitment to improvement.
For negative reviews (1-2 stars): Apologize sincerely, acknowledge specific issues, and outline steps being taken to address concerns.

Make the response feel personalized and thoughtful, not generic."""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Thank you for your {user_rating}-star review. We appreciate your detailed feedback and will use it to improve our service."
    
    def generate_summary(self, user_rating: int, user_review: str) -> str:
        """
        Generates a comprehensive and detailed summary of the review for admin dashboard.
        """
        prompt = f"""Analyze and summarize this customer review in detail for an admin dashboard.

Customer Rating: {user_rating} out of 5 stars
Customer Review: {user_review}

Provide a comprehensive summary (3-5 sentences) that includes:
1. Overall sentiment and key themes from the review
2. Specific positive aspects mentioned (if any)
3. Specific concerns or issues raised (if any)
4. Notable details about service, product quality, staff, or experience
5. The customer's overall impression and satisfaction level

Be thorough and capture all important details that would help management understand the customer's experience. Use professional language suitable for a business dashboard."""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"{user_rating}-star review: {user_review[:100]}..."
    
    def generate_recommended_actions(self, user_rating: int, user_review: str) -> str:
        """
        Generates detailed and actionable recommendations for the admin based on the review.
        """
        prompt = f"""You are a business consultant analyzing customer feedback. Based on this review, provide detailed, actionable recommendations.

Customer Rating: {user_rating} out of 5 stars
Customer Review: {user_review}

Generate comprehensive recommended actions (4-6 bullet points) that:
1. Address specific issues or concerns mentioned in the review
2. Build upon positive aspects to enhance strengths
3. Include both immediate actions and longer-term improvements
4. Are specific, measurable, and actionable
5. Consider the rating level and review content

For negative reviews (1-2 stars): Focus on damage control, customer recovery, and systemic improvements.
For neutral reviews (3 stars): Focus on identifying improvement opportunities and enhancing the experience.
For positive reviews (4-5 stars): Focus on maintaining excellence, leveraging positive feedback, and identifying what's working well.

Format as a clear bulleted list with detailed explanations for each action. Be professional and strategic."""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            if user_rating <= 2:
                return "• Immediately follow up with the customer to address their specific concerns and offer a resolution\n• Conduct a thorough review of the service quality issues mentioned and implement corrective measures\n• Review and enhance staff training programs to prevent similar issues\n• Consider offering appropriate compensation or a sincere apology to rebuild trust\n• Monitor for similar feedback patterns to identify systemic problems"
            elif user_rating == 3:
                return "• Analyze the feedback to identify specific areas mentioned that need improvement\n• Monitor for similar feedback patterns across other reviews to identify trends\n• Develop targeted improvement initiatives based on the concerns raised\n• Consider reaching out to the customer for additional feedback to better understand their experience\n• Review current processes and identify opportunities to exceed customer expectations"
            else:
                return "• Acknowledge and thank the customer publicly if appropriate and with their permission\n• Share this positive feedback with the team to recognize good performance and maintain standards\n• Consider using this review as testimonial material (with customer consent) for marketing purposes\n• Identify the specific factors that contributed to this positive experience and ensure they are consistently maintained\n• Use this feedback to reinforce best practices and training protocols"
    
    def generate_all(self, user_rating: int, user_review: str) -> tuple[str, str, str]:
        """
        Generates all three AI outputs at once.
        Returns (user_response, summary, recommended_actions)
        """
        user_response = self.generate_user_response(user_rating, user_review)
        summary = self.generate_summary(user_rating, user_review)
        recommended_actions = self.generate_recommended_actions(user_rating, user_review)
        
        return user_response, summary, recommended_actions
