/**
 * User Dashboard Component
 * Public-facing interface for submitting reviews.
 */

import React, { useState } from 'react';
import { submitReview } from '../services/api';
import './UserDashboard.css';

function UserDashboard() {
  const [rating, setRating] = useState(0);
  const [reviewText, setReviewText] = useState('');
  const [aiResponse, setAiResponse] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleRatingClick = (value) => {
    setRating(value);
    setError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess(false);
    setAiResponse('');

    if (rating === 0) {
      setError('Please select a rating');
      return;
    }

    if (!reviewText.trim()) {
      setError('Please write a review');
      return;
    }

    if (reviewText.length > 5000) {
      setError('Review is too long. Maximum 5000 characters.');
      return;
    }

    setIsSubmitting(true);

    try {
      const result = await submitReview(rating, reviewText);
      
      if (result.success) {
        setAiResponse(result.data.ai_response);
        setSuccess(true);
        setReviewText('');
        setRating(0);
      } else {
        setError(result.error || 'Failed to submit review');
      }
    } catch (err) {
      setError('An unexpected error occurred. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="user-dashboard">
      <div className="dashboard-container">
        <h1>Submit Your Review</h1>
        <p className="subtitle">We value your feedback. Please share your experience with us.</p>

        <form onSubmit={handleSubmit} className="review-form">
          <div className="rating-section">
            <label>Rating</label>
            <div className="star-rating">
              {[1, 2, 3, 4, 5].map((value) => (
                <button
                  key={value}
                  type="button"
                  className={`star-button ${rating >= value ? 'selected' : ''}`}
                  onClick={() => handleRatingClick(value)}
                  disabled={isSubmitting}
                >
                  ★
                </button>
              ))}
            </div>
          </div>

          <div className="review-section">
            <label htmlFor="review-text">Your Review</label>
            <textarea
              id="review-text"
              value={reviewText}
              onChange={(e) => setReviewText(e.target.value)}
              placeholder="Write your review here..."
              rows="6"
              maxLength={5000}
              disabled={isSubmitting}
            />
            <div className="char-count">{reviewText.length} / 5000</div>
          </div>

          {error && <div className="error-message">{error}</div>}

          <button
            type="submit"
            className="submit-button"
            disabled={isSubmitting || rating === 0 || !reviewText.trim()}
          >
            {isSubmitting ? 'Submitting...' : 'Submit Review'}
          </button>
        </form>

        {success && aiResponse && (
          <div className="ai-response-section">
            <h2>Thank you for your feedback!</h2>
            <div className="ai-response-box">
              <p>{aiResponse}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default UserDashboard;
