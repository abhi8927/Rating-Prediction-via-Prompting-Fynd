# Deployment Guide

This guide covers deploying both the backend and frontend of the AI Feedback System.

## Backend Deployment (Render)

1. **Create a new Web Service on Render:**
   - Go to https://render.com
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

2. **Configure the service:**
   - Name: `fynd-assignment-backend`
   - Environment: Python 3
   - Build Command: `pip install -r task2/backend/requirements.txt`
   - Start Command: `cd task2/backend && python app.py`

3. **Set Environment Variables:**
   - `GEMINI_API_KEY`: Your Gemini API key
   - `PORT`: 5000 (or let Render assign automatically)

4. **Deploy:**
   - Render will automatically deploy on every push to main branch
   - Note the service URL (e.g., `https://fynd-assignment-backend.onrender.com`)

## Frontend Deployment (Vercel)

1. **Create a new project on Vercel:**
   - Go to https://vercel.com
   - Click "Add New Project"
   - Import your GitHub repository

2. **Configure the project:**
   - Framework Preset: Create React App
   - Root Directory: `task2/frontend`
   - Build Command: `npm run build`
   - Output Directory: `build`

3. **Set Environment Variables:**
   - `REACT_APP_API_URL`: Your backend URL from Render (e.g., `https://fynd-assignment-backend.onrender.com`)

4. **Deploy:**
   - Vercel will automatically deploy on every push
   - Note the deployment URL

## Alternative: Full-Stack on Render

You can also deploy both on Render:

1. **Backend:** Deploy as Web Service (as above)
2. **Frontend:** 
   - Build the React app: `cd task2/frontend && npm run build`
   - Serve the build folder from Flask by adding a route in `app.py`:
   ```python
   @app.route('/', defaults={'path': ''})
   @app.route('/<path:path>')
   def serve(path):
       if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
           return send_from_directory(app.static_folder, path)
       else:
           return send_from_directory(app.static_folder, 'index.html')
   ```

## Post-Deployment

1. Update the README with your deployment URLs
2. Test both dashboards are accessible
3. Verify data persistence across refreshes
4. Check that API calls are working correctly

## Notes

- The database (SQLite) will persist on Render's filesystem
- For production, consider using PostgreSQL instead of SQLite
- Make sure CORS is properly configured for your frontend domain
