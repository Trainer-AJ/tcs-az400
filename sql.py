import sqlite3

def get_user_data(username):
    # Connect to SQLite database (for demo purposes)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Vulnerable SQL query with SQL Injection risk
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    user_data = cursor.fetchall()

    conn.close()
    return user_data

def main():
    # Simulate a user input
    username = input("Enter your username: ")

    # Fetch user data from database
    user_data = get_user_data(username)

    if user_data:
        print("User found:", user_data)
    else:
        print("No user found.")

if __name__ == "__main__":
    main()
