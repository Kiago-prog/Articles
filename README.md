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
