from flask import Flask, render_template_string
import mysql.connector
from random import choice
import string

app = Flask(__name__)

###################################################
# MySQL connection parameters
DB_CONFIG = {
    'host': 'app98.mysql.database.azure.com',
    'user': 'aj',
    'password': 'nooPho4ae5ooyai2',
    'database': 'testdb'
}
###################################################
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def insert_random_entry():
    connection = get_db_connection()
    cursor = connection.cursor()
    random_string = ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))
    cursor.execute("INSERT INTO entries (value) VALUES (%s)", (random_string,))
    connection.commit()
    cursor.execute("SELECT * FROM entries ORDER BY id DESC LIMIT 1")
    entry = cursor.fetchone()
    cursor.close()
    connection.close()
    return entry

@app.route('/')
def index():
    entry = insert_random_entry()
    return render_template_string('''
        <html>
        <head><title>Random Entry</title></head>
        <body>
            <h1>Latest Entry</h1>
            <p>ID: {{ entry[0] }}</p>
            <p>Value: {{ entry[1] }}</p>
        </body>
        </html>
    ''', entry=entry)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80',debug=True)
