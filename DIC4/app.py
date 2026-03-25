import os
import time
import sqlite3
import random
import threading
from datetime import datetime
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# --- DATABASE CONFIG ---
# Note: User requested 'pymysql' for 'SQLite'.
# 'pymysql' is a MySQL driver and does not support SQLite.
# We will use the built-in 'sqlite3' library for SQLite.
DB_FILE = 'sensors.db'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the SQLite database with id, humid, temp, and time fields."""
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS sensors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                humid REAL NOT NULL,
                temp REAL NOT NULL,
                time DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# --- BACKGROUND DATA SIMULATOR ---
def data_inserter():
    """Inserts random sensor data every 3 seconds."""
    while True:
        try:
            humid = round(random.uniform(40.0, 70.0), 2)  # Random humidity between 40-70%
            temp = round(random.uniform(20.0, 30.0), 2)    # Random temp between 20-30°C
            
            with get_db_connection() as conn:
                conn.execute(
                    "INSERT INTO sensors (humid, temp, time) VALUES (?, ?, ?)",
                    (humid, temp, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                )
                conn.commit()
            
            # Print to console for confirmation
            print(f"[{datetime.now()}] Data Inserted: Humid: {humid}%, Temp: {temp}°C")
            
        except Exception as e:
            print(f"Error in background background thread: {e}")
        
        time.sleep(3)

# --- ROUTES ---
@app.route('/')
def index():
    """Main dashboard page."""
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """Returns the latest 10 readings for UI updates."""
    with get_db_connection() as conn:
        rows = conn.execute("SELECT * FROM sensors ORDER BY id DESC LIMIT 10").fetchall()
        data = [dict(row) for row in rows]
        return jsonify(data)

if __name__ == '__main__':
    # Initialize the database
    init_db()
    
    # Start the background data insertion thread
    data_thread = threading.Thread(target=data_inserter, daemon=True)
    data_thread.start()
    
    # Run the Flask app
    app.run(debug=True, port=5000)
