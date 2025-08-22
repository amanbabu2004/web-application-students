import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { userService } from '../services/api';

const EditUser = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [updating, setUpdating] = useState(false);
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState('');
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    age: '',
    occupation: ''
  });

  useEffect(() => {
    fetchUser();
  }, [id]);

  const fetchUser = async () => {
    try {
      setLoading(true);
      const user = await userService.getUserById(id);
      setFormData({
        name: user.name,
        email: user.email,
        age: user.age.toString(),
        occupation: user.occupation
      });
      setMessage('');
    } catch (error) {
      setMessage('Failed to fetch user details');
      setMessageType('error');
      console.error('Error fetching user:', error);
    } finally {
      setLoading(false);
    }
  };

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
      setUpdating(true);
      setMessage('');
      
      const userData = {
        ...formData,
        age: parseInt(formData.age)
      };

      await userService.updateUser(id, userData);
      setMessage('User updated successfully!');
      setMessageType('success');

      // Redirect to user list after 2 seconds
      setTimeout(() => {
        navigate('/');
      }, 2000);

    } catch (error) {
      setMessage('Failed to update user. Please try again.');
      setMessageType('error');
      console.error('Error updating user:', error);
    } finally {
      setUpdating(false);
    }
  };

  if (loading) {
    return (
      <div className="container">
        <div className="loading">Loading user details...</div>
      </div>
    );
  }

  return (
    <div className="container">
      <h2>Edit User</h2>
      
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
            disabled={updating}
          >
            {updating ? 'Updating...' : 'Update User'}
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

export default EditUser;
