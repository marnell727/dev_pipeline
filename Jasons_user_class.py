import sqlite3

class User:
   def __init__(self):
      self.user_id = None
      self.first_name = None
      self.last_name = None
      self.city = None
      self.state = None
      self.email = None
      self.__password = None
      self.date_created = None
   
   def set_all(self, first_name, last_name, city, state, email, password, date_created = '2021-11-18 08:30:00'):
      self.first_name = first_name
      self.last_name = last_name
      self.city = city
      self.state = state
      self.email = email
      self.__password = password
      self.date_created = date_created
   
   def get_password(self):
      return self.__password

   def change_password(self, new_password):
      if new_password:
         self.__password = new_password

   def change_email(self, new_email):
      self.email = new_email

   def print_me(self):
      print(f'{self.user_id} {self.last_name}, {self.first_name}')
      print(f'  {self.city}, {self.state}')
      print(f'  {self.email}')
      print(f'  Created: {self.date_created}')

   def save(self, cursor):
      insert_sql = '''
         INSERT INTO Users 
            (first_name, last_name, city, state, email, password, date_created)
         VALUES
            (?, ?, ?, ?, ?, ?, ?)
      ;'''

      cursor.execute(insert_sql, (self.first_name, self.last_name, self.city, self.state, self.email, self.__password, self.date_created))
      cursor.connection.commit()

      # new_user_id = cursor.execute('SELECT user_id FROM Users WHERE email=?',(self.email,)).fetchone()
      new_user_id = cursor.execute('SELECT last_insert_rowid()').fetchone()
      self.user_id = new_user_id[0]

   def load(self, cursor):
      select_sql = '''
         SELECT user_id, first_name, last_name, city, state, email, date_created 
         FROM Users
         WHERE user_id=?;
      '''

      row = cursor.execute(select_sql, (self.user_id,)).fetchone()
      if not row:
         print("NOTHING RETURNED")
         return
      self.first_name = row[1]
      self.last_name = row[2]
      self.city = row[3]
      self.state = row[4]
      self.email = row[5]
      self.date_created = row[6]


def initialize_database(cursor):
   create_table_sql = '''
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
   cursor.execute(create_table_sql)
   cursor.connection.commit()
   

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

initialize_database(cursor)

lard_ben = User()
lard_ben.set_all('Ben', 'Nicklaus', 'Naples', 'FL', 'lord_ben_10@devpipeline.com', 'IAmLordBen!')
lard_ben.save(cursor)

new_ben = User()
new_ben.user_id = 100
new_ben.load(cursor)
new_ben.print_me()