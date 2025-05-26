# 📰 Author-Article-Magazine Project

This project models the relationships between authors, articles, and magazines using Python object-oriented programming (OOP) and raw SQL queries. It is designed to strengthen your understanding of database relationships, SQL logic, and Python class design.

---

## 🚀 Getting Started

### Option 1: Using Pipenv

```bash
pipenv install
pipenv shell
```
```bash 
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

🗄️ Database Setup
Using SQLite by default:

Define your schema in lib/db/schema.sql.

Set up the database:

```bash
python scripts/setup_db.py
```
The database file articles.db will be created with the necessary tables for authors, articles, and magazines.

🧪 Running Tests
Tests are written with pytest. To run them:

```bash
pytest
```
Make sure your database is set up before testing.

