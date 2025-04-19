import sqlite3

def create_database():
    conn = sqlite3.connect('data/webMonitor.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS websites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website_url TEXT(150),
        monitor_status INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_name TEXT(50),
        email TEXT(50),
        phone_number INTEGER(15),
        preferred_contact TEXT(50)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        integration_name TEXT(50),
        key TEXT(150),
        value TEXT(150),
        status INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS down_tracking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website_id INTEGER,
        time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        error_code TEXT(50),
        sent_contact INTEGER,
        FOREIGN KEY (website_id) REFERENCES websites(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS website_monitor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website_id INTEGER,
        contact_id INTEGER,
        FOREIGN KEY (website_id) REFERENCES websites(id),
        FOREIGN KEY (contact_id) REFERENCES contacts(id)
    )
    ''')

    cursor.execute('''
    INSERT OR IGNORE INTO settings (integration_name, key, value, status)
    VALUES ('monitor_header', 'header', '{"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"}', 1)
    ''')

    conn.commit()
    conn.close()
