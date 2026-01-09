# Project Report: Rating Prediction and AI Feedback System

## Executive Summary

This project consists of two main components. The first component evaluates different prompting strategies for predicting Yelp review ratings using large language models. The second component is a production-ready web application featuring user and admin dashboards for managing customer feedback with AI-powered analysis.

## Task 1: Rating Prediction via Prompting

### Objective

The goal was to determine which prompting approach yields the best results for predicting star ratings (1-5) from Yelp reviews. The evaluation was conducted using Google Gemini API on a sample of 200 reviews from the Yelp dataset.

### Methodology

The evaluation process involved:
1. Obtaining the Yelp Reviews dataset from Kaggle
2. Sampling 200 reviews for testing purposes
3. Implementing three distinct prompting strategies
4. Executing each approach and collecting results
5. Analyzing and comparing performance metrics

### Technical Implementation

The implementation uses Python with pandas for data processing, Google Gemini API for language model inference, and Jupyter Notebook for interactive development. Custom utilities were developed to parse JSON responses and handle error cases.

### Prompting Approaches

**Approach 1: Direct Classification**

This approach uses a straightforward instruction-based prompt that directly requests the model to classify the review. The prompt includes explicit JSON format requirements to ensure parseable output.

**Approach 2: Few-Shot Learning**

This approach provides the model with example reviews and their corresponding ratings before requesting classification. The examples cover all rating levels (1-5 stars) and include explanations to guide the model's understanding.

**Approach 3: Chain-of-Thought Reasoning**

This approach instructs the model to analyze the review systematically: identify positive aspects, identify negative aspects, determine overall sentiment, and then map the sentiment to an appropriate rating. This method encourages structured reasoning but requires more processing time.

### Evaluation Metrics

Three key metrics were measured:
1. **Accuracy**: Percentage of predictions that exactly matched the actual ratings
2. **JSON Validity Rate**: Percentage of responses containing valid, parseable JSON
3. **Valid Predictions Count**: Number of predictions that could be successfully extracted and compared

Each approach was tested on all 200 reviews, responses were parsed, and metrics were calculated.

### Results and Analysis

The direct classification approach demonstrated the fastest execution time but achieved moderate accuracy. The few-shot learning approach showed improved accuracy while maintaining high JSON validity rates. The chain-of-thought approach occasionally achieved the highest accuracy but required longer processing times and sometimes encountered parsing challenges.

**Key Finding**: There is a clear trade-off between prompt complexity and performance. Simpler prompts are faster and more cost-effective but may sacrifice accuracy. More complex prompts can improve accuracy but increase both cost and processing time.

## Task 2: Two-Dashboard AI Feedback System

### System Overview

A full-stack web application was developed with a React.js frontend and Flask backend. The system enables users to submit reviews and receive AI-generated responses, while administrators can view all submissions with AI-generated summaries and actionable recommendations.

### System Architecture

The frontend is built with React.js and includes client-side routing. The backend is implemented using Flask with a RESTful API. Data persistence is handled by SQLite. All AI operations are performed server-side to maintain security of API credentials.

**Data Flow**: User submits review → Backend validates and stores submission → Backend makes three sequential API calls to Gemini (user response generation, summary generation, action recommendations) → All data is persisted → User receives response, administrator views complete record.

### Design Decisions

React.js was selected for its component-based architecture and strong ecosystem for building interactive user interfaces. Flask was chosen for its simplicity and effectiveness in building REST APIs. SQLite was used for its ease of setup and suitability for this application's requirements.

The architecture follows separation of concerns: the frontend manages user interface, the backend handles API logic and AI integration, and the database provides data persistence. JSON schemas are used throughout to validate all request and response payloads.

### AI Prompt Engineering

**User Response Generation**: The prompt is designed to acknowledge specific feedback, express appreciation, address concerns or highlight positive aspects, and maintain an appropriate tone based on the rating. Responses are typically 4-6 sentences in length.

**Review Summarization**: The summary prompt captures overall sentiment, key themes, and specific details mentioned in the review. Summaries are 3-5 sentences and use professional language suitable for business dashboards.

**Action Recommendations**: The recommendations prompt generates detailed, actionable suggestions. Recommendations include 4-6 bullet points, are specific to the review content, and are tailored based on rating level: recovery strategies for negative reviews, enhancement opportunities for neutral reviews, and maintenance approaches for positive reviews.

### System Functionality

**User Dashboard**: Users select a star rating, enter their review text, and submit. Upon submission, they receive an AI-generated response acknowledging their feedback.

**Admin Dashboard**: Administrators can view all submitted reviews, access statistics and analytics, and use filtering capabilities. The dashboard auto-refreshes to display the latest submissions. Each review entry displays the rating, review text, AI-generated summary, and recommended actions.

**Backend API**: Provides REST endpoints, validates all input, orchestrates AI service calls, manages database operations, and implements comprehensive error handling.

### Trade-offs and Limitations

SQLite provides simplicity but has limitations for high-traffic scenarios. React requires a build step but offers excellent developer experience. Server-side AI calls introduce latency (2-5 seconds per submission) but are necessary for security.

**Current Limitations**:
- API rate limits may become a constraint under high traffic
- SQLite is not suitable for high-concurrency scenarios
- Each review submission requires three AI API calls, increasing costs
- Error recovery mechanisms are basic

**Potential Improvements**: Implement caching for similar reviews, enhance retry logic with exponential backoff, migrate to PostgreSQL for production, add user authentication, implement rate limiting, and develop time-series analytics.

## Deployment

The application has been successfully deployed on Render and is fully operational.

**Frontend (User Dashboard):** https://feedback-prediction-frontend-fynd.onrender.com/

**Admin Dashboard:** https://feedback-prediction-frontend-fynd.onrender.com/admin

**Backend API:** https://feedback-prediction-fynd.onrender.com

Both dashboards are publicly accessible and function without requiring local setup. Data persistence is maintained across page refreshes. Note that on Render's free tier, services may experience a 30-60 second cold start delay after 15 minutes of inactivity, but functionality is fully restored once services are active.

## Conclusions

Task 1 demonstrated that different prompting strategies offer distinct trade-offs in terms of accuracy, cost, and processing time. The few-shot learning approach provided the best balance for this particular use case.

Task 2 resulted in a fully functional web application suitable for production use. The architecture is well-structured and can be scaled with appropriate modifications.

## Deliverables

- **GitHub Repository**: https://github.com/abhi8927/Rating-Prediction-via-Prompting-Fynd
  - Contains all source code, including Task 1 Jupyter notebook and Task 2 complete application
- **Task 1 Notebook**: `task1/rating_prediction.ipynb` with complete evaluation and analysis
- **Task 2 Application**: Fully deployed web application with backend and frontend
- **Project Report**: This document

All components are complete, tested, and deployed.
