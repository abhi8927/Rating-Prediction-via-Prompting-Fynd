# Yelp Rating Prediction and AI Feedback System

This repository contains my implementation for a two-part assignment. The first part focuses on using prompt engineering to predict Yelp review ratings, and the second part is a web application with user and admin dashboards for managing feedback.

## Tasks Overview

### Task 1: Rating Prediction via Prompting

The goal here is to classify Yelp reviews into star ratings (1 to 5) using different prompting strategies with LLMs. I'll be testing multiple approaches and comparing their effectiveness.

### Task 2: Two-Dashboard AI Feedback System

This is a full web application with two separate dashboards - one for users to submit reviews and one for admins to view and manage all submissions. Both need to be deployed and fully functional.

---

## Task 1 Details

### What I'm Building

I'm creating a system that takes Yelp reviews and predicts their star rating using prompt engineering. The output needs to be in a specific JSON format with the predicted rating and an explanation.

### Dataset

I'm using the Yelp Reviews dataset from Kaggle. The link is: https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset

For evaluation purposes, I'll be working with a sample of around 200 rows to keep things manageable.

### Expected Output

The system should return JSON in this format:
```json
{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the assigned rating."
}
```

### Requirements

I need to implement at least three different prompting approaches. Each one will be evaluated on:
- How accurate the predictions are compared to actual ratings
- Whether the JSON responses are valid
- How consistent and reliable the results are across multiple runs

I'll create a comparison table showing how each approach performs and discuss the trade-offs.

### Where the Code Lives

The main notebook is in `task1/rating_prediction.ipynb`. There's also a Python script version at `task1/rating_prediction.py` for command-line execution. I've organized the prompts in `task1/prompts/` and evaluation functions in `task1/utils/evaluation.py`.

---

## Task 2 Details

### Architecture Overview

I'm building this with:
- React.js for the frontend (both dashboards)
- Flask for the backend API
- SQLite for storing data
- Google Gemini API for all LLM functionality (everything runs server-side)

### User Dashboard

This is the public-facing page where users can submit reviews. Here's what it does:

Users can select a star rating from 1 to 5, write their review text, and submit it. When they submit, they'll see an AI-generated response. The system handles success and error states clearly, and all submissions get stored in the database.

The flow is straightforward: select rating, write review, submit, see AI response, done.

### Admin Dashboard

This is the internal dashboard for viewing all submissions. It shows:

A live-updating list of every submission with the user's rating, their review text, an AI-generated summary, and AI-suggested actions. I've also added some analytics like counts by rating, total submissions, filters for recent submissions, and basic trend information.

The dashboard auto-refreshes so admins always see the latest data.

### Technical Requirements

There are some important constraints here:

- Cannot use Streamlit, HuggingFace Spaces, Gradio, or any notebook-based apps
- Must be a real web application deployed on platforms like Vercel or Render
- All LLM calls must happen server-side only (no client-side API calls)
- Backend needs clear API endpoints
- All request and response payloads must use explicit JSON schemas
- Must handle edge cases: empty reviews, very long reviews, and LLM/API failures gracefully

The LLM is used for three main things: summarizing reviews, suggesting recommended actions, and generating user-facing responses.

---

## Project Structure

Here's how I've organized the code:

```
fynd-assignment/
├── task1/
│   ├── rating_prediction.ipynb
│   ├── rating_prediction.py
│   ├── data/
│   │   └── yelp.csv
│   ├── prompts/
│   │   └── prompt_versions.py
│   └── utils/
│       └── evaluation.py
│
├── task2/
│   ├── backend/
│   │   ├── app.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── services/
│   │   │   └── gemini_service.py
│   │   ├── routes/
│   │   │   ├── reviews.py
│   │   │   └── admin.py
│   │   ├── database.db
│   │   └── requirements.txt
│   │
│   └── frontend/
│       ├── src/
│       │   ├── components/
│       │   │   ├── UserDashboard.jsx
│       │   │   ├── AdminDashboard.jsx
│       │   │   └── common/
│       │   ├── services/
│       │   │   └── api.js
│       │   ├── App.jsx
│       │   └── index.js
│       ├── package.json
│       └── public/
│
├── report/
│   └── report.md
│
├── .gitignore
└── README.md
```

---

## Setup Instructions

### What You Need

- Python 3.8 or higher
- Node.js 16 or higher
- Git
- A Google Gemini API key (you can get one at https://makersuite.google.com/app/apikey)

### Getting Started

First, clone the repository:
```bash
git clone https://github.com/abhi8927/Rating-Prediction-via-Prompting-Fynd.git
cd Rating-Prediction-via-Prompting-Fynd
```

### Setting Up Task 1

Navigate to the task1 directory and install the required packages:
```bash
cd task1
pip install jupyter pandas google-generativeai python-dotenv
```

Create a `.env` file in the task1 directory with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

**Option 1: Run as Jupyter Notebook**
```bash
jupyter notebook rating_prediction.ipynb
```

**Option 2: Run as Python Script**
```bash
python rating_prediction.py
```

The dataset file `yelp.csv` should be placed in the `task1/data/` directory.

### Setting Up Task 2 Backend

Go to the backend directory:
```bash
cd task2/backend
```

Create a virtual environment (recommended):
```bash
python -m venv venv
```

On Windows, activate it with:
```bash
venv\Scripts\activate
```

On Mac/Linux:
```bash
source venv/bin/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Create a `.env` file in the backend directory with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

Run the server:
```bash
python app.py
```

### Setting Up Task 2 Frontend

Navigate to the frontend directory:
```bash
cd task2/frontend
```

Install the dependencies:
```bash
npm install
```

Create a `.env` file with the backend API URL:
```
REACT_APP_API_URL=http://localhost:5000
```

Start the development server:
```bash
npm start
```

---

## Deployment

### Deployment Links

User Dashboard: ⏳ To be deployed  
Admin Dashboard: ⏳ To be deployed

### Deployment Plan

- Frontend: Vercel or Render
- Backend: Render or similar platform

### Deployment Requirements

Both dashboards must be:
- Publicly accessible via URLs
- Functional without local setup
- Data must persist across page refreshes
- Pages must load successfully

---

## Evaluation and Results

### Task 1 Metrics

The evaluation measures:
- **Accuracy**: Percentage of predictions that match the actual ratings
- **JSON validity rate**: Percentage of responses that contain valid, parseable JSON
- **Consistency**: Reliability of results across multiple runs

The full results, comparison table, and detailed analysis are available in:
- The Jupyter notebook: `task1/rating_prediction.ipynb`
- The project report: `report/report.md`

---

## Deliverables

### GitHub Repository

- ✅ Python notebook for Task 1 (`task1/rating_prediction.ipynb`)
- ✅ Application code for Task 2 (backend and frontend)
- ✅ Supporting files (schemas, prompts, configs, evaluation utilities)
- ⏳ Deployment links (to be added)

### Short Report

The report is available at `report/report.md` and covers:
- Overall approach to both tasks
- Design and architecture decisions
- Prompt iterations and improvements
- Evaluation methodology and results for Task 1
- System behavior, trade-offs, and limitations for Task 2

The report can be converted to PDF format for submission.

### Deployed Dashboards

⏳ Both dashboards need to be fully deployed with public URLs (deployment in progress).

---

## Technology Stack

- LLM: Google Gemini API
- Backend: Flask (Python)
- Frontend: React.js
- Database: SQLite
- Deployment: Vercel / Render

---

## Important Notes

All LLM calls happen server-side only - there are no client-side API calls to LLMs. The system handles edge cases like empty reviews, very long reviews, and API failures. Both dashboards read from and write to the same database, so data stays consistent. All API endpoints use explicit JSON schemas for requests and responses.

---

## Author

abhi8927

---

## License

This project is part of an assignment submission.

---

## Links

Repository: https://github.com/abhi8927/Rating-Prediction-via-Prompting-Fynd
Dataset: https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset
Gemini API: https://makersuite.google.com/app/apikey
