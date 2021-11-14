import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def display_people(query,values = None):
  if values:
    records = cursor.execute(query,values).fetchall()
  else:
    records = cursor.execute(query).fetchall()
  print(
    '''
--- People ---

ID  Name                      Email          Phone         City           State'''
  )
  for idx in range(len(records)):
    id, first_name, last_name, email, phone, city, state = records[idx]
    print(f'{id:<4}{first_name:<13}{last_name:<13}{email:<15}{phone:<14}{city:<15}{state:<4}')

def display_courses(query,values = None):
  if values:
    records = cursor.execute(query,values).fetchall()
  else:
    records = cursor.execute(query).fetchall()
  print(
    '''
--- People ---

ID  Name                      Email          Phone         City           State'''
  )
  for idx in range(len(records)):
    id, first_name, last_name, email, phone, city, state = records[idx]
    print(f'{id:<4}{first_name:<13}{last_name:<13}{email:<15}{phone:<14}{city:<15}{state:<4}')

def display_cohorts(query,values = None):
  if values:
    records = cursor.execute(query,values).fetchall()
  else:
    records = cursor.execute(query).fetchall()
  print(
    '''
--- People ---

ID  Name                      Email          Phone         City           State'''
  )
  for idx in range(len(records)):
    id, first_name, last_name, email, phone, city, state = records[idx]
    print(f'{id:<4}{first_name:<13}{last_name:<13}{email:<15}{phone:<14}{city:<15}{state:<4}')

def display_registrations(query,values = None):
  if values:
    records = cursor.execute(query,values).fetchall()
  else:
    records = cursor.execute(query).fetchall()
  print(
    '''
--- People ---

ID  Name                      Email          Phone         City           State'''
  )
  for idx in range(len(records)):
    id, first_name, last_name, email, phone, city, state = records[idx]
    print(f'{id:<4}{first_name:<13}{last_name:<13}{email:<15}{phone:<14}{city:<15}{state:<4}')

def cud_record(query,values):
  query = query
  values = values
  cursor.execute(query,values)
  connection.commit()

choice = ''
while choice.upper() != 'Q':
  print(
    '''

**** Student Registration Database ****

  [1] View all active Students and Instructors
  [2] View all Courses
  [3] View all active Cohorts for a Course
  [4] View active Registrations for a Cohort
  [5] Add a new Student
  [6] Add a new Course
  [7] Add a new Cohort
  [8] Register student for a Cohort
  [9] Remove a student from a Cohort
  [10] Deactivate a Course
  [11] Deactivate a Student or Instructor
  [12] Complete a Course for a Student
  [13] Reactivate a Course, Student, Cohort, or Registration
  [Q] Quit
  '''
  )

  choice = input('>>> ')

  if choice == '1':
    query = 'select person_id,first_name,last_name,email,phone,City,State from people'
    display_people(query)
  elif choice == '2':
    query = 'select person_id,first_name,last_name,email,phone,City,State from people'
    display_people(query)
  elif choice == '3':
    print('Please fill out the form below to add a new Student:\n\n')
    person_id = input('ID:         ')
    first_name = input('First Name: ')
    last_name =input('Last Name:  ')
    address = input('Address:    ')
    city = input('City:       ')
    state = input('State:      ')
    zipcode = input('Zipcode:    ')
    phone = input('Phone:      ')
    password = input('Password:   ')
    email = input('Email:      ')
    values = (person_id, first_name, last_name, email, phone, password, address, city, state, zipcode)
    query = 'insert into people (person_id, first_name, last_name, email, phone, password, address, city, state, postal_code) values (?,?,?,?,?,?,?,?,?,?)'
    cud_record(query, values)
    print(f'SUCCESS: Student {first_name} {last_name} successfully added!')
  elif choice =='4':
    print('Please fill out the form below to add a new Course:\n\n')
    person_id = input('ID:         ')
    first_name = input('First Name: ')
    last_name =input('Last Name:  ')
    address = input('Address:    ')
    city = input('City:       ')
    state = input('State:      ')
    zipcode = input('Zipcode:    ')
    phone = input('Phone:      ')
    password = input('Password:   ')
    email = input('Email:      ')
    values = (person_id, first_name, last_name, email, phone, password, address, city, state, zipcode)
    query = 'insert into courses (person_id, first_name, last_name, email, phone, password, address, city, state, postal_code) values (?,?,?,?,?,?,?,?,?,?)'
    cud_record(query, values)
    print(f'SUCCESS: Course {first_name} {last_name} successfully added!')
    
