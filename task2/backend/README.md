# Task 2 Backend: Flask API

Flask-based REST API for the AI Feedback System. Handles review submissions, stores data in SQLite, and integrates with Google Gemini API for AI responses.

## Features

- RESTful API endpoints for review submission
- Admin endpoints for viewing all reviews and analytics
- SQLite database for persistent storage
- Google Gemini API integration for AI responses
- JSON schema validation for all requests/responses
- Error handling for edge cases

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
Create a `.env` file:
```
GEMINI_API_KEY=your_api_key_here
PORT=5000
```

3. Run the server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
- `GET /api/health` - Check if API is running

### User Endpoints
- `POST /api/reviews` - Submit a new review
  - Request body: `{"user_rating": 1-5, "user_review": "text"}`
  - Returns: Review data with AI response

### Admin Endpoints
- `GET /api/admin/reviews` - Get all reviews
- `GET /api/admin/stats` - Get analytics statistics

## Database

SQLite database (`database.db`) is automatically created on first run. The `Review` model stores:
- User rating (1-5)
- User review text
- AI-generated response
- AI summary
- Recommended actions
- Timestamp

## Project Structure

- `app.py`: Main Flask application
- `models.py`: Database models
- `schemas.py`: JSON validation schemas
- `routes/`: API route handlers
- `services/`: External service integrations (Gemini API)
