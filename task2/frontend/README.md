# Task 2 Frontend: React Application

React-based frontend with two dashboards: User Dashboard for submitting reviews and Admin Dashboard for viewing all submissions.

## Features

- User Dashboard: Submit reviews with star ratings
- Admin Dashboard: View all reviews with AI summaries and recommendations
- Auto-refreshing admin dashboard
- Analytics and filtering
- Responsive design

## Setup

1. Install dependencies:
```bash
npm install
```

2. Set environment variables:
Create a `.env` file:
```
REACT_APP_API_URL=http://localhost:5000
```

3. Run development server:
```bash
npm start
```

The app will open at `http://localhost:3000`

## Routes

- `/` - User Dashboard (public-facing)
- `/admin` - Admin Dashboard (internal)

## Project Structure

- `src/components/`: React components
  - `UserDashboard.jsx`: User review submission interface
  - `AdminDashboard.jsx`: Admin review management interface
- `src/services/`: API client
  - `api.js`: Functions for backend communication
- `src/App.jsx`: Main app with routing

## Building for Production

```bash
npm run build
```

This creates an optimized build in the `build/` directory.
