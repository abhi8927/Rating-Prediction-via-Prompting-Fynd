/**
 * API client for communicating with the backend.
 * Handles all HTTP requests to the Flask API.
 */

import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const submitReview = async (userRating, userReview) => {
  try {
    const response = await apiClient.post('/api/reviews', {
      user_rating: userRating,
      user_review: userReview,
    });
    return { success: true, data: response.data };
  } catch (error) {
    if (error.response) {
      return { success: false, error: error.response.data.message || 'Failed to submit review' };
    }
    return { success: false, error: 'Network error. Please check your connection.' };
  }
};

export const getAllReviews = async () => {
  try {
    const response = await apiClient.get('/api/admin/reviews');
    return { success: true, data: response.data.reviews || [] };
  } catch (error) {
    if (error.response) {
      return { success: false, error: error.response.data.message || 'Failed to fetch reviews' };
    }
    return { success: false, error: 'Network error. Please check your connection.' };
  }
};

export const getStats = async () => {
  try {
    const response = await apiClient.get('/api/admin/stats');
    return { success: true, data: response.data };
  } catch (error) {
    if (error.response) {
      return { success: false, error: error.response.data.message || 'Failed to fetch stats' };
    }
    return { success: false, error: 'Network error. Please check your connection.' };
  }
};

export const healthCheck = async () => {
  try {
    const response = await apiClient.get('/api/health');
    return { success: true, data: response.data };
  } catch (error) {
    return { success: false, error: 'API is not reachable' };
  }
};
