"""
Evaluation utilities for rating prediction.
Includes functions for calculating accuracy, JSON validity, and consistency.
"""

import json
import re
from typing import Dict, List, Tuple


def parse_json_response(response_text: str) -> Dict:
    """
    Attempts to parse JSON from the LLM response.
    Handles cases where response might have extra text around JSON.
    """
    try:
        # Try direct JSON parsing first
        return json.loads(response_text)
    except json.JSONDecodeError:
        # Try to extract JSON from text
        json_match = re.search(r'\{[^{}]*\}', response_text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass
    
    return None


def is_valid_json(response_text: str) -> bool:
    """
    Checks if the response contains valid JSON.
    """
    parsed = parse_json_response(response_text)
    return parsed is not None


def has_required_fields(parsed_json: Dict) -> bool:
    """
    Checks if the parsed JSON has the required fields.
    """
    if not parsed_json:
        return False
    return "predicted_stars" in parsed_json and "explanation" in parsed_json


def get_predicted_rating(parsed_json: Dict) -> int:
    """
    Extracts the predicted rating from parsed JSON.
    Returns None if not found or invalid.
    """
    if not parsed_json:
        return None
    
    rating = parsed_json.get("predicted_stars")
    if rating is None:
        return None
    
    try:
        rating = int(rating)
        if 1 <= rating <= 5:
            return rating
    except (ValueError, TypeError):
        pass
    
    return None


def calculate_accuracy(predictions: List[int], actuals: List[int]) -> float:
    """
    Calculates accuracy as the percentage of correct predictions.
    """
    if len(predictions) != len(actuals):
        raise ValueError("Predictions and actuals must have the same length")
    
    if len(predictions) == 0:
        return 0.0
    
    correct = sum(1 for p, a in zip(predictions, actuals) if p == a)
    return (correct / len(predictions)) * 100


def calculate_json_validity_rate(responses: List[str]) -> float:
    """
    Calculates the percentage of responses that contain valid JSON.
    """
    if len(responses) == 0:
        return 0.0
    
    valid_count = sum(1 for resp in responses if is_valid_json(resp))
    return (valid_count / len(responses)) * 100


def calculate_consistency(predictions_list: List[List[int]]) -> float:
    """
    Calculates consistency across multiple runs.
    For each item, checks if all runs produced the same prediction.
    Returns the percentage of items with consistent predictions.
    """
    if not predictions_list or len(predictions_list) == 0:
        return 0.0
    
    num_items = len(predictions_list[0])
    if num_items == 0:
        return 0.0
    
    consistent_count = 0
    for i in range(num_items):
        predictions_for_item = [pred_list[i] for pred_list in predictions_list if i < len(pred_list)]
        if len(set(predictions_for_item)) == 1:
            consistent_count += 1
    
    return (consistent_count / num_items) * 100


def evaluate_approach(responses: List[str], actual_ratings: List[int]) -> Dict:
    """
    Comprehensive evaluation of a prompting approach.
    Returns a dictionary with all metrics.
    """
    parsed_jsons = [parse_json_response(resp) for resp in responses]
    valid_jsons = [pj for pj in parsed_jsons if pj and has_required_fields(pj)]
    predictions = [get_predicted_rating(pj) for pj in parsed_jsons]
    
    # Filter out None predictions for accuracy calculation
    valid_predictions = []
    corresponding_actuals = []
    for pred, actual in zip(predictions, actual_ratings):
        if pred is not None:
            valid_predictions.append(pred)
            corresponding_actuals.append(actual)
    
    json_validity = calculate_json_validity_rate(responses)
    accuracy = calculate_accuracy(valid_predictions, corresponding_actuals) if valid_predictions else 0.0
    
    return {
        "total_responses": len(responses),
        "valid_json_count": len(valid_jsons),
        "json_validity_rate": json_validity,
        "valid_predictions_count": len(valid_predictions),
        "accuracy": accuracy,
        "predictions": predictions,
        "actual_ratings": actual_ratings
    }
