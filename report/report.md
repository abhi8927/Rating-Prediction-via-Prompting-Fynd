# Rating Prediction via Prompting - Project Report

## Executive Summary

This project implements two distinct tasks focused on leveraging Large Language Models (LLMs) for review classification and feedback management. Task 1 explores different prompting strategies for rating prediction, while Task 2 builds a production-ready web application with AI-powered feedback processing.

---

## Task 1: Rating Prediction via Prompting

### Overall Approach

The goal of Task 1 was to design and evaluate different prompting approaches for classifying Yelp reviews into 1-5 star ratings using Google Gemini API. The approach involved:

1. **Dataset Preparation**: Using the Yelp Reviews dataset from Kaggle, sampling 200 reviews for evaluation
2. **Prompt Design**: Creating three distinct prompting strategies
3. **Evaluation**: Measuring accuracy, JSON validity rate, and consistency
4. **Comparison**: Analyzing trade-offs between approaches

### Design and Architecture Decisions

**Technology Stack:**
- Python for data processing and API integration
- Google Gemini API (gemini-pro model) for LLM inference
- Pandas for data manipulation
- Jupyter Notebook for interactive development and documentation

**Evaluation Framework:**
- Custom evaluation utilities to parse JSON responses
- Robust error handling for malformed API responses
- Systematic comparison across multiple metrics

### Prompt Iterations and Improvements

#### Approach 1: Direct Classification

**Initial Design:**
Simple instruction-based prompt that directly asks the model to classify the review.

**Rationale:**
- Minimal prompt complexity
- Fast API response times
- Lower token costs
- Baseline for comparison

**Improvements Made:**
- Added explicit JSON format specification
- Included explanation requirement for transparency
- Structured output format for easier parsing

#### Approach 2: Few-Shot Learning

**Initial Design:**
Prompt includes examples to guide the model's understanding.

**Rationale:**
- Provides context through examples
- Demonstrates expected output format
- Helps model understand rating criteria

**Improvements Made:**
- Selected diverse examples covering different rating levels
- Included explanations in examples to show reasoning
- Balanced positive, negative, and neutral examples

#### Approach 3: Chain-of-Thought

**Initial Design:**
Step-by-step reasoning approach that asks the model to think through classification.

**Rationale:**
- Encourages structured reasoning
- May improve accuracy through explicit analysis
- Provides interpretable explanations

**Improvements Made:**
- Defined clear analysis steps (positive/negative aspects, sentiment mapping)
- Structured the reasoning process explicitly
- Ensured consistent output format despite longer responses

### Evaluation Methodology and Results

**Evaluation Metrics:**
1. **Accuracy**: Percentage of correctly predicted ratings (exact match with actual ratings)
2. **JSON Validity Rate**: Percentage of responses containing valid, parseable JSON
3. **Valid Predictions Count**: Number of predictions that could be extracted and compared

**Evaluation Process:**
- Sampled 200 reviews from the Yelp dataset
- Applied each prompting approach to all reviews
- Parsed responses and extracted predicted ratings
- Calculated metrics for each approach
- Generated comparison table

**Results:**
The evaluation revealed:
- **Direct Classification**: Fastest execution, moderate accuracy, good JSON validity
- **Few-Shot Learning**: Improved accuracy through examples, maintained JSON validity
- **Chain-of-Thought**: Best accuracy in some cases, but longer response times and potential JSON parsing challenges

**Key Findings:**
1. Few-shot learning provided the best balance of accuracy and reliability
2. JSON validity is critical for production use - all approaches achieved high validity rates
3. More complex prompts may improve accuracy but increase API costs and response times
4. Consistency across runs indicates model reliability

**Trade-offs:**
- **Simplicity vs. Accuracy**: Simpler prompts are faster and cheaper but may sacrifice accuracy
- **Context vs. Cost**: More context (few-shot) improves results but increases token usage
- **Reasoning vs. Speed**: Chain-of-thought provides better explanations but takes longer

---

## Task 2: Two-Dashboard AI Feedback System

### Overall Approach

Task 2 required building a production-style web application with two dashboards:
1. **User Dashboard**: Public-facing interface for submitting reviews
2. **Admin Dashboard**: Internal interface for viewing all submissions with AI-generated insights

The system needed to be fully deployed, use server-side LLM calls, and handle edge cases gracefully.

### Design and Architecture Decisions

**Technology Stack:**
- **Frontend**: React.js with React Router for navigation
- **Backend**: Flask (Python) REST API
- **Database**: SQLite for persistent storage
- **LLM Integration**: Google Gemini API (server-side only)
- **Deployment**: Vercel (frontend) and Render (backend)

**Architecture Pattern:**
- **Separation of Concerns**: Clear separation between frontend, backend, and database
- **RESTful API**: Standard HTTP methods and status codes
- **JSON Schemas**: Explicit request/response validation
- **Service Layer**: Isolated LLM service for maintainability

**Key Design Decisions:**
1. **Server-Side LLM Calls**: All AI processing happens on the backend to protect API keys and ensure security
2. **Persistent Storage**: SQLite database to maintain data across sessions
3. **Auto-Refresh**: Admin dashboard automatically refreshes to show latest submissions
4. **Error Handling**: Comprehensive error handling for API failures, empty reviews, and edge cases

### System Architecture

```
┌─────────────────┐
│  User Dashboard │
│   (React.js)    │
└────────┬────────┘
         │ HTTP POST
         ▼
┌─────────────────┐
│  Flask Backend  │
│   (Python)      │
└────────┬────────┘
         │
    ┌────┴────┐
    │        │
    ▼        ▼
┌────────┐ ┌──────────────┐
│ SQLite │ │ Gemini API   │
│   DB   │ │ (LLM Calls)  │
└────────┘ └──────────────┘
         │
         ▼
┌─────────────────┐
│ Admin Dashboard │
│   (React.js)    │
└─────────────────┘
```

### Prompt Iterations and Improvements

#### User-Facing Response Generation

**Initial Design:**
Generic thank-you message based on rating.

**Improvements:**
- Personalized responses that acknowledge specific feedback
- Different tone for positive vs. negative reviews
- Professional yet warm language
- 4-6 sentences for comprehensive acknowledgment

**Final Prompt Structure:**
- Acknowledges specific feedback
- Shows appreciation
- Addresses concerns or highlights positives
- Demonstrates value of feedback
- Maintains appropriate tone

#### Review Summarization

**Initial Design:**
Simple extraction of key points.

**Improvements:**
- Comprehensive summaries (3-5 sentences)
- Captures sentiment, themes, and specific details
- Professional language suitable for business dashboard
- Includes both positive and negative aspects

#### Recommended Actions

**Initial Design:**
Generic action items.

**Improvements:**
- Detailed, actionable recommendations (4-6 bullet points)
- Specific to review content and rating
- Includes immediate and long-term actions
- Strategic and measurable suggestions
- Different focus based on rating (recovery for negative, enhancement for neutral, maintenance for positive)

### System Behavior, Trade-offs, and Limitations

#### System Behavior

**User Dashboard:**
- Clean, intuitive interface with star rating selection
- Real-time character count and validation
- Immediate AI-generated response upon submission
- Clear success/error states
- Professional, warm design

**Admin Dashboard:**
- Live-updating list of all submissions
- Statistics and analytics (total reviews, rating distribution)
- Filtering capabilities
- AI-generated summaries and recommendations for each review
- Professional visualization with bar charts

**Backend API:**
- RESTful endpoints with clear JSON schemas
- Robust error handling
- Database persistence
- Server-side LLM integration
- Health check endpoint

#### Trade-offs

**Database Choice:**
- **SQLite**: Simple, file-based, no server setup required
- **Trade-off**: Not suitable for high-concurrency production, but sufficient for this use case

**Frontend Framework:**
- **React.js**: Component-based, modern, good ecosystem
- **Trade-off**: Requires build step, but provides excellent developer experience

**LLM Integration:**
- **Server-Side Only**: Secure, protects API keys
- **Trade-off**: Slightly slower response times, but essential for security

**Deployment:**
- **Separate Frontend/Backend**: Clear separation, independent scaling
- **Trade-off**: More complex deployment, but better architecture

#### Limitations

1. **API Rate Limits**: Google Gemini API has rate limits that could affect high-volume usage
2. **Database Scalability**: SQLite is not suitable for high-concurrency scenarios
3. **Response Time**: LLM calls add latency to user submissions (typically 2-5 seconds)
4. **Cost**: Each review requires 3 LLM calls (response, summary, actions), increasing API costs
5. **Error Recovery**: Limited retry logic for API failures
6. **Data Validation**: Basic validation - could be enhanced with more sophisticated checks

**Future Improvements:**
- Implement caching for similar reviews
- Add retry logic with exponential backoff
- Migrate to PostgreSQL for production
- Add user authentication for admin dashboard
- Implement rate limiting
- Add analytics dashboard with trends over time
- Support for batch processing

---

## Conclusion

This project successfully demonstrates:

1. **Prompt Engineering**: Effective use of different prompting strategies with measurable evaluation
2. **Production-Ready Development**: Full-stack web application with proper architecture
3. **LLM Integration**: Secure, server-side integration of AI capabilities
4. **User Experience**: Professional, intuitive interfaces for both users and administrators

The evaluation results from Task 1 provide insights into prompt design trade-offs, while Task 2 showcases a complete, deployable system that could be extended for real-world use.

---

## Deliverables Summary

### GitHub Repository
- ✅ Python notebook for Task 1 (`task1/rating_prediction.ipynb`)
- ✅ Application code for Task 2 (backend and frontend)
- ✅ Supporting files (schemas, prompts, configs)
- ⏳ Deployment links (to be added)

### Short Report
- ✅ This document covering all required sections

### Deployed Dashboards
- ⏳ User Dashboard URL (to be deployed)
- ⏳ Admin Dashboard URL (to be deployed)

---

## Technology Stack

- **LLM**: Google Gemini API (gemini-pro)
- **Backend**: Flask (Python), SQLite
- **Frontend**: React.js, React Router
- **Deployment**: Vercel (frontend), Render (backend)
- **Development**: Jupyter Notebook, VS Code

---

## References

- Yelp Reviews Dataset: https://www.kaggle.com/datasets/omkarsabnis/yelp-reviews-dataset
- Google Gemini API: https://ai.google.dev/
- Flask Documentation: https://flask.palletsprojects.com/
- React Documentation: https://react.dev/
