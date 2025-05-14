from database import create_connection
import sqlite3

def add_course(name, units):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (name, units) VALUES (?, ?)", (name, units))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError:
        print(" Course name must be unique.")
    conn.close()