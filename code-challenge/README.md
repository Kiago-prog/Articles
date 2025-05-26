# 📰 Articles & Magazines SQL Challenge

A Python project using Object-Oriented Programming and raw SQL to model the relationships between **Authors**, **Articles**, and **Magazines**. Designed for practicing OOP principles, database design, and SQL query writing.

---

## 📁 Project Structure

code-challenge/
├── lib/
│ ├── models/
│ │ ├── author.py
│ │ ├── article.py
│ │ └── magazine.py
│ ├── db/
│ │ ├── connection.py
│ │ ├── schema.sql
│ │ └── seed.py
│ ├── debug.py
│ └── init.py
├── tests/
│ ├── test_author.py
│ ├── test_article.py
│ └── test_magazine.py
├── scripts/
│ ├── setup_db.py
│ └── run_queries.py
├── .gitignore
├── Pipfile / requirements.txt
└── README.md

yaml
Copy
Edit

---

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
Tests are written using pytest.

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

List all articles in the magazine

List contributors

Show titles of all articles

List contributing authors (with more than 2 articles)

✅ Article
Create/find articles

Track relationships with authors and magazines

💡 Advanced Queries
Magazines with articles by at least 2 different authors

Author with the most articles

Count articles per magazine

Top publishing magazine

💾 Transaction Handling
Includes robust support for database transactions with rollback on failure:

python
Copy
Edit
try:
    conn.execute("BEGIN TRANSACTION")
    # Do inserts
    conn.execute("COMMIT")
except:
    conn.execute("ROLLBACK")
🧼 Code Quality
Follows OOP principles (encapsulation, reuse, DRY)

Uses raw SQL for full transparency and learning

Organized, modular Python files

Includes comprehensive tests for models and relationships

🔐 Security
All SQL queries use parameterized queries (?) to prevent SQL injection.

✅ Commit Best Practices
Frequent, atomic commits

Clear messages using:

markdown
Copy
Edit
[Feature/Fix/Refactor]: Brief description

- More details if needed
Example:

Feature: Add Author.articles() method

Fix: Correct JOIN query in Magazine.contributors()

✨ Bonus Ideas
CLI interface for user interaction

PostgreSQL support

Performance optimization with indexes

📌 License
MIT License – open for educational use.

👨‍💻 Author
Built as part of a Python OOP & SQL project challenge.

vbnet
Copy
Edit

Let me know if you want help editing your actual project files or if you'd like to automate seeding and setup with scripts.