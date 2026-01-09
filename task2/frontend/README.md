# Task 2 Frontend

React app with two dashboards: one for users to submit reviews, one for admins to see all submissions.

## Features

- User dashboard to submit reviews with ratings
- Admin dashboard to view all reviews with AI summaries
- Auto-refreshing admin dashboard
- Stats and filters
- Responsive design

## Setup

Install dependencies:
```bash
npm install
```

Create a `.env` file:
```
REACT_APP_API_URL=http://localhost:5000
```

Run the dev server:
```bash
npm start
```

Opens at http://localhost:3000

## Routes

- `/` - User dashboard (public)
- `/admin` - Admin dashboard (internal)

## Files

- `src/components/UserDashboard.jsx` - user review form
- `src/components/AdminDashboard.jsx` - admin view
- `src/services/api.js` - API calls
- `src/App.jsx` - routing

## Build

```bash
npm run build
```

Creates production build in `build/` folder.
