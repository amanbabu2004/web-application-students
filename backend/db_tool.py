#!/usr/bin/env python3
"""
Database Query Tool for User Management System
Provides command-line interface to query and manage the SQLite database
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import sqlite3
from database import SessionLocal, User as DBUser, AuthUser as DBAuthUser, Session as DBSession
from datetime import datetime
import argparse

class DatabaseTool:
    def __init__(self):
        self.db_path = "./db/user_management.db"
        
    def execute_raw_sql(self, query):
        """Execute raw SQL query"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                # Get column names
                columns = [description[0] for description in cursor.description]
                
                print(f"\n📊 Query Results ({len(results)} rows):")
                print("=" * 80)
                
                if results:
                    # Print header
                    print(" | ".join(f"{col:15}" for col in columns))
                    print("-" * 80)
                    
                    # Print data
                    for row in results:
                        print(" | ".join(f"{str(val):15}" for val in row))
                else:
                    print("No results found.")
            else:
                conn.commit()
                print(f"✅ Query executed successfully. Rows affected: {cursor.rowcount}")
                
            conn.close()
            
        except Exception as e:
            print(f"❌ Error executing query: {e}")
    
    def show_all_users(self):
        """Show all users in a formatted table"""
        query = """
        SELECT id, name, email, age, occupation, created_at 
        FROM users 
        ORDER BY name
        """
        self.execute_raw_sql(query)
    
    def show_user_stats(self):
        """Show user statistics"""
        queries = [
            ("Total Users", "SELECT COUNT(*) as count FROM users"),
            ("Average Age", "SELECT ROUND(AVG(age), 2) as avg_age FROM users"),
            ("Youngest Student", "SELECT MIN(age) as min_age FROM users"),
            ("Oldest Student", "SELECT MAX(age) as max_age FROM users"),
            ("Most Common Age", """
                SELECT age, COUNT(*) as count 
                FROM users 
                GROUP BY age 
                ORDER BY count DESC, age 
                LIMIT 1
            """)
        ]
        
        print("\n📈 User Statistics:")
        print("=" * 50)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for title, query in queries:
            cursor.execute(query)
            result = cursor.fetchone()
            print(f"{title}: {result[0]}")
        
        conn.close()
    
    def show_occupation_breakdown(self):
        """Show breakdown by occupation"""
        query = """
        SELECT 
            occupation,
            COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM users), 2) as percentage
        FROM users 
        GROUP BY occupation 
        ORDER BY count DESC
        """
        print("\n🎓 Students by Occupation:")
        print("=" * 60)
        self.execute_raw_sql(query)
    
    def search_users(self, search_term):
        """Search users by name or email"""
        query = f"""
        SELECT id, name, email, age, occupation 
        FROM users 
        WHERE name LIKE '%{search_term}%' OR email LIKE '%{search_term}%'
        ORDER BY name
        """
        print(f"\n🔍 Search Results for '{search_term}':")
        self.execute_raw_sql(query)
    
    def show_auth_users(self):
        """Show authentication users"""
        query = "SELECT username, created_at FROM auth_users ORDER BY username"
        print("\n🔐 Authentication Users:")
        self.execute_raw_sql(query)
    
    def show_active_sessions(self):
        """Show active sessions"""
        query = """
        SELECT username, token, created_at, expires_at 
        FROM sessions 
        WHERE expires_at > datetime('now')
        ORDER BY created_at DESC
        """
        print("\n🔓 Active Sessions:")
        self.execute_raw_sql(query)
    
    def cleanup_expired_sessions(self):
        """Clean up expired sessions"""
        query = "DELETE FROM sessions WHERE expires_at <= datetime('now')"
        print("\n🧹 Cleaning up expired sessions...")
        self.execute_raw_sql(query)
    
    def backup_database(self, backup_path=None):
        """Create a backup of the database"""
        if not backup_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"./db/backup_user_management_{timestamp}.db"
        
        try:
            import shutil
            shutil.copy2(self.db_path, backup_path)
            print(f"✅ Database backed up to: {backup_path}")
        except Exception as e:
            print(f"❌ Error creating backup: {e}")

def main():
    parser = argparse.ArgumentParser(description="User Management Database Tool")
    parser.add_argument("--sql", help="Execute raw SQL query")
    parser.add_argument("--users", action="store_true", help="Show all users")
    parser.add_argument("--stats", action="store_true", help="Show user statistics")
    parser.add_argument("--occupations", action="store_true", help="Show occupation breakdown")
    parser.add_argument("--search", help="Search users by name or email")
    parser.add_argument("--auth", action="store_true", help="Show auth users")
    parser.add_argument("--sessions", action="store_true", help="Show active sessions")
    parser.add_argument("--cleanup", action="store_true", help="Clean up expired sessions")
    parser.add_argument("--backup", nargs="?", const="", help="Backup database")
    
    args = parser.parse_args()
    
    db_tool = DatabaseTool()
    
    print("🗄️  User Management Database Tool")
    print("=" * 50)
    
    if args.sql:
        db_tool.execute_raw_sql(args.sql)
    elif args.users:
        db_tool.show_all_users()
    elif args.stats:
        db_tool.show_user_stats()
    elif args.occupations:
        db_tool.show_occupation_breakdown()
    elif args.search:
        db_tool.search_users(args.search)
    elif args.auth:
        db_tool.show_auth_users()
    elif args.sessions:
        db_tool.show_active_sessions()
    elif args.cleanup:
        db_tool.cleanup_expired_sessions()
    elif args.backup is not None:
        backup_path = args.backup if args.backup else None
        db_tool.backup_database(backup_path)
    else:
        # Interactive mode
        print("\n🔧 Interactive Mode - Choose an option:")
        print("1. Show all users")
        print("2. Show user statistics")
        print("3. Show occupation breakdown")
        print("4. Search users")
        print("5. Show auth users")
        print("6. Show active sessions")
        print("7. Execute custom SQL")
        print("8. Backup database")
        print("0. Exit")
        
        while True:
            choice = input("\nEnter your choice (0-8): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                db_tool.show_all_users()
            elif choice == "2":
                db_tool.show_user_stats()
            elif choice == "3":
                db_tool.show_occupation_breakdown()
            elif choice == "4":
                search_term = input("Enter search term: ").strip()
                db_tool.search_users(search_term)
            elif choice == "5":
                db_tool.show_auth_users()
            elif choice == "6":
                db_tool.show_active_sessions()
            elif choice == "7":
                sql_query = input("Enter SQL query: ").strip()
                db_tool.execute_raw_sql(sql_query)
            elif choice == "8":
                db_tool.backup_database()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
