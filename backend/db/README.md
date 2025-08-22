# Database Management Scripts

This folder contains scripts for managing the SQLite database.

## Files

### `schema.sql`
Database schema definition with all table structures.

### `sample_data.sql`
Sample data insertion script with 25 student records and 5 authentication users.

### `db_tool.py`
Comprehensive database query and management tool.

## Usage

### Basic Database Operations

```bash
# Initialize database with sample data
python init_db.py

# Show all users
python db_tool.py --users

# Show user statistics
python db_tool.py --stats

# Show occupation breakdown
python db_tool.py --occupations

# Search users
python db_tool.py --search "Alice"

# Show authentication users
python db_tool.py --auth

# Show active sessions
python db_tool.py --sessions

# Clean up expired sessions
python db_tool.py --cleanup

# Execute custom SQL
python db_tool.py --sql "SELECT * FROM users WHERE age > 25"

# Backup database
python db_tool.py --backup

# Interactive mode
python db_tool.py
```

### Advanced Queries

```bash
# Find users by age range
python db_tool.py --sql "SELECT name, age FROM users WHERE age BETWEEN 20 AND 25 ORDER BY age"

# Count users by occupation
python db_tool.py --sql "SELECT occupation, COUNT(*) FROM users GROUP BY occupation"

# Find youngest and oldest students
python db_tool.py --sql "SELECT name, age FROM users WHERE age = (SELECT MIN(age) FROM users) OR age = (SELECT MAX(age) FROM users)"

# Recent user registrations
python db_tool.py --sql "SELECT name, email, created_at FROM users ORDER BY created_at DESC LIMIT 10"
```

## Database Schema

### Users Table
- `id`: Primary key (INTEGER)
- `name`: Full name (TEXT)
- `email`: Email address (TEXT, UNIQUE)
- `age`: Age (INTEGER)
- `occupation`: Student occupation/field (TEXT)
- `created_at`: Timestamp (DATETIME)

### Auth_Users Table
- `id`: Primary key (INTEGER)
- `username`: Login username (TEXT, UNIQUE)
- `password_hash`: Hashed password (TEXT)
- `created_at`: Timestamp (DATETIME)

### Sessions Table
- `id`: Primary key (INTEGER)
- `username`: Associated username (TEXT)
- `token`: Session token (TEXT, UNIQUE)
- `created_at`: Creation timestamp (DATETIME)
- `expires_at`: Expiration timestamp (DATETIME)

## Demo Credentials

For testing the authentication system:

| Username | Password |
|----------|----------|
| admin    | admin123 |
| student  | student123 |
| teacher  | teacher123 |
| guest    | guest123 |
| demo     | demo123 |

## Sample Data Overview

The database contains 25 diverse student records with:
- **Ages**: 18-28 years
- **Occupations**: 
  - Computer Science (6 students)
  - Engineering (4 students)
  - Business Administration (3 students)
  - Psychology, Biology, Mathematics (2 each)
  - Art, Physics, Literature, Economics, Medicine, History (1 each)
- **International Names**: Representing diverse backgrounds
- **Realistic Email Addresses**: Following common patterns

## Backup Strategy

Regular backups are recommended:

```bash
# Create timestamped backup
python db_tool.py --backup

# Create named backup
python db_tool.py --backup ./backups/before_migration.db
```

## VS Code Database Connection

### Connection Details
- **Database Type**: SQLite
- **File Path**: `C:\Users\Yasmi\OneDrive\Desktop\amanwork\backend\db\user_management.db`
- **Connection URL**: `sqlite:///C:/Users/Yasmi/OneDrive/Desktop/amanwork/backend/db/user_management.db`
- **Username**: Not required (SQLite is file-based)
- **Password**: Not required (SQLite is file-based)

### Recommended Extensions
1. **SQLite Viewer** (`qwtel.sqlite-viewer`) - Best for quick viewing
2. **SQLTools** (`mtxr.sqltools`) + **SQLTools SQLite** (`mtxr.sqltools-driver-sqlite`) - Best for queries
3. **SQLite** (`alexcvzz.vscode-sqlite`) - Alternative viewer

### Setup Instructions
1. Install any of the recommended extensions
2. Open Command Palette (`Ctrl+Shift+P`)
3. Type "SQLite: Open Database" or "SQLTools: Add New Connection"
4. Browse to the database file path above

## Troubleshooting

### Database Locked
If you encounter "database is locked" errors:
1. Ensure no other processes are using the database
2. Close any open database connections
3. Restart the FastAPI server

### Missing Tables
If tables are missing:
```bash
python init_db.py
```

### Corrupt Data
Restore from backup:
```bash
cp ./db/backup_user_management_TIMESTAMP.db ./db/user_management.db
```
