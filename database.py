import sqlite3
from datetime import datetime

DB_NAME = "scraper.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            author TEXT NOT NULL,
            tags TEXT,
            scraped_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_quote(text, author, tags):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM quotes WHERE text=?", (text,))
    if not cursor.fetchone():
        cursor.execute('''
            INSERT INTO quotes (text, author, tags, scraped_at)
            VALUES (?, ?, ?, ?)
        ''', (text, author, tags, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
    conn.close()

def get_all_quotes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quotes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def export_to_csv():
    import csv
    quotes = get_all_quotes()
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Text', 'Author', 'Tags', 'Scraped At'])
        writer.writerows(quotes)
    return len(quotes)
