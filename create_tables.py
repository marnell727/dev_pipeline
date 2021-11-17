import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

with open('create_users_table.txt','r') as myfile:
    cursor.executescript(myfile.read())

connection.commit()