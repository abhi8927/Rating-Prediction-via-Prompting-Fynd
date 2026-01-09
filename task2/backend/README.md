# Task 2 Backend

Flask API for the feedback system. Handles review submissions, saves to SQLite, and calls Google Gemini API for AI responses.

## Features

- API endpoints for submitting reviews
- Admin endpoints to see all reviews and stats
- SQLite database to store everything
- Google Gemini API integration
- JSON schema validation
- Error handling

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a `.env` file:
```
GEMINI_API_KEY=your_api_key_here
PORT=5000
```

Run the server:
```bash
python app.py
```

Runs on http://localhost:5000

## API Endpoints

**Health check:**
- `GET /api/health` - check if server is running

**User endpoints:**
- `POST /api/reviews` - submit a review
  - Body: `{"user_rating": 1-5, "user_review": "text"}`
  - Returns: review data with AI response

**Admin endpoints:**
- `GET /api/admin/reviews` - get all reviews
- `GET /api/admin/stats` - get statistics

## Database

SQLite database (`database.db`) gets created automatically. Stores:
- User rating (1-5)
- Review text
- AI-generated response
- AI summary
- Recommended actions
- Timestamp

## Files

- `app.py` - main Flask app
- `models.py` - database models
- `schemas.py` - JSON validation
- `routes/` - API endpoints
- `services/` - Gemini API integration
