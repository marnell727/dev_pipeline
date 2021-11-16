import sqlite3
from datetime import date

connection = sqlite3.connect('users.db')
cursor = connection.cursor()


class User:
    def __init__(self,id,fname,lname,city,state,email,password):
        self.user_id
        self.first_name
        self.last_name
        self.city
        self.state
        self.email
        self.password
        self.date_created = date.today()

    def change_password(self,password):
        self.password = password

    def change_email(self,email):
        self.email = email

    def display_user(self):
        return self.first_name, self.last_name, self.city, self.state, self.email

    def lookup_user(self,cursor,query,values):
        records = cursor.executescript(query,values).fetchall()

    def save_user(self,cursor,query,values):
        records = cursor.executescript(query,values)
        connection.commit()


