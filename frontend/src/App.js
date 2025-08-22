import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import Login from './components/Login';
import UserList from './components/UserList';
import AddUser from './components/AddUser';
import EditUser from './components/EditUser';
import GetUser from './components/GetUser';
import { authService } from './services/api';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [currentUser, setCurrentUser] = useState('');
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Check if user is already logged in
    const checkAuth = async () => {
      const token = localStorage.getItem('authToken');
      const username = localStorage.getItem('username');
      
      if (token) {
        try {
          const response = await authService.verifySession(token);
          if (response.valid) {
            setIsAuthenticated(true);
            setCurrentUser(username || response.username);
          } else {
            // Invalid token, clear storage
            localStorage.removeItem('authToken');
            localStorage.removeItem('username');
          }
        } catch (error) {
          console.error('Auth verification failed:', error);
          localStorage.removeItem('authToken');
          localStorage.removeItem('username');
        }
      }
      setIsLoading(false);
    };

    checkAuth();
  }, []);

  const handleLogin = (token, username) => {
    setIsAuthenticated(true);
    setCurrentUser(username);
  };

  const handleLogout = async () => {
    const token = localStorage.getItem('authToken');
    if (token) {
      try {
        await authService.logout(token);
      } catch (error) {
        console.error('Logout error:', error);
      }
    }
    
    localStorage.removeItem('authToken');
    localStorage.removeItem('username');
    setIsAuthenticated(false);
    setCurrentUser('');
  };

  if (isLoading) {
    return <div className="loading">Loading...</div>;
  }

  if (!isAuthenticated) {
    return <Login onLogin={handleLogin} />;
  }

  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <h1>User Management System</h1>
          <div className="nav-user">
            <span>Welcome, {currentUser}!</span>
            <button onClick={handleLogout} className="logout-btn">Logout</button>
          </div>
          <div className="nav-links">
            <Link to="/">All Users</Link>
            <Link to="/add">Add User</Link>
            <Link to="/get">Get Single User</Link>
          </div>
        </nav>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<UserList />} />
            <Route path="/add" element={<AddUser />} />
            <Route path="/edit/:id" element={<EditUser />} />
            <Route path="/get" element={<GetUser />} />
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
