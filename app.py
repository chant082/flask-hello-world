import os
import psycopg2

from flask import Flask
app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
conn = None
cur = None
try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # SQL work goes here

    conn.commit()
    return "Success message here"
except Exception as e:
    if conn is not None:
        conn.rollback()
    return f"Database error: {e}"
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

@app.route('/')
def hello_world():
    return 'Hello World! from YOUR NAME in 3308'
