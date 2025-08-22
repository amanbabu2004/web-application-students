-- User Management System Database Schema
-- SQLite Database Schema

-- Drop tables if they exist (for fresh install)
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS auth_users;
DROP TABLE IF EXISTS sessions;

-- Users table for student data
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER NOT NULL,
    occupation TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Authentication users table
CREATE TABLE auth_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Sessions table for authentication
CREATE TABLE sessions (
    token TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME NOT NULL,
    FOREIGN KEY (username) REFERENCES auth_users (username)
);

-- Create indexes for better performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_name ON users(name);
CREATE INDEX idx_sessions_username ON sessions(username);
CREATE INDEX idx_sessions_expires ON sessions(expires_at);

-- Insert default authentication users
INSERT INTO auth_users (username, password) VALUES 
    ('admin', 'admin123'),
    ('user', 'password'),
    ('demo', 'demo123'),
    ('teacher', 'teacher123'),
    ('student', 'student123');
