# 🚀 Student Management System

## 📋 Project Overview
A complete full-stack web application built with FastAPI (backend) and React (frontend) for managing student records with authentication. The application features a SQLite database with 25 sample student records and a comprehensive authentication system.

### 🛠️ Technology Stack
- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Frontend**: React, JavaScript, CSS
- **Database**: SQLite with persistent storage
- **Authentication**: Session-based token authentication
- **Deployment**: Docker containers, CI/CD pipelines

## 🏗️ Application Structure
```
student-management-system/
├── backend/              # Backend application
├── frontend/             # Frontend application
├── db/                   # Database files
└── README.md             # Project documentation
```

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- Docker (optional)

### Setup Instructions

1. **Clone the repository**
   ```
   git clone <repository-url>
   cd student-management-system
   ```

2. **Backend Setup**
   - Navigate to the backend directory:
     ```
     cd backend
     ```
   - Install Python dependencies:
     ```
     pip install -r requirements.txt
     ```

3. **Frontend Setup**
   - Navigate to the frontend directory:
     ```
     cd ../frontend
     ```
   - Install Node.js dependencies:
     ```
     npm install
     ```

## 🚦 Running the Application

### Method 1: Individual Servers
- Start the backend server:
  ```
  cd backend
  python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  ```
- Start the frontend server:
  ```
  cd ../frontend
  npm start
  ```

### Method 2: Docker Compose
- Start both servers with Docker:
  ```
  docker-compose up --build
  ```

## 🌐 Accessing the Application
- Frontend: [http://localhost:3001](http://localhost:3001)
- Backend API: [http://localhost:8000](http://localhost:8000)
- API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📡 API Documentation
Refer to the API documentation for details on available endpoints and usage.

## 🎉 Features
- Full CRUD operations for user management
- Authentication system with session management
- Responsive UI built with React
- Health monitoring and error handling

## 🔒 Security
- Password hashing and session token management
- CORS protection and input sanitization

## 📞 Support
For issues or feature requests, please open an issue in the repository. 

## 🎯 License
This project is licensed under the MIT License.