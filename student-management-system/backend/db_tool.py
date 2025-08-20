import os
import sqlite3
import csv
from datetime import datetime

DATABASE_PATH = 'db/user_management.db'

def connect_db():
    return sqlite3.connect(DATABASE_PATH)

def get_db_stats():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM auth_users")
    auth_user_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM sessions")
    session_count = cursor.fetchone()[0]
    conn.close()
    return {
        "user_count": user_count,
        "auth_user_count": auth_user_count,
        "session_count": session_count,
        "timestamp": datetime.now().isoformat()
    }

def search_user(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def list_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def backup_database():
    conn = connect_db()
    with open('db_backup.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    conn.close()

def reset_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS auth_users")
    cursor.execute("DROP TABLE IF EXISTS sessions")
    cursor.executescript(open('db/schema.sql').read())
    cursor.executescript(open('db/sample_data.sql').read())
    conn.commit()
    conn.close()

def export_to_csv():
    users = list_users()
    with open('users.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Name', 'Email', 'Age', 'Occupation', 'Created At', 'Updated At'])
        writer.writerows(users)