import sqlite3

# Function to initialize the database and create the table if not exists
def initialize_db():
    conn = sqlite3.connect("databases/login_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            level TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(username, password,level):
    conn = sqlite3.connect("databases/login_database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password,level) VALUES (?, ?, ?)", (username, password,level))
    conn.commit()
    conn.close()

# Function to check if the entered username and password are correct
def check_credentials(username, password):
    conn = sqlite3.connect("databases/login_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    stored_password = cursor.fetchone()

    if stored_password and stored_password[0] == password:
        return True
    else:
        return False

    conn.close()
