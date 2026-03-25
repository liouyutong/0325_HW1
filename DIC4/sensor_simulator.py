import sqlite3
import random
import time
from datetime import datetime

# --- CONFIG ---
DB_FILE = 'aiotdb.db'
INTERVAL = 2  # 2 seconds as requested

def init_db():
    """Initializes the SQLite database with the 'sensors' table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            humid REAL NOT NULL,
            temp REAL NOT NULL,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database initialized: {DB_FILE}, table: sensors")

def simulate():
    """Generates random data and inserts into sensors table every 2 seconds."""
    print(f"Starting simulation. Interval: {INTERVAL}s")
    while True:
        try:
            # DHT11 typical ranges: 20-80% RH, 0-50°C
            humid = round(random.uniform(30.0, 90.0), 2)
            temp = round(random.uniform(15.0, 35.0), 2)
            
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            record_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cursor.execute(
                "INSERT INTO sensors (humid, temp, time) VALUES (?, ?, ?)",
                (humid, temp, record_time)
            )
            conn.commit()
            conn.close()
            
            print(f"[{record_time}] Inserted: Humid: {humid}%, Temp: {temp}°C")
            
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(INTERVAL)

if __name__ == '__main__':
    init_db()
    simulate()
