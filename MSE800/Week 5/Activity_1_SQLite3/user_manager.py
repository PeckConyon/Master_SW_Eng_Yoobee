from data_access_manager import DataAccessManager
import sqlite3

def add_user(name, email):
    dam = DataAccessManager('user_db')
    try:
        dam.execute_query("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")

def view_users():
    dam = DataAccessManager('user_db')
    rows = dam.fetch("SELECT * FROM users")
    return rows

def search_user(name):
    dam = DataAccessManager('user_db')
    rows = dam.fetch_data.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    return rows

def delete_user(user_id):
    dam = DataAccessManager('user_db')
    dam.execute_query("DELETE FROM users WHERE id = ?", (user_id,))
    print("🗑️ User deleted.")
    
def advanced_search(user_id, name):
    dam = DataAccessManager('user_db')
    rows = dam.fetch_data("SELECT * FROM users WHERE name LIKE ? AND id = ?", (f"%{name}%", user_id))
    return rows
