"""
Task 1: Rating Prediction via Prompting
This script implements three different prompting approaches for classifying Yelp reviews.

To convert to Jupyter notebook:
1. Install jupyter: pip install jupyter
2. Run: jupyter nbconvert --to notebook --execute rating_prediction.py
Or manually create cells in Jupyter and copy code sections.
"""

import pandas as pd
import google.generativeai as genai
import json
import os
from typing import List, Dict
import sys

# Add paths for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from prompts.prompt_versions import get_direct_classification_prompt, get_few_shot_prompt, get_chain_of_thought_prompt
from utils.evaluation import evaluate_approach, calculate_accuracy, calculate_json_validity_rate

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not found. Please set it in your environment.")
    print("You can get an API key from: https://makersuite.google.com/app/apikey")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def load_yelp_data(file_path: str, sample_size: int = 200) -> pd.DataFrame:
    """
    Loads and samples the Yelp reviews dataset.
    """
    print(f"Loading data from {file_path}...")
    try:
        df = pd.read_csv(file_path)
        if len(df) > sample_size:
            df = df.sample(n=sample_size, random_state=42).reset_index(drop=True)
        print(f"Loaded {len(df)} reviews")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        print("Please download the Yelp dataset from:")
        print("https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset")
        return pd.DataFrame()


def predict_rating(prompt: str) -> str:
    """
    Sends prompt to Gemini API and returns response.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling API: {e}")
        return ""


def run_evaluation(df: pd.DataFrame, approach_name: str, prompt_func) -> Dict:
    """
    Runs evaluation for a single prompting approach.
    """
    print(f"\nEvaluating {approach_name} approach...")
    responses = []
    actual_ratings = []
    
    for idx, row in df.iterrows():
        review_text = str(row.get('text', row.get('review', '')))
        actual_rating = int(row.get('stars', row.get('rating', 3)))
        
        if not review_text:
            continue
        
        prompt = prompt_func(review_text)
        response = predict_rating(prompt)
        
        responses.append(response)
        actual_ratings.append(actual_rating)
        
        if (idx + 1) % 20 == 0:
            print(f"Processed {idx + 1}/{len(df)} reviews...")
    
    results = evaluate_approach(responses, actual_ratings)
    results['approach_name'] = approach_name
    return results


def main():
    """
    Main function to run all three prompting approaches and compare results.
    """
    print("=" * 60)
    print("Task 1: Rating Prediction via Prompting")
    print("=" * 60)
    
    # Load data
    data_file = "data/yelp_reviews_sample.csv"
    df = load_yelp_data(data_file)
    
    if df.empty:
        print("\nCreating sample data structure for demonstration...")
        print("Please download the actual dataset and place it in data/yelp_reviews_sample.csv")
        return
    
    # Define approaches
    approaches = [
        ("Direct Classification", get_direct_classification_prompt),
        ("Few-Shot Learning", get_few_shot_prompt),
        ("Chain-of-Thought", get_chain_of_thought_prompt)
    ]
    
    # Run evaluations
    all_results = []
    for approach_name, prompt_func in approaches:
        results = run_evaluation(df, approach_name, prompt_func)
        all_results.append(results)
    
    # Print comparison table
    print("\n" + "=" * 60)
    print("COMPARISON TABLE")
    print("=" * 60)
    print(f"{'Approach':<25} {'Accuracy':<12} {'JSON Validity':<15} {'Valid Predictions':<20}")
    print("-" * 60)
    
    for result in all_results:
        print(f"{result['approach_name']:<25} "
              f"{result['accuracy']:.2f}%{'':<8} "
              f"{result['json_validity_rate']:.2f}%{'':<10} "
              f"{result['valid_predictions_count']:<20}")
    
    # Discussion
    print("\n" + "=" * 60)
    print("DISCUSSION")
    print("=" * 60)
    print("\nKey Findings:")
    print("1. Direct Classification: Simple and fast, but may lack context.")
    print("2. Few-Shot Learning: Provides examples to guide the model.")
    print("3. Chain-of-Thought: Encourages step-by-step reasoning.")
    print("\nTrade-offs:")
    print("- More complex prompts may improve accuracy but increase API costs.")
    print("- JSON validity is crucial for production use.")
    print("- Consistency across runs indicates reliability.")


if __name__ == "__main__":
    main()
