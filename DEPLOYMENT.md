# Deployment Guide for Render

This guide will help you deploy both the backend and frontend to Render.

## Prerequisites

1. GitHub account with this repository pushed
2. Render account (sign up at https://render.com)
3. Google Gemini API key

## Step 1: Deploy Backend

1. Go to https://dashboard.render.com
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Select the repository: `Rating-Prediction-via-Prompting-Fynd`
5. Configure the service:
   - **Name**: `feedback-system-backend` (or any name you prefer)
   - **Root Directory**: `task2/backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Add Environment Variables:
   - `GEMINI_API_KEY` = your Gemini API key
   - `PORT` = leave empty (Render sets this automatically)
7. Click "Create Web Service"
8. Wait for deployment to complete
9. Copy the service URL (e.g., `https://feedback-system-backend.onrender.com`)

## Step 2: Deploy Frontend

1. In Render dashboard, click "New +" and select "Static Site"
2. Connect your GitHub repository
3. Select the repository: `Rating-Prediction-via-Prompting-Fynd`
4. Configure the service:
   - **Name**: `feedback-system-frontend` (or any name you prefer)
   - **Root Directory**: `task2/frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `build`
5. Add Environment Variable:
   - `REACT_APP_API_URL` = your backend URL from Step 1 (e.g., `https://feedback-system-backend.onrender.com`)
6. Click "Create Static Site"
7. Wait for deployment to complete
8. Copy the frontend URL

## Step 3: Update Backend CORS (if needed)

If you get CORS errors, the backend should already allow all origins. If not, the CORS is configured in `app.py` with `CORS(app)` which allows all origins.

## Step 4: Test Deployment

1. Visit your frontend URL
2. Try submitting a review
3. Visit `/admin` route to see the admin dashboard
4. Check that data persists after refresh

## URLs

After deployment, you'll have:
- **Backend API**: `https://your-backend-name.onrender.com`
- **Frontend**: `https://your-frontend-name.onrender.com`
- **User Dashboard**: `https://your-frontend-name.onrender.com`
- **Admin Dashboard**: `https://your-frontend-name.onrender.com/admin`

## Notes

- Render free tier services spin down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds
- Database (SQLite) persists data across deployments
- Environment variables are set in Render dashboard, not in `.env` files

## Troubleshooting

**Backend not starting:**
- Check build logs in Render dashboard
- Ensure `gunicorn` is in requirements.txt
- Verify `GEMINI_API_KEY` is set

**Frontend can't connect to backend:**
- Check `REACT_APP_API_URL` environment variable
- Ensure backend URL doesn't have trailing slash
- Check browser console for CORS errors

**Database issues:**
- SQLite file is created automatically
- Data persists in Render's filesystem
- For production, consider upgrading to PostgreSQL
