# 📰 Articles & Magazines SQL Challenge

A Python project using Object-Oriented Programming and raw SQL to model the relationships between **Authors**, **Articles**, and **Magazines**. Designed for practicing OOP principles, database design, and SQL query writing.



## 🛠️ Setup Instructions

### 📦 Option 1: Using Pipenv (Recommended)
```bash
pipenv install
pipenv shell
📦 Option 2: Using venv
bash
Copy
Edit
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
🗃️ Database Setup
✅ SQLite (default)
Edit lib/db/connection.py:

python
Copy
Edit
import sqlite3

def get_connection():
    conn = sqlite3.connect('articles.db')
    conn.row_factory = sqlite3.Row
    return conn
To initialize the schema:

bash
Copy
Edit
python scripts/setup_db.py
🧪 Running Tests
Tests are written using pytest

bash
Copy
Edit
pytest
📚 Features
✅ Author
Create/find authors

List all articles by the author

List all magazines the author has written for

Add a new article

List topic areas (categories) contributed to

✅ Magazine
Create/find magazines

List all articles in the magazine.
