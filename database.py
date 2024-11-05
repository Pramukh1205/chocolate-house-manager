import sqlite3

def connect_db():
    conn = sqlite3.connect("chocolate_house.db")
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        flavor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_name TEXT NOT NULL,
        start_date TEXT,
        end_date TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredient_inventory (
        ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        quantity REAL,
        unit TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_suggestions (
        suggestion_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        suggested_flavor TEXT,
        allergy_concerns TEXT
    )
    ''')

    conn.commit()
    conn.close()

# Run this function once to create tables
create_tables()