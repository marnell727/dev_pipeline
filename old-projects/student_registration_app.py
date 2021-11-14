import sqlite3
from datetime import date
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def display_people(values = None):
  if values:
    query = 'select person_id,first_name || " " || last_name as name,email,phone,City,State \
    from people where active = 1'
    records = cursor.execute(query,values).fetchall()
  else:
    query = 'select person_id,first_name || " " || last_name as name,email,phone,City,State \
    from people where active = 1'
    records = cursor.execute(query).fetchall()
  print(
    '''
--- People ---

ID  Name               Email                    Phone          City           State'''
  )
  for idx in range(len(records)):
    id, name, email, phone, city, state = records[idx]
    print(f'{id:<4}{name:<19}{email:<25}{phone:<15}{city:<15}{state:<4}')

def display_courses(values = None):
  if values:
    query = 'select course_id, name, description from Courses where active = 1 and course_id = ?'
    records = cursor.execute(query,values).fetchall()
  else:
    query = 'select course_id, name, description from Courses where active = 1'
    records = cursor.execute(query).fetchall()
  print(
    '''
--- Courses ---

Course ID   Name      Description'''
  )
  for idx in range(len(records)):
    course_id, name, description = records[idx]
    print(f'{course_id:^12}{name:<10}{description}')

def display_cohorts(values = None):
  if values:
    query = 'select ch.cohort_id, p.first_name || " " || p.last_name as instructor, cs.name, ch.start_date, \
    ch.end_date from Cohort ch left outer join People p \
    on ch.instructor_id = p.person_id \
    left outer join Courses cs \
    on ch.course_id = cs.course_id \
    where ch.active = 1 and ch.course_id = ?'
    records = cursor.execute(query,values).fetchall()
  else:
    query = 'select ch.cohort_id, p.first_name || " " || p.last_name as instructor, cs.name, ch.start_date, ch.end_date \
      from Cohort ch left outer join People p on ch.instructor_id = p.person_id \
      left outer join Courses cs on ch.course_id = cs.course_id where ch.active = 1'
    records = cursor.execute(query).fetchall()
  print(
    '''
--- Cohorts ---

Cohort ID Instructor Name    Course Name   Start Date              End Date'''
  )
  for idx in range(len(records)):
    cohort_id, instructor, course, start_date, end_date = records[idx]
    print(f'{cohort_id:^10}{instructor:<19}{course:<14}{start_date:<24}{end_date:<15}')

def display_registrations(values = None):
  if values:
    query = 'select sr.cohort_id, cs.name, pi.first_name || " " || pi.last_name as instructor, \
p.person_id, p.first_name || " " || p.last_name as student, sr.registration_date, \
sr.completion_date, sr.drop_date \
from Student_Cohort_Registration sr left outer join People p \
on sr.student_id = p.person_id left outer join Cohort ch \
on sr.cohort_id = ch.cohort_id left outer join Courses cs \
on ch.course_id = cs.course_id left outer join People pi \
on ch.instructor_id = pi.person_id where sr.cohort_id = ? and sr.completion_date = " " and drop_date == " "'
    records = cursor.execute(query,values).fetchall()
  else:
    query = 'select sr.cohort_id, cs.name, pi.first_name || " " || pi.last_name as instructor, \
p.person_id, p.first_name || " " || p.last_name as student, sr.registration_date, \
sr.completion_date, sr.drop_date \
from Student_Cohort_Registration sr left outer join People p \
on sr.student_id = p.person_id left outer join Cohort ch \
on sr.cohort_id = ch.cohort_id left outer join Courses cs \
on ch.course_id = cs.course_id left outer join People pi \
on ch.instructor_id = pi.person_id where sr.completion_date = " " and drop_date == " "'
    records = cursor.execute(query).fetchall()
  print(
    '''
--- Student Cohort Registrations ---

Cohort ID   Course Name   Instructor         Student ID  Student            Registration Date       Completion Date        Drop Date'''
  )
  for idx in range(len(records)):
    id, name, instructor, student_id, student, registration_date, completion_date, drop_date = records[idx]
    print(f'{id:^12}{name:<14}{instructor:<19}{student_id:^12}{student:<19}{registration_date:<24}{completion_date:<23}{drop_date}')

def display_inactive_people(values = None):
  if values:
    query = 'select person_id,first_name || " " || last_name as name,email,phone,City,State \
    from people where active = 0'
    records = cursor.execute(query,values).fetchall()
  else:
    query = 'select person_id,first_name || " " || last_name as name,email,phone,City,State \
    from people where active = 0'
    records = cursor.execute(query).fetchall()
  print(
    '''
--- People ---

ID  Name               Email                    Phone          City           State'''
  )
  for idx in range(len(records)):
    id, name, email, phone, city, state = records[idx]
    print(f'{id:<4}{name:<19}{email:<25}{phone:<15}{city:<15}{state:<4}')

def display_inactive_courses(values = None):
  if values:
    query = 'select course_id, name, description from Courses where active = 0 and course_id = ?'
    records = cursor.execute(query,values).fetchall()
  else:
    query = 'select course_id, name, description from Courses where active = 0'
    records = cursor.execute(query).fetchall()
  print(
    '''
--- Courses ---

Course ID   Name      Description'''
  )
  for idx in range(len(records)):
    course_id, name, description = records[idx]
    print(f'{course_id:^12}{name:<10}{description}')

def display_inactive_cohorts(values = None):
  if values:
    query = 'select ch.cohort_id, p.first_name || " " || p.last_name as instructor, cs.name, ch.start_date, \
    ch.end_date from Cohort ch left outer join People p \
    on ch.instructor_id = p.person_id \
    left outer join Courses cs \
    on ch.course_id = cs.course_id \
    where ch.active = 0 and ch.course_id = ?'
    records = cursor.execute(query,values).fetchall()
  else:
    query = 'select ch.cohort_id, p.first_name || " " || p.last_name as instructor, cs.name, ch.start_date, ch.end_date \
      from Cohort ch left outer join People p on ch.instructor_id = p.person_id \
      left outer join Courses cs on ch.course_id = cs.course_id where ch.active = 0'
    records = cursor.execute(query).fetchall()
  print(
    '''
--- Cohorts ---

Cohort ID Instructor Name    Course Name   Start Date              End Date'''
  )
  for idx in range(len(records)):
    cohort_id, instructor, course, start_date, end_date = records[idx]
    print(f'{cohort_id:^10}{instructor:<19}{course:<14}{start_date:<24}{end_date:<15}')

def display_inactive_registrations(values = None):
  if values:
    query = 'select sr.cohort_id, cs.name, pi.first_name || " " || pi.last_name as instructor, \
p.person_id, p.first_name || " " || p.last_name as student, sr.registration_date, \
sr.completion_date, sr.drop_date \
from Student_Cohort_Registration sr left outer join People p \
on sr.student_id = p.person_id left outer join Cohort ch \
on sr.cohort_id = ch.cohort_id left outer join Courses cs \
on ch.course_id = cs.course_id left outer join People pi \
on ch.instructor_id = pi.person_id where sr.cohort_id = ? and drop_date != " "'
    records = cursor.execute(query,values).fetchall()
  else:
    query = 'select sr.cohort_id, cs.name, pi.first_name || " " || pi.last_name as instructor, \
p.person_id, p.first_name || " " || p.last_name as student, sr.registration_date, \
sr.completion_date, sr.drop_date \
from Student_Cohort_Registration sr left outer join People p \
on sr.student_id = p.person_id left outer join Cohort ch \
on sr.cohort_id = ch.cohort_id left outer join Courses cs \
on ch.course_id = cs.course_id left outer join People pi \
on ch.instructor_id = pi.person_id where drop_date != " "'
    records = cursor.execute(query).fetchall()
  print(
    '''
--- Student Cohort Registrations ---

Cohort ID   Course Name   Instructor         Student ID  Student            Registration Date       Completion Date        Drop Date'''
  )
  for idx in range(len(records)):
    id, name, instructor, student_id, student, registration_date, completion_date, drop_date = records[idx]
    print(f'{id:^12}{name:<14}{instructor:<19}{student_id:^12}{student:<19}{registration_date:<24}{completion_date:<23}{drop_date}')

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
  [4] View Student Registrations for a Cohort
  [5] Add a new Student
  [6] Add a new Course
  [7] Add a new Cohort
  [8] Register student for a Cohort
  [9] Remove a student from a Cohort
  [10] Deactivate a Course
  [11] Deactivate a Student or Instructor
  [12] Deactivate a Cohort
  [13] Complete a Course for a Student
  [14] Reactivate a Course, Student, Cohort, or Registration
  [Q] Quit
  '''
  )
  choice = input('>>> ')

  if choice == '1':
    display_people()
  elif choice == '2':
    display_courses()
  elif choice == '3':
    display_courses()
    course_id  = (input("\nPlease enter the ID of the course whose active cohorts you would like to view:\n"),)
    display_cohorts(course_id)
  elif choice == '4':
    display_cohorts()
    cohort_id  = (input("\nPlease enter the ID of the cohort whose student registrations you would like to view:\n"),)
    display_registrations(cohort_id)
  elif choice == '5':
    print('Please fill out the form below to add a new Student:\n\n')
    first_name = input('First Name: ')
    last_name =input('Last Name:  ')
    address = input('Address:    ')
    city = input('City:       ')
    state = input('State:      ')
    zipcode = input('Zipcode:    ')
    phone = input('Phone:      ')
    password = input('Password:   ')
    email = input('Email:      ')
    values = (first_name, last_name, email, phone, password, address, city, state, zipcode)
    query = 'insert into people (first_name, last_name, email, phone, password, address, city, state, postal_code) values (?,?,?,?,?,?,?,?,?)'
    cud_record(query, values)
    print(f'\nSUCCESS: Student {first_name} {last_name} successfully added!')
  elif choice =='6':
    print('Please fill out the form below to add a new Course:\n\n')
    name = input('Course Name:      ')
    description = input('Course Description: ')
    values = (name, description)
    query = 'insert into courses (name, description) values (?,?)'
    cud_record(query, values)
    print(f'\nSUCCESS: Course {name}: {description} successfully added!')
  elif choice =='7':
    display_courses()
    course = input('\nPlease enter the ID of the course for which you would like to add a cohort:\n')
    display_people()
    instructor = input('\nPlease enter the ID of the instructor for this cohort:\n')
    start_date = input('\nPlease enter the start date for this cohort in the format "YYYY-MM-DD hh:mm:ss"\n')
    end_date = input('\nPlease enter the end date for this cohort in the format "YYYY-MM-DD hh:mm:ss"\n')
    values = (course, instructor, start_date, end_date)
    query = 'insert into Cohort (course_id, instructor_id, start_date, end_date) \
      values (?, ?, ?, ?)'
    cud_record(query, values)
    print(f'\nSUCCESS: Cohort successfully added!\n')
    display_cohorts()
  elif choice =='8':
    display_cohorts()
    cohort = input('\nPlease enter the ID of the cohort for which you would like to register a student:\n')
    display_people()
    student = input('\nPlease enter the ID of the student you would like to register:\n')
    registration_date = date.today()
    values = (cohort, student, registration_date)
    query = 'insert into Student_Cohort_Registration (cohort_id, student_id, registration_date, completion_date, drop_date) \
      values (?, ?, ?, " ", " ")'
    cud_record(query, values)
    print(f'\nSUCCESS: Student successfully registered!\n')
    display_registrations(cohort)
  elif choice =='9':
    display_cohorts()
    cohort = input('\nPlease enter the ID of the cohort from which you would like to remove a student:\n')
    display_registrations(cohort)
    student = input('\nPlease enter the ID of the student you would like to remove from the cohort:\n')
    values = (cohort, student)
    query = 'update Student_Cohort_Registration set drop_date = date("now") where cohort_id = ? and student_id = ?'
    cud_record(query,values)
    print(f'\nSUCCESS: Student successfully removed from cohort!\n')
    display_registrations((cohort,))
  elif choice =='10':
    display_courses()
    values = (input('\nPlease enter the ID of the course you would like to deactivate:\n'),)
    query = 'update courses set active = 0 where course_id = ?'
    cud_record(query, values)
    print(f'\nSUCCESS: Course successfully deactivated!\n')
    display_courses()
  elif choice =='11':
    display_people()
    values = (input('\nPlease enter the ID of the person you would like to deactivate:\n'),)
    query = 'update people set active = 0 where person_id = ?'
    cud_record(query, values)
    display_people()
    print(f'\nSUCCESS: Person successfully deactivated!\n')
  elif choice =='12':
    display_cohorts()
    values = (input('\nPlease enter the ID of the cohort you would like to deactivate:\n'),)
    query = 'update cohort set active = 0 where cohort_id = ?'
    cud_record(query, values)
    display_cohorts()
    print(f'\nSUCCESS: Cohort successfully deactivated!\n')
  elif choice =='13':
    display_cohorts()
    cohort = input('\nPlease enter the Cohort ID for the course that the student has completedt:\n')
    display_registrations(cohort)
    student = input('\nPlease enter the ID of the student that has completed the course:\n')
    values = (cohort, student)
    query = 'update Student_Cohort_Registration set completion_date = date("now") where cohort_id = ? and student_id = ?'
    cud_record(query,values)
    print(f'\nSUCCESS: Student successfully completed course!\n')
    display_registrations((cohort,))
  elif choice =='14':
    record_to_reactivate = ''
    while record_to_reactivate == '':
      record_to_reactivate = input('''
      Would you like to reactivate a (1) Course, (2) Student, (3) Cohort, or (4) Registration?
      ''')
      if record_to_reactivate == '1':
        display_inactive_courses()
        values = (input('\nPlease enter the ID of the course you would like to activate:\n'),)
        query = 'update courses set active = 1 where course_id = ?'
        cud_record(query, values)
        print(f'\nSUCCESS: Course successfully activated!\n')
        display_courses()
      elif record_to_reactivate == '2':
        display_inactive_people()
        values = (input('\nPlease enter the ID of the person you would like to activate:\n'),)
        query = 'update people set active = 1 where person_id = ?'
        cud_record(query, values)
        display_people()
        print(f'\nSUCCESS: Person successfully activated!\n')
      elif record_to_reactivate == '3':
        display_inactive_cohorts()
        values = (input('\nPlease enter the ID of the cohort you would like to activate:\n'),)
        query = 'update cohort set active = 1 where cohort_id = ?'
        cud_record(query, values)
        display_cohorts()
        print(f'\nSUCCESS: Cohort successfully activated!\n')
      elif record_to_reactivate == '4':
        display_cohorts()
        cohort = input('\nPlease enter the ID of the cohort in which you would like to reactivate a student registration:\n')
        display_inactive_registrations((cohort,))
        student = input('\nPlease enter the ID of the student you would like to reactivate in the cohort:\n')
        values = (cohort, student)
        query = 'update Student_Cohort_Registration set drop_date = " ", registration_date = date("now") where cohort_id = ? and student_id = ?'
        cud_record(query,values)
        print(f'\nSUCCESS: Student successfully reactivated in cohort!\n')
        display_registrations((cohort,))
      else:
        pass