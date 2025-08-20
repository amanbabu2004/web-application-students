from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from db_tool import create_sample_data
from routers import user_router, auth_router

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router)
app.include_router(auth_router)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Create sample data
create_sample_data()

@app.get("/")
def read_root():
    return {"message": "User Management API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}