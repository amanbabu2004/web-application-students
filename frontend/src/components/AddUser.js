import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { userService } from '../services/api';

const AddUser = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState('');
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    age: '',
    occupation: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Basic validation
    if (!formData.name || !formData.email || !formData.age || !formData.occupation) {
      setMessage('Please fill in all fields');
      setMessageType('error');
      return;
    }

    if (isNaN(formData.age) || formData.age <= 0) {
      setMessage('Please enter a valid age');
      setMessageType('error');
      return;
    }

    try {
      setLoading(true);
      setMessage('');
      
      const userData = {
        ...formData,
        age: parseInt(formData.age)
      };

      await userService.createUser(userData);
      setMessage('User created successfully!');
      setMessageType('success');
      
      // Reset form
      setFormData({
        name: '',
        email: '',
        age: '',
        occupation: ''
      });

      // Redirect to user list after 2 seconds
      setTimeout(() => {
        navigate('/');
      }, 2000);

    } catch (error) {
      setMessage('Failed to create user. Please try again.');
      setMessageType('error');
      console.error('Error creating user:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2>Add New User</h2>
      
      {message && (
        <div className={`message ${messageType}`}>
          {message}
        </div>
      )}

      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Enter full name"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Enter email address"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="age">Age:</label>
          <input
            type="number"
            id="age"
            name="age"
            value={formData.age}
            onChange={handleChange}
            placeholder="Enter age"
            min="1"
            max="120"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="occupation">Occupation:</label>
          <input
            type="text"
            id="occupation"
            name="occupation"
            value={formData.occupation}
            onChange={handleChange}
            placeholder="Enter occupation"
            required
          />
        </div>

        <div className="actions">
          <button 
            type="submit" 
            className="btn btn-success"
            disabled={loading}
          >
            {loading ? 'Creating...' : 'Create User'}
          </button>
          <button 
            type="button" 
            onClick={() => navigate('/')}
            className="btn btn-secondary"
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default AddUser;
