import sqlite3
from datetime import date

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

class User:
    def __init__(self,id,fname,lname,city,state,email,password,create_date):
        self.user_id = id
        self.first_name = fname
        self.last_name = lname
        self.city = city
        self.state = state
        self.email = email
        self.password = password
        self.date_created = create_date

    def change_password(self,password):
        self.password = password

    def change_email(self,email):
        self.email = email

    def display_user(self):
        print(f'''\nUsername: {self.user_id}
First Name: {self.first_name}
Last Name: {self.last_name}
City: {self.city}
State: {self.state}
Email: {self.email}
''')

    def save_user(self,cursor):
        query = 'insert into Users (user_id,first_name,last_name,city,state,email,password,date_created) \
values (?,?,?,?,?,?,?,?)'
        values = (self.user_id,self.first_name,self.last_name,self.city,self.state,\
            self.email,self.password,self.date_created)
        cursor.execute(query,values)
        connection.commit()

def lookup_user(cursor,values):
        query = 'select * from Users where user_id = ?'
        records = cursor.execute(query,values).fetchall()
        username, fname, lname, city, state, email, password, c_date = records[0]
        return User(username, fname, lname, city, state, email, password, c_date)

choice = ''
while choice.upper() != 'Q':
    choice = input('''Please select an option:
    A) Add new user
    B) Display current user
    C) Load user from DB
    D) Save current user to DB
    E) Change email address
    F) Change password
    Q) Quit
''')
    if choice.upper() == 'A':
        user = User(
            input('Please enter a username\n'),
            input('Please enter user\'s first name\n'),
            input('Please enter user\'s last name\n'),
            input('Please enter user\'s city\n'),
            input('Please enter user\'s state\n'),
            input('Please enter user\'s email\n'),
            input('Please enter user\'s password\n'),
            date.today()
        )
    if choice.upper() == 'B' and user:
        user.display_user()
    if choice.upper() == 'C':
        user = lookup_user(
            cursor,(input('Please enter a username\n'),)
        )
    if choice.upper() == 'D' and user:
        user.save_user(cursor)
    if choice.upper() == 'E' and user:
        user.change_email(
            input('Please enter a new email address for this user\n')
        )
    if choice.upper() == 'F' and user:
        user.change_password(
            input('Please enter a new password for this user\n')
        )