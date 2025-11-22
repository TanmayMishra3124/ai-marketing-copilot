import sqlite3
import os
from config.settings import DB_PATH

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    schema_path = os.path.join(os.path.dirname(__file__), 'models.sql')
    with open(schema_path, 'r') as f:
        schema = f.read()
    
    conn = get_db_connection()
    conn.executescript(schema)
    conn.close()

def save_campaign(brand, audience, platform, tone, goal, content):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO campaigns (brand, audience, platform, tone, goal, content) VALUES (?, ?, ?, ?, ?, ?)',
        (brand, audience, platform, tone, goal, content)
    )
    conn.commit()
    conn.close()

def get_campaigns():
    conn = get_db_connection()
    campaigns = conn.execute('SELECT * FROM campaigns ORDER BY created_at DESC').fetchall()
    conn.close()
    return campaigns
