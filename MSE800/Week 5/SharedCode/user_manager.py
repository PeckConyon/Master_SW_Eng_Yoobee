from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
    
def advanced_search(user_id, name):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name LIKE ? AND id = ?"
    params = (f"%{name}%", user_id)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

def assign_course_to_user(user_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO user_courses (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
        conn.commit()
        print(" Course assigned to user successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def search_user_courses(user_name, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT u.name, c.name FROM users as u JOIN user_courses as uc ON u.id = uc.user_id JOIN courses c ON uc.course_id = c.id where u.name = ?  AND uc.course_id = ?"
    params = (user_name, course_id)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows