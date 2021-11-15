import sqlite3

connection = sqlite3.connect('friends_phonebook.db')
cursor = connection.cursor()

with open('create_phonebook_tables.txt','r') as myfile:
    cursor.executescript(myfile.read())

connection.commit()