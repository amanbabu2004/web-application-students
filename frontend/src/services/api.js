import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const userService = {
  // Get all users
  getAllUsers: async () => {
    const response = await api.get('/users/');
    return response.data;
  },

  // Get user by ID
  getUserById: async (id) => {
    const response = await api.get(`/users/${id}`);
    return response.data;
  },

  // Create new user
  createUser: async (userData) => {
    const response = await api.post('/users/', userData);
    return response.data;
  },

  // Update user
  updateUser: async (id, userData) => {
    const response = await api.put(`/users/${id}`, userData);
    return response.data;
  },

  // Delete user
  deleteUser: async (id) => {
    const response = await api.delete(`/users/${id}`);
    return response.data;
  },
};

// Authentication service
export const authService = {
  // Login
  login: async (username, password) => {
    const response = await api.post('/auth/login', { username, password });
    return response.data;
  },

  // Logout
  logout: async (token) => {
    const response = await api.post('/auth/logout', null, {
      params: { token }
    });
    return response.data;
  },

  // Verify session
  verifySession: async (token) => {
    const response = await api.get('/auth/verify', {
      params: { token }
    });
    return response.data;
  },
};

export default userService;
