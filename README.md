# Yelp Rating Prediction and Feedback System

## 🚀 Live Deployment

**Frontend (User Dashboard):** https://feedback-prediction-frontend-fynd.onrender.com/  
**Admin Dashboard:** https://feedback-prediction-frontend-fynd.onrender.com/admin  
**Backend API:** https://feedback-prediction-fynd.onrender.com

---

This is my assignment submission with two parts. First part is about predicting Yelp review ratings using different prompt strategies. Second part is a web app with two dashboards for handling user feedback.

## What's in Here

### Task 1: Rating Prediction

I built a system that takes Yelp reviews and guesses their star rating (1-5) using different ways of asking the AI. Tried three different approaches and compared how well they work.

The dataset comes from Kaggle: https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset

I used about 200 reviews for testing. The system returns JSON like this:
```json
{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the assigned rating."
}
```

I tested three different prompting methods:
- Direct classification (just ask directly)
- Few-shot learning (give examples)
- Chain-of-thought (step by step reasoning)

Each one gets measured on accuracy, whether the JSON is valid, and how consistent the results are.

The code is in `task1/rating_prediction.ipynb` (notebook) or `task1/rating_prediction.py` (script). Prompts are in `task1/prompts/` and evaluation code is in `task1/utils/evaluation.py`.

### Task 2: Two Dashboards for Feedback

Built a web app with React frontend and Flask backend. Two dashboards:

**User Dashboard**: People can pick a star rating, write a review, and submit it. They get an AI response back. Everything gets saved to a database.

**Admin Dashboard**: Shows all the reviews that came in. Each one has the user's rating, their review text, an AI summary, and suggested actions. Also shows some stats like total reviews and breakdown by rating. Refreshes automatically so you always see the latest.

**Tech stack:**
- React.js for frontend
- Flask for backend API
- SQLite for database
- Google Gemini API for all the AI stuff (runs on server only)

**Important rules:**
- Can't use Streamlit, HuggingFace, Gradio, or notebook-based apps
- Must be a real web app deployed somewhere
- All AI calls happen on the server, never in the browser
- API endpoints need clear JSON schemas
- Handles empty reviews, super long reviews, and API failures

The AI does three things: generates responses to users, summarizes reviews for admins, and suggests actions.

## Project Structure

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
│   │   └── requirements.txt
│   │
│   └── frontend/
│       ├── src/
│       │   ├── components/
│       │   │   ├── UserDashboard.jsx
│       │   │   └── AdminDashboard.jsx
│       │   ├── services/
│       │   │   └── api.js
│       │   └── App.jsx
│       └── package.json
│
├── report/
│   └── report.md
│
└── README.md
```

## How to Run

### Prerequisites

- Python 3.8+
- Node.js 16+
- Git
- Google Gemini API key from https://makersuite.google.com/app/apikey

### Task 1 Setup

Go to the task1 folder:
```bash
cd task1
pip install jupyter pandas google-generativeai python-dotenv
```

Create a `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

Run the notebook:
```bash
jupyter notebook rating_prediction.ipynb
```

Or run as a script:
```bash
python rating_prediction.py
```

Make sure `yelp.csv` is in the `task1/data/` folder.

### Task 2 Backend Setup

Go to backend folder:
```bash
cd task2/backend
```

Create virtual environment (optional but recommended):
```bash
python -m venv venv
```

Activate it:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

Install packages:
```bash
pip install -r requirements.txt
```

Create `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

Run the server:
```bash
python app.py
```

Server runs on http://localhost:5000

### Task 2 Frontend Setup

Go to frontend folder:
```bash
cd task2/frontend
```

Install packages:
```bash
npm install
```

Create `.env` file:
```
REACT_APP_API_URL=http://localhost:5000
```

Start the app:
```bash
npm start
```

Opens at http://localhost:3000

## Deployment

✅ **Successfully deployed on Render!**

**Frontend:** https://feedback-prediction-frontend-fynd.onrender.com/  
**Backend:** https://feedback-prediction-fynd.onrender.com

Both dashboards are:
- ✅ Publicly accessible
- ✅ Work without any local setup
- ✅ Keep data when you refresh
- ✅ Load properly

Note: On Render's free tier, services may take 30-60 seconds to wake up if they've been idle for 15+ minutes.

## Results

For Task 1, I measured:
- Accuracy: how many predictions matched the real ratings
- JSON validity: how often the responses were valid JSON
- Consistency: how reliable results were across runs

Full results are in the notebook and the report.

## What's Included

- Task 1 notebook and code
- Task 2 complete web app (backend + frontend)
- All supporting files (schemas, prompts, evaluation code)
- Project report

Deployment links coming soon.

## Tech Used

- Google Gemini API for AI
- Flask for backend
- React.js for frontend
- SQLite for database
- Vercel/Render for deployment (planned)

## Notes

All AI calls happen on the server only - nothing in the browser. The system handles edge cases like empty reviews, super long reviews, and API failures. Both dashboards use the same database so data stays consistent. All API endpoints have explicit JSON schemas.

## Links

Repo: https://github.com/abhi8927/Rating-Prediction-via-Prompting-Fynd  
Dataset: https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset  
Gemini API: https://makersuite.google.com/app/apikey
