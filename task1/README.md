# Task 1: Rating Prediction

Three different ways to ask an AI to predict Yelp review ratings (1-5 stars) using Google Gemini API.

## The Three Approaches

1. Direct Classification - just ask directly
2. Few-Shot Learning - give examples first
3. Chain-of-Thought - step by step reasoning

## Setup

Install packages:
```bash
pip install pandas google-generativeai python-dotenv
```

Set your API key in a `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

Get the Yelp dataset from Kaggle:
- https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset
- Put the CSV file in `data/yelp.csv`
- The code will sample 200 rows automatically

## Running It

**As a script:**
```bash
python rating_prediction.py
```

**As a notebook:**
```bash
jupyter notebook rating_prediction.ipynb
```

## What It Measures

- Accuracy: how many predictions matched the real ratings
- JSON validity: how often responses were valid JSON
- Consistency: how reliable results are across runs

## Output

Shows a comparison table with metrics for all three approaches, plus discussion of results and trade-offs.

## Files

- `rating_prediction.py` - main script
- `rating_prediction.ipynb` - notebook version
- `prompts/prompt_versions.py` - the three prompt templates
- `utils/evaluation.py` - evaluation functions
- `data/yelp.csv` - dataset (you need to download this)
