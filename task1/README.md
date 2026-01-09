# Task 1: Rating Prediction via Prompting

This task implements three different prompting approaches to classify Yelp reviews into star ratings (1-5) using Google Gemini API.

## Approaches Implemented

1. **Direct Classification**: Simple instruction-based prompt
2. **Few-Shot Learning**: Includes examples in the prompt
3. **Chain-of-Thought**: Step-by-step reasoning approach

## Setup

1. Install required packages:
```bash
pip install pandas google-generativeai jupyter
```

2. Set your Gemini API key:
```bash
export GEMINI_API_KEY=your_api_key_here
```

Or create a `.env` file in the task1 directory.

3. Download the Yelp dataset from Kaggle:
   - URL: https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset
   - Place the CSV file in `data/yelp_reviews_sample.csv`
   - The script will automatically sample 200 rows for evaluation

## Usage

### Option 1: Run as Python script
```bash
python rating_prediction.py
```

### Option 2: Use in Jupyter Notebook
1. Start Jupyter: `jupyter notebook`
2. Create a new notebook
3. Copy code sections from `rating_prediction.py` into cells
4. Run cells sequentially

## Evaluation Metrics

The script evaluates each approach on:
- **Accuracy**: Percentage of correctly predicted ratings
- **JSON Validity Rate**: Percentage of valid JSON responses
- **Consistency**: Reliability across multiple runs

## Output

The script generates:
- A comparison table showing metrics for all three approaches
- Discussion of results and trade-offs
- Detailed evaluation data

## Files

- `rating_prediction.py`: Main script
- `prompts/prompt_versions.py`: Prompt templates
- `utils/evaluation.py`: Evaluation functions
- `data/yelp_reviews_sample.csv`: Dataset (you need to download this)
