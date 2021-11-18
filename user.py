import sqlite3
from datetime import date

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

class User:
    def __init__(self,fname,lname,city,state,email,password):
        self.user_id = None
        self.first_name = fname
        self.last_name = lname
        self.city = city
        self.state = state
        self.email = email
        self.password = password
        self.date_created = date.today()

    def change_password(self,new_password):
        if new_password:
            self.password = new_password

    def change_email(self,email):
        self.email = email

    def display_user(self):
        print(f'''\nUser ID: {self.user_id}
First Name: {self.first_name}
Last Name: {self.last_name}
City: {self.city}
State: {self.state}
Email: {self.email}
''')

    def save_user(self,cursor):
        query = 'INSERT INTO Users (first_name,last_name,city,state,email,password,date_created) \
VALUES (?,?,?,?,?,?,?)'
        values = (self.first_name,self.last_name,self.city,self.state,\
            self.email,self.password,self.date_created)
        cursor.execute(query,values)
        connection.commit()

    def load_user(self,cursor,values):
        query = 'SELECT user_id, first_name, last_name, city, state, email, date_created FROM Users WHERE user_id = ?'
        records = cursor.execute(query,values).fetchone()
        self.user_id, self.first_name, self.last_name, self.city, self.state, self.email, self.date_created = records
        

def initialize_db(cursor):
    query = '''DROP TABLE Users;
    
    CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    city TEXT,
    state TEXT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    date_created TEXT
);'''
    cursor.executescript(query)

initialize_db(cursor)

user = User('Tom','Fong','Santa Barbara','CA','tommyboy@email.com','poiupoiu')
user.save_user(cursor)
user = User('Phil','Stubbins','Santa Barbara','CA','philsemail@email.com','poiupoiu')
user.save_user(cursor)
user = User('Michael','Arnell','Lehi','UT','marnell@email.com','asdfasdf')
user.save_user(cursor)

user.load_user(cursor,(1,))

user.display_user()