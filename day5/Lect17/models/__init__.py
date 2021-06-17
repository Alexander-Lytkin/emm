import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

CREATE_QUERY = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT, password TEXT, about TEXT)"
cur.execute(CREATE_QUERY)

conn.commit()
conn.close()
