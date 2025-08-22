import React, { useState } from 'react';
import { userService } from '../services/api';

const GetUser = () => {
  const [userId, setUserId] = useState('');
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState('');

  const handleSearch = async (e) => {
    e.preventDefault();
    
    if (!userId.trim()) {
      setMessage('Please enter a user ID');
      setMessageType('error');
      return;
    }

    try {
      setLoading(true);
      setMessage('');
      setUser(null);
      
      const userData = await userService.getUserById(userId.trim());
      setUser(userData);
      setMessage('');
    } catch (error) {
      if (error.response && error.response.status === 404) {
        setMessage('User not found');
      } else {
        setMessage('Failed to fetch user details');
      }
      setMessageType('error');
      setUser(null);
      console.error('Error fetching user:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setUserId('');
    setUser(null);
    setMessage('');
  };

  return (
    <div className="container">
      <h2>Get Single User</h2>
      
      <form onSubmit={handleSearch} className="search-form">
        <div className="form-group">
          <label htmlFor="userId">User ID:</label>
          <input
            type="text"
            id="userId"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            placeholder="Enter user ID (e.g., 1, 2, 3...)"
            required
          />
        </div>
        <div className="actions">
          <button 
            type="submit" 
            className="btn btn-primary"
            disabled={loading}
          >
            {loading ? 'Searching...' : 'Search User'}
          </button>
          <button 
            type="button" 
            onClick={handleClear}
            className="btn btn-secondary"
          >
            Clear
          </button>
        </div>
      </form>

      {message && (
        <div className={`message ${messageType}`}>
          {message}
        </div>
      )}

      {user && (
        <div className="user-card">
          <h3>{user.name}</h3>
          <p><strong>ID:</strong> {user.id}</p>
          <p><strong>Email:</strong> {user.email}</p>
          <p><strong>Age:</strong> {user.age}</p>
          <p><strong>Occupation:</strong> {user.occupation}</p>
        </div>
      )}
    </div>
  );
};

export default GetUser;
