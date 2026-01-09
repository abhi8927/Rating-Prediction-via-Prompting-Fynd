/**
 * Admin Dashboard Component
 * Internal interface for viewing all reviews and analytics.
 */

import React, { useState, useEffect } from 'react';
import { getAllReviews, getStats } from '../services/api';
import './AdminDashboard.css';

function AdminDashboard() {
  const [reviews, setReviews] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [filterRating, setFilterRating] = useState('all');

  const fetchData = async () => {
    try {
      const [reviewsResult, statsResult] = await Promise.all([
        getAllReviews(),
        getStats(),
      ]);

      if (reviewsResult.success) {
        setReviews(reviewsResult.data);
      } else {
        setError(reviewsResult.error);
      }

      if (statsResult.success) {
        setStats(statsResult.data);
      }
    } catch (err) {
      setError('Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 10000);
    return () => clearInterval(interval);
  }, []);

  const filteredReviews = filterRating === 'all'
    ? reviews
    : reviews.filter(review => review.user_rating === parseInt(filterRating));

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    try {
      const date = new Date(dateString);
      return date.toLocaleString();
    } catch {
      return dateString;
    }
  };

  if (loading) {
    return (
      <div className="admin-dashboard">
        <div className="loading">Loading dashboard...</div>
      </div>
    );
  }

  return (
    <div className="admin-dashboard">
      <div className="dashboard-header">
        <h1>Admin Dashboard</h1>
        <button onClick={fetchData} className="refresh-button">
          Refresh
        </button>
      </div>

      {error && <div className="error-banner">{error}</div>}

      {stats && (
        <div className="stats-section">
          <div className="stat-card">
            <div className="stat-value">{stats.total_reviews}</div>
            <div className="stat-label">Total Reviews</div>
          </div>
          {Object.entries(stats.rating_distribution || {}).map(([rating, count]) => (
            <div key={rating} className="stat-card">
              <div className="stat-value">{count}</div>
              <div className="stat-label">{rating} Star{count !== 1 ? 's' : ''}</div>
            </div>
          ))}
        </div>
      )}

      <div className="filters-section">
        <label>Filter by Rating:</label>
        <select
          value={filterRating}
          onChange={(e) => setFilterRating(e.target.value)}
          className="filter-select"
        >
          <option value="all">All Ratings</option>
          <option value="5">5 Stars</option>
          <option value="4">4 Stars</option>
          <option value="3">3 Stars</option>
          <option value="2">2 Stars</option>
          <option value="1">1 Star</option>
        </select>
      </div>

      <div className="reviews-list">
        <h2>All Submissions ({filteredReviews.length})</h2>
        {filteredReviews.length === 0 ? (
          <div className="empty-state">No reviews found</div>
        ) : (
          filteredReviews.map((review) => (
            <div key={review.review_id} className="review-card">
              <div className="review-header">
                <div className="rating-badge">{review.user_rating} Stars</div>
                <div className="review-date">{formatDate(review.created_at)}</div>
              </div>
              <div className="review-content">
                <p className="review-text">{review.user_review}</p>
              </div>
              {review.ai_summary && (
                <div className="ai-section">
                  <h4>AI Summary</h4>
                  <p>{review.ai_summary}</p>
                </div>
              )}
              {review.recommended_actions && (
                <div className="ai-section">
                  <h4>Recommended Actions</h4>
                  <div className="actions-content">{review.recommended_actions}</div>
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default AdminDashboard;
