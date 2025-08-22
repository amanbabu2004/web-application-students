# Backend - FastAPI User Management API

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Running the Server

```bash
# Start the development server with auto-reload
uvicorn main:app --reload

# Or run directly with Python
python main.py
```

The API will be available at:
- **Server**: `http://localhost:8000`
- **Interactive Docs**: `http://localhost:8000/docs`
- **Alternative Docs**: `http://localhost:8000/redoc`

## 📋 Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation using Python type annotations

## 🏗️ Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 📊 Data Models

### UserCreate (Request Model)
```python
{
  "name": "string",
  "email": "string", 
  "age": "integer",
  "occupation": "string"
}
```

### UserUpdate (Request Model)
```python
{
  "name": "string (optional)",
  "email": "string (optional)",
  "age": "integer (optional)", 
  "occupation": "string (optional)"
}
```

### User (Response Model)
```python
{
  "id": "string (UUID)",
  "name": "string",
  "email": "string",
  "age": "integer",
  "occupation": "string"
}
```

## 🛠️ API Endpoints

### Create User
- **POST** `/users/`
- **Body**: UserCreate model
- **Response**: User model
- **Status**: 201 Created

### Get All Users  
- **GET** `/users/`
- **Response**: List of User models
- **Status**: 200 OK

### Get User by ID
- **GET** `/users/{user_id}`
- **Response**: User model
- **Status**: 200 OK / 404 Not Found

### Update User
- **PUT** `/users/{user_id}`
- **Body**: UserUpdate model (partial updates supported)
- **Response**: User model  
- **Status**: 200 OK / 404 Not Found

### Delete User
- **DELETE** `/users/{user_id}`
- **Response**: Success message
- **Status**: 200 OK / 404 Not Found

## 🔧 Configuration

### CORS Settings
The API is configured to allow requests from:
- `http://localhost:3000` (React development server)

To modify CORS settings, update the `CORSMiddleware` configuration in `main.py`.

### Sample Data
The application initializes with 3 sample users. To modify or disable this, edit the `initialize_sample_data()` function.

## 🐛 Error Handling

The API returns appropriate HTTP status codes:
- **200**: Success
- **201**: Created  
- **404**: User not found
- **422**: Validation error (invalid request data)

Error responses include descriptive messages:
```json
{
  "detail": "User not found"
}
```

## 📝 Development Notes

- Users are stored in an in-memory dictionary (`users_db`)
- User IDs are automatically generated UUIDs
- All data is lost when the server restarts
- CORS is enabled for frontend integration
- Request/response validation is handled by Pydantic models

## 🔄 Extending the API

To add new features:

1. **Add new endpoints**: Define new route functions
2. **Modify data models**: Update Pydantic models
3. **Add validation**: Use Pydantic validators
4. **Database integration**: Replace in-memory storage with a real database
5. **Authentication**: Add JWT or session-based auth

## 🧪 Testing

Test the API using:
- **Interactive Docs**: `http://localhost:8000/docs`
- **curl**: Command-line HTTP client
- **Postman**: API testing tool
- **Python requests**: HTTP library

Example curl command:
```bash
# Create a new user
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","age":25,"occupation":"Tester"}'
```
