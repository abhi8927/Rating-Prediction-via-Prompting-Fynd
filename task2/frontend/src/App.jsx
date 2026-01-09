/**
 * Main App Component
 * Sets up routing between User and Admin dashboards.
 */

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import UserDashboard from './components/UserDashboard';
import AdminDashboard from './components/AdminDashboard';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <nav className="app-nav">
          <Link to="/" className="nav-link">User Dashboard</Link>
          <Link to="/admin" className="nav-link">Admin Dashboard</Link>
        </nav>
        <Routes>
          <Route path="/" element={<UserDashboard />} />
          <Route path="/admin" element={<AdminDashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
