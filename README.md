# Full-Stack User Management System

A complete full-stack web application built with FastAPI (Python) backend and React frontend for managing users with full CRUD functionality.

## 🏗️ Architecture

- **Backend**: FastAPI (Python) - REST API with in-memory database
- **Frontend**: React with React Router - Modern web interface
- **API Communication**: Axios for HTTP requests
- **Styling**: Custom CSS with responsive design

## ✨ Features

### Backend (FastAPI)
- ✅ **POST /users/** - Create a new user
- ✅ **GET /users/** - Get all users  
- ✅ **GET /users/{id}** - Get user by ID
- ✅ **PUT /users/{id}** - Update user
- ✅ **DELETE /users/{id}** - Delete user
- ✅ **CORS enabled** for React frontend
- ✅ **In-memory database** (dictionary) with sample data
- ✅ **Data validation** with Pydantic models

### Frontend (React)
- ✅ **User List Page** - View all users with edit/delete actions
- ✅ **Add User Page** - Form to create new users
- ✅ **Edit User Page** - Form to update existing users
- ✅ **Delete Functionality** - Remove users with confirmation
- ✅ **Get Single User** - Search for user by ID (bonus feature)
- ✅ **React Router** for navigation
- ✅ **State Management** with useState and useEffect
- ✅ **Success/Error Messages** for all operations
- ✅ **Responsive Design** with clean styling

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### 1. Backend Setup (FastAPI)

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
```

The backend will be available at: `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### 2. Frontend Setup (React)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

The frontend will be available at: `http://localhost:3000`

## 📊 User Data Model

Each user has the following fields:
- **id**: Unique identifier (string, auto-generated UUID)
- **name**: Full name (string, required)
- **email**: Email address (string, required)
- **age**: Age in years (integer, required)
- **occupation**: Job title/profession (string, required)

## 🛠️ API Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/users/` | Get all users | None |
| GET | `/users/{id}` | Get user by ID | None |
| POST | `/users/` | Create new user | `{name, email, age, occupation}` |
| PUT | `/users/{id}` | Update user | `{name, email, age, occupation}` (partial updates supported) |
| DELETE | `/users/{id}` | Delete user | None |

## 🎨 Frontend Pages

1. **Home (/)** - User List with all users in a table
2. **Add User (/add)** - Form to create new users
3. **Edit User (/edit/:id)** - Form to update existing users  
4. **Get User (/get)** - Search for a single user by ID

## 🔧 Development

### Backend Development
- FastAPI automatically reloads on file changes with `--reload` flag
- Access interactive API docs at `http://localhost:8000/docs`
- Logs are displayed in the terminal

### Frontend Development  
- React dev server automatically reloads on file changes
- Components are in `src/components/`
- API service functions are in `src/services/api.js`
- Styling is in `src/App.css`

## 📱 Responsive Design

The application is fully responsive and works well on:
- Desktop computers
- Tablets
- Mobile phones

## 🐛 Error Handling

- **Backend**: Proper HTTP status codes and error messages
- **Frontend**: User-friendly error messages and loading states
- **Validation**: Client-side and server-side input validation

## 🔄 Sample Data

The application comes pre-loaded with 3 sample users:
1. John Doe - Software Engineer
2. Jane Smith - Designer  
3. Bob Johnson - Product Manager

## 📝 Next Steps

To extend this application, you could:
- Add user authentication and authorization
- Implement a real database (PostgreSQL, MongoDB)
- Add user profile pictures
- Implement search and filtering
- Add pagination for large user lists
- Add unit and integration tests
- Deploy to cloud platforms (Heroku, Vercel, AWS)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
