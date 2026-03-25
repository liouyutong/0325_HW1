import streamlit as st
import pandas as pd
import sqlite3
import time
from datetime import datetime

# --- SET UP PAGE ---
st.set_page_config(
    page_title="DHT11 Live Monitor",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Elegant Ancient (素雅古風) Green theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;700&display=swap');

    /* Background and global text */
    .stApp {
        background-color: #f1f8f1; /* Pale Green silk color */
        color: #1b4332; /* Deep forest green */
        font-family: 'Noto Serif TC', serif !important;
    }
    
    /* Willow Animation Container */
    .willow-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .willow-branch {
        position: absolute;
        top: -10px;
        right: 2%;
        width: 300px;
        transform-origin: top center;
        animation: sway 8s ease-in-out infinite;
        opacity: 0.5;
    }
    
    .willow-branch.left {
        left: 2%;
        right: auto;
        animation: sway 10s ease-in-out infinite reverse;
    }

    @keyframes sway {
        0%, 100% { transform: rotate(-5deg) translateY(0); }
        50% { transform: rotate(8deg) translateY(5px); }
    }

    /* Headers and titles */
    h1, h2, h3, .stMarkdown p {
        color: #2d5a27 !important;
        font-family: 'Noto Serif TC', serif !important;
    }

    h1 {
        border-bottom: 3px double #52796f; 
        display: inline-block;
        padding-bottom: 10px;
        margin-bottom: 2rem;
        letter-spacing: 0.2em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }

    /* Metric cards styling */
    [data-testid="stMetricValue"] {
        font-weight: bold;
        color: #1b4332 !important;
        font-family: 'Noto Serif TC', serif !important;
    }

    [data-testid="stMetricLabel"] {
        color: #52796f !important;
        letter-spacing: 0.15em;
        font-weight: 500;
        font-family: 'Noto Serif TC', serif !important;
    }

    /* Custom Frame for metrics */
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border: 1px solid #c0d8c0;
        border-radius: 12px;
        box-shadow: 4px 4px 20px rgba(45, 90, 39, 0.08);
    }
    
    /* Chart styling */
    .stPlotlyChart {
         background-color: transparent !important;
    }
    </style>
    
    <!-- Willow SVG Branch Animation -->
    <div class="willow-container">
        <!-- Right side willow -->
        <svg class="willow-branch" viewBox="0 0 100 200" preserveAspectRatio="xMinYMin meet">
            <path d="M70,0 C75,50 40,100 50,200" stroke="#52796f" stroke-width="0.8" fill="none"/>
            <path d="M65,30 C30,40 20,60" stroke="#8a9a5b" stroke-width="0.4" fill="none"/>
            <path d="M72,60 C95,80 85,130" stroke="#8a9a5b" stroke-width="0.4" fill="none"/>
            <path d="M60,100 C30,120 40,170" stroke="#8a9a5b" stroke-width="0.4" fill="none"/>
            <!-- Leaves -->
            <ellipse cx="20" cy="60" rx="1.5" ry="6" fill="#8a9a5b" transform="rotate(-30 20 60)"/>
            <ellipse cx="85" cy="130" rx="1.5" ry="6" fill="#8a9a5b" transform="rotate(30 85 130)"/>
            <ellipse cx="40" cy="170" rx="1.5" ry="6" fill="#8a9a5b" transform="rotate(-15 40 170)"/>
        </svg>
        <!-- Left side willow -->
        <svg class="willow-branch left" viewBox="0 0 100 200" preserveAspectRatio="xMinYMin meet">
            <path d="M30,0 C25,60 60,120 50,230" stroke="#52796f" stroke-width="0.8" fill="none"/>
            <path d="M35,40 C70,60 80,100" stroke="#8a9a5b" stroke-width="0.4" fill="none"/>
            <path d="M28,80 C10,110 20,160" stroke="#8a9a5b" stroke-width="0.4" fill="none"/>
            <ellipse cx="80" cy="100" rx="1.5" ry="6" fill="#8a9a5b" transform="rotate(20 80 100)"/>
            <ellipse cx="20" cy="160" rx="1.5" ry="6" fill="#8a9a5b" transform="rotate(-40 20 160)"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)

# --- DATABASE FETCH ---
DB_FILE = 'aiotdb.db'

def init_db_if_missing():
    """Initializes the SQLite database and table if they don't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            humid REAL NOT NULL,
            temp REAL NOT NULL,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Check if empty (important for first-time cloud deployment)
    cursor.execute("SELECT COUNT(*) FROM sensors")
    count = cursor.fetchone()[0]
    
    if count == 0:
        import random
        from datetime import datetime, timedelta
        # Insert 40 dummy records for the chart to look good
        now = datetime.now()
        for i in range(40):
            record_time = (now - timedelta(minutes=(40-i))).strftime('%Y-%m-%d %H:%M:%S')
            h = round(random.uniform(40.0, 70.0), 2)
            t = round(random.uniform(22.0, 28.0), 2)
            cursor.execute("INSERT INTO sensors (humid, temp, time) VALUES (?, ?, ?)", (h, t, record_time))
            
    conn.commit()
    conn.close()

def get_data(limit=50):
    """Fetches the latest readings from the database."""
    init_db_if_missing() # Ensure table exists at runtime
    try:
        conn = sqlite3.connect(DB_FILE)
        query = f"SELECT * FROM sensors ORDER BY id DESC LIMIT {limit}"
        df = pd.read_sql_query(query, conn)
        conn.close()
        # Ensure time is datetime
        df['time'] = pd.to_datetime(df['time'])
        return df.sort_values(by='time')
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame(columns=['id', 'humid', 'temp', 'time'])

# --- MAIN APP ---
st.title("🌡️ DHT11 Live Monitor")
st.caption("Real-time temperature & humidity data from aiotdb.db · sensors table")

# Placeholders for dynamic content
metrics_placeholder = st.empty()
chart_placeholder = st.empty()

# LOOP FOR DYNAMIC UPDATES
# Note: In Streamlit production, we use st_autorefresh. 
# Here we'll use a simple loop with st.rerun if it's a newer version or manual refresh.
while True:
    df = get_data(50)
    
    if not df.empty:
        latest = df.iloc[-1]
        
        # 1. Metrics Layout (Cards)
        with metrics_placeholder.container():
            col1, col2, col3, col4 = st.columns(4)
            
            # Current Temperature
            col1.metric("🌡️ TEMPERATURE", f"{latest['temp']}°C", delta=None)
            
            # Current Humidity
            col2.metric("💧 HUMIDITY", f"{latest['humid']}%", delta=None)
            
            # Additional Stats (Avg Temp/Max Temp) - Simple mockup of the UI in the image
            avg_temp = round(df['temp'].mean(), 1)
            max_temp = round(df['temp'].max(), 1)
            col3.metric("📈 TEMP AVG / MAX", f"{avg_temp}° / {max_temp}°")
            
            # Additional Stats (Avg Humid/Max Humid)
            avg_humid = round(df['humid'].mean(), 1)
            max_humid = round(df['humid'].max(), 1)
            col4.metric("📊 HUMID AVG / MAX", f"{avg_humid}% / {max_humid}%")

        # 2. Charts Layout
        with chart_placeholder.container():
            # Temperature Chart
            st.subheader("Temperature History (°C)")
            st.line_chart(df.set_index('time')['temp'], color="#ff4b4b")
            
            # Humidity Chart
            st.subheader("Humidity History (%)")
            st.line_chart(df.set_index('time')['humid'], color="#38bdf8")

    # Refresh every 2 seconds
    time.sleep(2)
    st.rerun() if hasattr(st, "rerun") else st.experimental_rerun()
