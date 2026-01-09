# Project Report

## What This Project Is About

I built two things for this assignment. First part is testing different ways to ask an AI to guess star ratings from Yelp reviews. Second part is a web app where people can leave reviews and admins can see them with AI summaries.

## Task 1: Rating Prediction

### What I Did

I wanted to find out which way of asking the AI gives the best results for predicting star ratings. I used Google Gemini API and tested three different methods on 200 Yelp reviews.

Here's what I did:
1. Downloaded the Yelp dataset from Kaggle
2. Picked 200 reviews to test with
3. Made three different types of prompts
4. Ran each one and checked the results
5. Compared them to see which worked best

### Tech Stuff

I used Python with pandas to work with the data. Google Gemini API for all the AI stuff. Jupyter notebook to run everything. I also wrote some helper code to parse the JSON responses and catch errors.

### The Three Methods I Tried

**Method 1: Just Ask Directly**

I just asked the AI to classify the review. Simple and quick. I made sure to ask for JSON format so I could parse it easily.

**Method 2: Give Examples First**

I gave the AI some examples of reviews and their ratings, then asked it to classify. This helps the AI understand what I'm looking for. I picked examples that covered all rating levels from 1 to 5 stars, with explanations.

**Method 3: Step by Step Thinking**

I asked the AI to think through it step by step - find the good parts, find the bad parts, figure out the overall feeling, then decide on a rating. This takes more time but sometimes gives better results.

### How I Tested Them

I measured three things:
1. Accuracy - how many times the AI got it right
2. JSON validity - how often the response was valid JSON I could actually use
3. Valid predictions - how many I could extract and compare

I ran each method on all 200 reviews, parsed all the responses, and calculated the numbers.

### What I Found

The direct method was fastest but accuracy was just okay. The example method did better on accuracy and still gave me valid JSON most of the time. The step-by-step method sometimes got the best accuracy but took longer and sometimes had issues with parsing.

The main thing I learned: simpler prompts are faster and cheaper but might not be as accurate. More complex prompts can be more accurate but cost more and take longer.

## Task 2: Web App with Two Dashboards

### What I Built

I made a full web app with React for the frontend and Flask for the backend. Users can submit reviews and get AI responses back. Admins can see all the reviews with AI summaries and suggested actions.

### How It's Built

Frontend uses React with routing. Backend is Flask with REST API. Database is SQLite. All the AI calls happen on the server side - never in the browser. This keeps the API keys safe.

Here's how it works: user submits a review → backend saves it → backend calls Gemini API three times (once for user response, once for summary, once for actions) → everything gets saved → user sees their response, admin sees everything.

### Why I Chose These Tools

I picked React because it's good for making interactive UIs. Flask because it's simple and works well for APIs. SQLite because it's easy to set up and works fine for this project.

I kept things separate: frontend handles the UI, backend handles the API and AI calls, database stores everything. I used JSON schemas to make sure all requests and responses are valid.

### The AI Prompts

**User Response**: I made it acknowledge the specific feedback, show appreciation, address any concerns or highlight good points. Different tone for positive vs negative reviews. About 4-6 sentences.

**Summary**: Captures the overall feeling, main points, specific details. About 3-5 sentences. Professional language for business use.

**Actions**: Detailed recommendations that can actually be done. About 4-6 bullet points. Specific to what the review says. Different focus based on rating - recovery for bad reviews, improvement for neutral ones, maintenance for good ones.

### How It Works

User dashboard: pick a rating, write your review, submit it. You see an AI response. Pretty straightforward.

Admin dashboard: see all reviews, check stats, use filters. It refreshes automatically. Each review shows the rating, the text, an AI summary, and suggested actions.

Backend: REST endpoints, validates input, calls the AI, saves to database, handles errors.

### Trade-offs and Limitations

SQLite is simple but not great if you have tons of traffic. React needs a build step but makes development easier. Server-side AI calls are slower but you need them for security.

Some limitations:
- API rate limits could be a problem with lots of traffic
- SQLite won't handle high concurrency well
- AI calls add 2-5 seconds to each submission
- Each review needs 3 AI calls (costs money)
- Basic error recovery

Things I could improve: cache similar reviews, better retry logic, use PostgreSQL for production, add user authentication, rate limiting, analytics over time.

## Deployment

Everything is deployed and working on Render.

**Frontend (User Dashboard):** https://feedback-prediction-frontend-fynd.onrender.com/

**Admin Dashboard:** https://feedback-prediction-frontend-fynd.onrender.com/admin

**Backend API:** https://feedback-prediction-fynd.onrender.com

Both dashboards are publicly accessible and work without any local setup. Data persists across page refreshes. On Render's free tier, services might take 30-60 seconds to wake up if they've been idle for 15+ minutes, but once they're up they work fine.

## What I Learned

Task 1 showed me that different ways of asking the AI have different trade-offs. The example method seemed like the best balance for this use case.

Task 2 is a working web app that could be used for real. The setup is solid and could be scaled up with some changes.

## What's Included

- GitHub repo with all the code: https://github.com/abhi8927/Rating-Prediction-via-Prompting-Fynd
- Task 1 notebook with all the evaluation: `task1/rating_prediction.ipynb`
- Task 2 complete web app (backend and frontend)
- This report
- All deployed and working

Everything is done and deployed.
