import sqlite3

DB_NAME='jobs.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn=sqlite3.connect('jobs.db')
    c=conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KET AUTOINCREMENT,
        company TEXT NOT NULL,
        position TEXT NOT NULL,
        date_applied TEXT NOT NULL,
        status TEXT NOT NULL
        )
            ''')
    conn.commit()
    conn.close()