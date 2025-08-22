from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import uuid
import hashlib
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database import get_db, init_database, User as DBUser, AuthUser as DBAuthUser, Session as DBSession
import os

# For serverless deployment (AWS Lambda, Vercel)
try:
    from mangum import Mangum
except ImportError:
    Mangum = None

app = FastAPI(title="User Management API", version="1.0.0")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    occupation: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    occupation: Optional[str] = None

class User(BaseModel):
    id: str
    name: str
    email: str
    age: int
    occupation: str

# Authentication models
class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    message: str
    token: Optional[str] = None

# In-memory database (dictionary) - REMOVED, using SQLite now
# users_db: Dict[str, User] = {}

# Simple authentication storage - MOVED to database
# auth_users = {
#     "admin": "admin123",  # username: password
#     "user": "password",
#     "demo": "demo123"
# }

# Simple session storage - MOVED to database
# active_sessions: Dict[str, str] = {}  # token: username

# Initialize database on startup
init_database()

@app.get("/")
async def root():
    return {"message": "User Management API is running with SQLite Database!"}

# Authentication endpoints
@app.post("/auth/login", response_model=LoginResponse)
async def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate user and return session token"""
    username = login_request.username
    password = login_request.password
    
    # Check credentials in database
    auth_user = db.query(DBAuthUser).filter(DBAuthUser.username == username).first()
    if auth_user and auth_user.password == password:
        # Create simple session token
        token = hashlib.md5(f"{username}_{datetime.now()}".encode()).hexdigest()
        
        # Store session in database
        expires_at = datetime.now() + timedelta(hours=24)
        db_session = DBSession(token=token, username=username, expires_at=expires_at)
        db.add(db_session)
        db.commit()
        
        return LoginResponse(
            success=True,
            message="Login successful",
            token=token
        )
    else:
        return LoginResponse(
            success=False,
            message="Invalid username or password"
        )

@app.post("/auth/logout")
async def logout(token: str, db: Session = Depends(get_db)):
    """Logout user and invalidate session token"""
    db_session = db.query(DBSession).filter(DBSession.token == token).first()
    if db_session:
        db.delete(db_session)
        db.commit()
        return {"message": "Logged out successfully"}
    return {"message": "Invalid session"}

@app.get("/auth/verify")
async def verify_session(token: str, db: Session = Depends(get_db)):
    """Verify if session token is valid"""
    db_session = db.query(DBSession).filter(
        DBSession.token == token,
        DBSession.expires_at > datetime.now()
    ).first()
    if db_session:
        return {"valid": True, "username": db_session.username}
    return {"valid": False}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    user_id = str(uuid.uuid4())
    
    # Create database user
    db_user = DBUser(
        id=user_id,
        name=user.name,
        email=user.email,
        age=user.age,
        occupation=user.occupation
    )
    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        # Return Pydantic User model
        return User(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            age=db_user.age,
            occupation=db_user.occupation
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating user: {str(e)}")

@app.get("/users/", response_model=List[User])
async def get_all_users(db: Session = Depends(get_db)):
    """Get all users"""
    db_users = db.query(DBUser).all()
    return [User(
        id=user.id,
        name=user.name,
        email=user.email,
        age=user.age,
        occupation=user.occupation
    ) for user in db_users]

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str, db: Session = Depends(get_db)):
    """Get user by ID"""
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return User(
        id=db_user.id,
        name=db_user.name,
        email=db_user.email,
        age=db_user.age,
        occupation=db_user.occupation
    )

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    """Update user by ID"""
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update only provided fields
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    try:
        db.commit()
        db.refresh(db_user)
        
        return User(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            age=db_user.age,
            occupation=db_user.occupation
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating user: {str(e)}")

@app.delete("/users/{user_id}")
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    """Delete user by ID"""
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    try:
        user_name = db_user.name
        db.delete(db_user)
        db.commit()
        return {"message": f"User {user_name} deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting user: {str(e)}")

# Health check endpoint for deployment
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# For serverless deployment (AWS Lambda, Vercel)
if Mangum:
    handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
