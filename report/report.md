# Rating Prediction Project Report

## Overview

This project has two parts. First part is about testing different ways to ask an AI to predict Yelp review ratings. Second part is building a web app where users can submit reviews and admins can see them with AI summaries.

## Task 1: Rating Prediction

### What I Did

I wanted to see which way of asking the AI works best for predicting star ratings. Used Google Gemini API and tested three different approaches on 200 Yelp reviews.

The process was:
1. Get the Yelp dataset from Kaggle
2. Sample 200 reviews for testing
3. Create three different prompt styles
4. Test each one and measure results
5. Compare them

### Tech Choices

Used Python with pandas for handling data. Google Gemini API for the AI calls. Jupyter notebook for running experiments. Built some utilities to parse JSON responses and handle errors.

### The Three Approaches

**Approach 1: Direct Classification**

Just ask the AI directly to classify the review. Simple and fast. Added clear JSON format requirements so the output is easy to parse.

**Approach 2: Few-Shot Learning**

Give the AI some examples first, then ask it to classify. This helps it understand what you want. I picked examples covering different rating levels (1-5 stars) with explanations.

**Approach 3: Chain-of-Thought**

Ask the AI to think through it step by step - identify positives, identify negatives, figure out sentiment, then map to a rating. This takes longer but sometimes gives better results.

### How I Evaluated

Measured three things:
1. Accuracy - how many predictions matched the real ratings
2. JSON validity - how often the response was valid JSON I could parse
3. Valid predictions - how many I could actually extract and compare

Ran each approach on all 200 reviews, parsed the responses, and calculated the metrics.

### Results

Direct classification was fastest but accuracy was okay. Few-shot learning did better on accuracy while keeping JSON validity high. Chain-of-thought sometimes got the best accuracy but took longer and sometimes had parsing issues.

The trade-off is: simpler prompts are faster and cheaper but might not be as accurate. More complex prompts can improve accuracy but cost more and take longer.

## Task 2: Web App with Two Dashboards

### What I Built

A full web app with React frontend and Flask backend. Users can submit reviews and see AI responses. Admins can see all reviews with summaries and action suggestions.

### Architecture

Frontend is React with routing. Backend is Flask with REST API. Database is SQLite. All AI calls happen on the server - never in the browser. This keeps API keys safe.

The flow is: user submits review → backend saves it → backend calls Gemini API three times (user response, summary, actions) → everything gets saved → user sees response, admin sees everything.

### Design Decisions

Chose React because it's good for building interactive UIs. Flask because it's simple and works well for APIs. SQLite because it's easy to set up and works fine for this use case.

Separated concerns: frontend handles UI, backend handles API and AI calls, database stores everything. Used JSON schemas to validate all requests and responses.

### The Prompts

**User Response**: Made it acknowledge specific feedback, show appreciation, address concerns or highlight positives. Different tone for positive vs negative reviews. 4-6 sentences.

**Summary**: Captures sentiment, key themes, specific details. 3-5 sentences. Professional language for business use.

**Actions**: Detailed, actionable recommendations. 4-6 bullet points. Specific to the review content. Different focus based on rating - recovery for bad reviews, enhancement for neutral, maintenance for good ones.

### How It Works

User dashboard: pick rating, write review, submit. See AI response. Simple.

Admin dashboard: see all reviews, stats, filters. Auto-refreshes. Each review shows rating, text, AI summary, and suggested actions.

Backend: REST endpoints, validates input, calls AI, saves to database, handles errors.

### Trade-offs and Limits

SQLite is simple but not great for high traffic. React needs a build step but gives good developer experience. Server-side AI calls are slower but necessary for security.

Limitations:
- API rate limits could be an issue with lots of traffic
- SQLite won't scale to high concurrency
- AI calls add 2-5 seconds to submissions
- Each review needs 3 AI calls (costs money)
- Basic error recovery

Could improve by: caching similar reviews, better retry logic, using PostgreSQL for production, adding user auth, rate limiting, analytics over time.

## Conclusion

Task 1 showed that different prompting strategies have different trade-offs. Few-shot learning seemed like the best balance for this use case.

Task 2 is a working web app that could be extended for real use. The architecture is solid and could scale with some changes.

## Deliverables

- GitHub repo with all code
- Task 1 notebook with evaluation
- Task 2 complete web app
- This report

Deployment is still in progress.
