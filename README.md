# Yelp Rating Prediction & AI Feedback System

## Assignment Overview

This repository contains the complete implementation for a two-part assignment focusing on LLM-based rating prediction and a production-style feedback system.

## 📋 Tasks

### Task 1: Rating Prediction via Prompting
Design and evaluate multiple prompting approaches to classify Yelp reviews into 1–5 star ratings using LLMs.

### Task 2: Two-Dashboard AI Feedback System
Build a production-style web application with User and Admin dashboards for managing customer feedback.

---

## 🎯 Task 1: Rating Prediction via Prompting

### Objective
Classify Yelp reviews into 1–5 star ratings using prompt engineering, returning structured JSON responses.

### Dataset
- **Source**: [Yelp Reviews Dataset](https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset) from Kaggle
- **Sample Size**: ~200 rows (for evaluation)

### Output Format
```json
{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the assigned rating."
}
```

### Requirements
- ✅ Implement at least **3 different prompting approaches**
- ✅ Evaluate on:
  - Accuracy (Actual vs Predicted)
  - JSON validity rate
  - Reliability and consistency
- ✅ Provide comparison table and discussion of results

### Implementation
- **Location**: `task1/rating_prediction.ipynb`
- **Prompt Versions**: Stored in `task1/prompts/`
- **Evaluation Metrics**: Calculated in `task1/utils/evaluation.py`

---

## 🌐 Task 2: Two-Dashboard AI Feedback System

### Architecture
- **Frontend**: React.js (User & Admin Dashboards)
- **Backend**: Flask (Python) with RESTful API
- **Database**: SQLite (persistent data storage)
- **LLM**: Google Gemini API (server-side only)

### A. User Dashboard (Public-Facing)

**Features:**
- ⭐ Star rating selector (1–5)
- 📝 Review text input
- ✉️ Submit review functionality
- 🤖 AI-generated response display
- ✅ Success/error state handling

**User Flow:**
1. User selects rating and writes review
2. Submits review
3. Receives AI-generated response
4. Review is stored in database

### B. Admin Dashboard (Internal-Facing)

**Features:**
- 📊 Live-updating list of all submissions
- 📈 Analytics dashboard:
  - Count by rating
  - Total submissions
  - Recent submissions filter
  - Rating trends
- 📋 Display for each submission:
  - User rating
  - User review text
  - AI-generated summary
  - AI-suggested recommended actions
- 🔄 Auto-refresh functionality

### Technical Requirements

**Mandatory Constraints:**
- ❌ **NOT allowed**: Streamlit, HuggingFace Spaces, Gradio, or notebook-based apps
- ✅ **Required**: Real web application deployed on Vercel/Render
- ✅ All LLM calls must be **server-side only**
- ✅ Backend must expose clear **API endpoints**
- ✅ Request/response payloads use **explicit JSON schemas**
- ✅ Error handling for:
  - Empty reviews
  - Long reviews
  - LLM/API failures

**LLM Usage:**
- Review summarization
- Recommended next actions
- User-facing responses

---

## 📁 Project Structure

```
fynd-assignment/
├── task1/                          # Task 1: Rating Prediction
│   ├── rating_prediction.ipynb     # Main notebook
│   ├── data/
│   │   └── yelp_reviews_sample.csv # Sampled dataset
│   ├── prompts/
│   │   └── prompt_versions.py      # Prompt definitions
│   └── utils/
│       └── evaluation.py            # Evaluation functions
│
├── task2/                          # Task 2: Web Application
│   ├── backend/                    # Flask API
│   │   ├── app.py                  # Flask application
│   │   ├── models.py               # Database models
│   │   ├── schemas.py              # JSON schemas
│   │   ├── services/
│   │   │   └── gemini_service.py   # LLM integration
│   │   ├── routes/
│   │   │   ├── reviews.py          # Review endpoints
│   │   │   └── admin.py            # Admin endpoints
│   │   ├── database.db             # SQLite database
│   │   └── requirements.txt
│   │
│   └── frontend/                   # React Application
│       ├── src/
│       │   ├── components/
│       │   │   ├── UserDashboard.jsx
│       │   │   ├── AdminDashboard.jsx
│       │   │   └── common/
│       │   ├── services/
│       │   │   └── api.js          # API client
│       │   ├── App.jsx
│       │   └── index.js
│       ├── package.json
│       └── public/
│
├── report/                         # Project Report
│   └── report.md                   # Report content (PDF)
│
├── .gitignore
└── README.md
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/abhi8927/Rating-Prediction-via-Prompting-Fynd.git
cd Rating-Prediction-via-Prompting-Fynd
```

#### 2. Task 1 Setup
```bash
cd task1
# Install Jupyter and dependencies
pip install jupyter pandas google-generativeai
# Launch Jupyter
jupyter notebook rating_prediction.ipynb
```

#### 3. Task 2 Backend Setup
```bash
cd task2/backend
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
# Create .env file with:
# GEMINI_API_KEY=your_api_key_here

# Run the server
python app.py
```

#### 4. Task 2 Frontend Setup
```bash
cd task2/frontend
# Install dependencies
npm install

# Set environment variables
# Create .env file with:
# REACT_APP_API_URL=http://localhost:5000

# Run development server
npm start
```

---

## 🌍 Deployment

### Deployment Links

- **User Dashboard**: [To be deployed]
- **Admin Dashboard**: [To be deployed]

### Deployment Platforms
- **Frontend**: Vercel or Render
- **Backend**: Render or similar platform

### Deployment Requirements
- ✅ Both dashboards must be publicly accessible
- ✅ Data must persist across refreshes
- ✅ Function without manual intervention
- ✅ Load successfully

---

## 📊 Evaluation & Results

### Task 1 Evaluation Metrics
- **Accuracy**: Percentage of correctly predicted ratings
- **JSON Validity Rate**: Percentage of valid JSON responses
- **Consistency**: Reliability across multiple runs

Results and comparison table will be available in the notebook and report.

---

## 📄 Deliverables

### 1. GitHub Repository ✅
- [x] Python notebook for Task 1
- [x] Application code for Task 2
- [x] Supporting files (schemas, prompts, configs)
- [ ] Deployment links (in progress)

### 2. Short Report
- Overall approach
- Design and architecture decisions
- Prompt iterations and improvements
- Evaluation methodology and results (Task 1)
- System behaviour, trade-offs, and limitations (Task 2)

### 3. Deployed Dashboards
- [ ] User Dashboard URL
- [ ] Admin Dashboard URL

---

## 🔧 Technology Stack

- **LLM**: Google Gemini API
- **Backend**: Flask (Python)
- **Frontend**: React.js
- **Database**: SQLite
- **Deployment**: Vercel / Render

---

## 📝 Notes

- All LLM calls are server-side only (no client-side API calls)
- The system handles edge cases: empty reviews, long reviews, API failures
- Both dashboards read from and write to the same persistent data source
- JSON schemas are explicitly defined for all API endpoints

---

## 👤 Author

**abhi8927**

---

## 📜 License

This project is part of an assignment submission.

---

## 🔗 Links

- **Repository**: https://github.com/abhi8927/Rating-Prediction-via-Prompting-Fynd
- **Dataset**: https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset
- **Gemini API**: https://makersuite.google.com/app/apikey
