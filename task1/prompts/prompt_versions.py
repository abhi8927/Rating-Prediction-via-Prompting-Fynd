"""
Different prompting approaches for rating prediction.
Each function returns a prompt template for classifying Yelp reviews.
"""

def get_direct_classification_prompt(review_text):
    """
    Approach 1: Direct Classification
    Simple instruction-based prompt that directly asks for rating classification.
    """
    prompt = f"""Classify the following Yelp review into a star rating from 1 to 5.

Review: {review_text}

Respond with a JSON object containing:
- "predicted_stars": a number from 1 to 5
- "explanation": a brief explanation for your rating

JSON Response:"""
    return prompt


def get_few_shot_prompt(review_text):
    """
    Approach 2: Few-Shot Learning
    Includes examples in the prompt to guide the model.
    """
    prompt = f"""Classify Yelp reviews into star ratings (1-5). Here are some examples:

Example 1:
Review: "Terrible service, food was cold and staff was rude. Never coming back."
Rating: 1
Explanation: Multiple negative aspects including poor service, food quality, and staff behavior.

Example 2:
Review: "Amazing food and great atmosphere! The staff was friendly and helpful. Highly recommend!"
Rating: 5
Explanation: Consistently positive feedback across food, atmosphere, and service.

Example 3:
Review: "Food was okay but nothing special. Service was decent. Average experience overall."
Rating: 3
Explanation: Mixed neutral feedback indicating an average experience.

Now classify this review:
Review: {review_text}

Respond with JSON:
{{
  "predicted_stars": <number>,
  "explanation": "<your explanation>"
}}"""
    return prompt


def get_chain_of_thought_prompt(review_text):
    """
    Approach 3: Chain-of-Thought Reasoning
    Asks the model to think through the classification step by step.
    """
    prompt = f"""Analyze the following Yelp review and determine its star rating by thinking through each aspect.

Review: {review_text}

Step 1: Identify positive aspects mentioned in the review.
Step 2: Identify negative aspects mentioned in the review.
Step 3: Consider the overall sentiment (very negative, negative, neutral, positive, very positive).
Step 4: Map the sentiment to a star rating:
   - Very negative: 1 star
   - Negative: 2 stars
   - Neutral: 3 stars
   - Positive: 4 stars
   - Very positive: 5 stars
Step 5: Provide your final rating and reasoning.

Respond with a JSON object:
{{
  "predicted_stars": <your rating>,
  "explanation": "<your step-by-step reasoning>"
}}"""
    return prompt


def get_all_prompts(review_text):
    """
    Returns all three prompt versions for a given review.
    Useful for batch processing and comparison.
    """
    return {
        "direct": get_direct_classification_prompt(review_text),
        "few_shot": get_few_shot_prompt(review_text),
        "chain_of_thought": get_chain_of_thought_prompt(review_text)
    }
