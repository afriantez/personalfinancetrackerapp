import sqlite3

def connect_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            date TEXT,
            type TEXT, -- 'income' or 'expense'
            category TEXT,
            amount REAL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction(date, type, category, amount, description):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (date, type, category, amount, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, type, category, amount, description))
    conn.commit()
    conn.close()