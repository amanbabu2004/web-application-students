#!/usr/bin/env python3
"""
Database Setup Script for User Management System
This script initializes the SQLite database with schema and sample data
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import init_database, SessionLocal, User as DBUser, AuthUser as DBAuthUser
import sqlite3

def create_database_with_sql():
    """Create database using raw SQL files"""
    db_path = "./db/user_management.db"
    
    # Ensure db directory exists
    os.makedirs("./db", exist_ok=True)
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Read and execute schema
        with open('./db/schema.sql', 'r') as f:
            schema_sql = f.read()
            cursor.executescript(schema_sql)
        
        # Read and execute sample data
        with open('./db/sample_data.sql', 'r') as f:
            data_sql = f.read()
            cursor.executescript(data_sql)
        
        conn.commit()
        print("✅ Database created successfully with SQL scripts!")
        
        # Show stats
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM auth_users")
        auth_count = cursor.fetchone()[0]
        
        print(f"📊 Database Statistics:")
        print(f"   • Users: {user_count}")
        print(f"   • Auth Users: {auth_count}")
        print(f"   • Database Location: {os.path.abspath(db_path)}")
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        conn.rollback()
    finally:
        conn.close()

def init_with_sqlalchemy():
    """Initialize database using SQLAlchemy ORM"""
    try:
        print("🔧 Initializing database with SQLAlchemy...")
        init_database()
        
        # Get stats
        db = SessionLocal()
        user_count = db.query(DBUser).count()
        auth_count = db.query(DBAuthUser).count()
        db.close()
        
        print(f"✅ Database initialized successfully!")
        print(f"📊 Database Statistics:")
        print(f"   • Users: {user_count}")
        print(f"   • Auth Users: {auth_count}")
        print(f"   • Database Location: {os.path.abspath('./db/user_management.db')}")
        
    except Exception as e:
        print(f"❌ Error initializing database: {e}")

def view_database_contents():
    """View current database contents"""
    try:
        db = SessionLocal()
        
        print("\n👥 Current Users in Database:")
        print("-" * 80)
        users = db.query(DBUser).all()
        for user in users:
            print(f"ID: {user.id} | Name: {user.name} | Email: {user.email} | Age: {user.age} | Occupation: {user.occupation}")
        
        print(f"\n🔐 Auth Users:")
        print("-" * 40)
        auth_users = db.query(DBAuthUser).all()
        for auth in auth_users:
            print(f"Username: {auth.username} | Password: {auth.password}")
        
        db.close()
        
    except Exception as e:
        print(f"❌ Error viewing database: {e}")

if __name__ == "__main__":
    print("🗄️  User Management System Database Setup")
    print("=" * 50)
    
    # Method 1: Using SQLAlchemy ORM (Recommended)
    init_with_sqlalchemy()
    
    # View contents
    view_database_contents()
    
    print("\n🎉 Database setup complete!")
    print("You can now start the FastAPI server with: python main.py")
