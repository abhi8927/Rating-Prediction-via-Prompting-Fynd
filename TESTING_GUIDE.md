# Testing Guide for Task 2 Web Application

## Prerequisites

Make sure both servers are running:

1. **Backend Server** (Flask API):
   ```bash
   cd task2/backend
   python app.py
   ```
   Should show: "Running on http://127.0.0.1:5000"

2. **Frontend Server** (React App):
   ```bash
   cd task2/frontend
   npm start
   ```
   Should open automatically at http://localhost:3000

## Testing User Dashboard

### Step 1: Open User Dashboard
- Go to: http://localhost:3000
- You should see the review submission form

### Step 2: Test Review Submission

**Test Case 1: Valid Review**
1. Select a star rating (click stars 1-5)
2. Enter a review text (e.g., "Great service and food!")
3. Click "Submit Review"
4. **Expected**: You should see an AI-generated response below the form

**Test Case 2: Empty Review**
1. Select a rating but leave review text empty
2. Click "Submit Review"
3. **Expected**: Error message "Please write a review"

**Test Case 3: No Rating Selected**
1. Write a review but don't select a rating
2. Click "Submit Review"
3. **Expected**: Error message "Please select a rating"

**Test Case 4: Long Review**
1. Enter a review longer than 5000 characters
2. **Expected**: Error message "Review is too long"

### Step 3: Verify AI Response
- After successful submission, check that:
  - AI response is displayed (4-6 sentences, professional)
  - Form clears after submission
  - Success state is shown

## Testing Admin Dashboard

### Step 1: Open Admin Dashboard
- Go to: http://localhost:3000/admin
- Or click "Admin Dashboard" in the navigation

### Step 2: Verify Features

**Check 1: All Reviews Display**
- Should see all submitted reviews
- Each review card should show:
  - User rating (as a badge)
  - User review text
  - AI-generated summary
  - AI-suggested recommended actions
  - Timestamp

**Check 2: Analytics Section**
- Should see stat cards showing:
  - Total reviews count
  - Count by each rating (1-5 stars)

**Check 3: Filter Functionality**
- Use the "Filter by Rating" dropdown
- Select different ratings
- **Expected**: Only reviews with that rating are shown

**Check 4: Auto-Refresh**
- Submit a new review from User Dashboard
- Wait 10 seconds (or click Refresh button)
- **Expected**: New review appears in Admin Dashboard

**Check 5: Empty State**
- If no reviews exist, should show "No reviews found"

## Testing API Endpoints Directly

You can also test the backend API directly:

### Health Check
```bash
curl http://localhost:5000/api/health
```
Expected: `{"status": "ok", "message": "API is running"}`

### Submit Review
```bash
curl -X POST http://localhost:5000/api/reviews \
  -H "Content-Type: application/json" \
  -d '{"user_rating": 4, "user_review": "Great experience!"}'
```

### Get All Reviews
```bash
curl http://localhost:5000/api/admin/reviews
```

### Get Statistics
```bash
curl http://localhost:5000/api/admin/stats
```

## Common Issues

**Issue: "Network error. Please check your connection."**
- Solution: Make sure backend is running on port 5000

**Issue: Frontend won't load**
- Solution: Make sure npm start is running and wait for compilation

**Issue: API calls fail**
- Solution: Check backend console for errors
- Verify GEMINI_API_KEY is set correctly

## What to Verify

✅ User can submit reviews with rating and text
✅ AI generates professional responses
✅ Reviews are stored in database
✅ Admin can see all reviews
✅ AI summaries and recommendations are shown
✅ Analytics display correctly
✅ Filtering works
✅ Auto-refresh works
✅ Error handling works (empty reviews, etc.)
