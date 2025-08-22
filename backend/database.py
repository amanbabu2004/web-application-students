from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from datetime import datetime, timedelta
import os

# Database configuration
DATABASE_URL = "sqlite:///./db/user_management.db"

# Create database directory if it doesn't exist
os.makedirs("./db", exist_ok=True)

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    occupation = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class AuthUser(Base):
    __tablename__ = "auth_users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Session(Base):
    __tablename__ = "sessions"
    
    token = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Initialize database with sample data
def init_database():
    create_tables()
    db = SessionLocal()
    
    try:
        # Check if auth users exist
        existing_auth = db.query(AuthUser).first()
        if not existing_auth:
            # Add default auth users
            auth_users = [
                AuthUser(username="admin", password="admin123"),
                AuthUser(username="user", password="password"),
                AuthUser(username="demo", password="demo123"),
                AuthUser(username="teacher", password="teacher123"),
                AuthUser(username="student", password="student123"),
            ]
            db.add_all(auth_users)
        
        # Check if sample users exist
        existing_users = db.query(User).first()
        if not existing_users:
            # Add sample student data
            sample_users = [
                User(id="1", name="Alice Johnson", email="alice.johnson@university.edu", age=20, occupation="Computer Science Student"),
                User(id="2", name="Bob Smith", email="bob.smith@university.edu", age=19, occupation="Engineering Student"),
                User(id="3", name="Charlie Brown", email="charlie.brown@university.edu", age=21, occupation="Mathematics Student"),
                User(id="4", name="Diana Prince", email="diana.prince@university.edu", age=22, occupation="Physics Student"),
                User(id="5", name="Edward Norton", email="edward.norton@university.edu", age=20, occupation="Chemistry Student"),
                User(id="6", name="Fiona Green", email="fiona.green@university.edu", age=19, occupation="Biology Student"),
                User(id="7", name="George Wilson", email="george.wilson@university.edu", age=23, occupation="Psychology Student"),
                User(id="8", name="Hannah Miller", email="hannah.miller@university.edu", age=21, occupation="Literature Student"),
                User(id="9", name="Ian Thompson", email="ian.thompson@university.edu", age=20, occupation="History Student"),
                User(id="10", name="Julia Davis", email="julia.davis@university.edu", age=22, occupation="Economics Student"),
                User(id="11", name="Kevin Lee", email="kevin.lee@university.edu", age=19, occupation="Business Student"),
                User(id="12", name="Laura White", email="laura.white@university.edu", age=21, occupation="Art Student"),
                User(id="13", name="Michael Chen", email="michael.chen@university.edu", age=20, occupation="Music Student"),
                User(id="14", name="Nancy Rodriguez", email="nancy.rodriguez@university.edu", age=23, occupation="Philosophy Student"),
                User(id="15", name="Oliver Kim", email="oliver.kim@university.edu", age=19, occupation="Sociology Student"),
                User(id="16", name="Priya Patel", email="priya.patel@university.edu", age=22, occupation="Political Science Student"),
                User(id="17", name="Quinn Taylor", email="quinn.taylor@university.edu", age=21, occupation="Environmental Science Student"),
                User(id="18", name="Rachel Garcia", email="rachel.garcia@university.edu", age=20, occupation="Communications Student"),
                User(id="19", name="Samuel Martinez", email="samuel.martinez@university.edu", age=24, occupation="Graduate Student"),
                User(id="20", name="Tina Anderson", email="tina.anderson@university.edu", age=19, occupation="Pre-Med Student"),
                User(id="21", name="Umar Hassan", email="umar.hassan@university.edu", age=22, occupation="Mechanical Engineering Student"),
                User(id="22", name="Victoria Wong", email="victoria.wong@university.edu", age=21, occupation="Electrical Engineering Student"),
                User(id="23", name="William Brooks", email="william.brooks@university.edu", age=23, occupation="Civil Engineering Student"),
                User(id="24", name="Ximena Lopez", email="ximena.lopez@university.edu", age=20, occupation="Biomedical Engineering Student"),
                User(id="25", name="Yuki Tanaka", email="yuki.tanaka@university.edu", age=19, occupation="Data Science Student"),
            ]
            db.add_all(sample_users)
        
        db.commit()
        print("Database initialized successfully with sample data!")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()
