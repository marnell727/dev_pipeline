import sqlite3
connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

columns = {
  'I':'id',
  'N':'name',
  'A':'address',
  'C':'city',
  'S':'state',
  'Z':'zipcode',
  'P':'phone',
  'E':'email',
}
def display_records(query,values = None):
  values = values
  query = query
  if values:
    records = cursor.execute(query,values).fetchall()
  else:
    records = cursor.execute(query).fetchall()
  print(
    '''
--- Customers ---
ID  Name                     City          State Phone       Email'''
  )
  for idx in range(len(records)):
    id, name, city, state, phone, email = records[idx]
    print(f'{id:<4}{name:<25}{city:<15}{state:<4}{phone:<13}{email:<10}')

def display_detail(query,values = None):
  values = values
  query = query
  record = cursor.execute(query,values).fetchone()
  id, name, address, city, state, zipcode, phone, email = record
  print(f'''
+++ Customer Detail +++
ID:     {id}
Name:   {name}
Address:{address}
City:   {city}
State:  {state}
Zipcode:{zipcode}
Phone:  {phone}
Email:  {email}
''')

def cud_record(query,values):
  query = query
  values = values
  cursor.execute(query,values)
  connection.commit()

choice = ''
while choice.upper() != 'Q':
  print(
    '''**** Customer Database ****

  [1] View All Customers
  [2] Search Customers
  [3] Add a New Customer
  [Q] Quit
  '''
  )

  choice = input('>>> ')

  if choice == '1':
    query = 'select customer_id,Name,City,State,Phone,Email from customers'
    display_records(query)
    cid = (input('\nEnter a Customer ID to View a Customer: '),)
    if cid != None:
      query_detail = 'select customer_id,Name,street_address,City,State,postal_code,Phone,Email from customers where customer_id = ?'
      display_detail(query_detail,cid)
    update_delete = input('''
  To update a field, enter the first letter of the field.
  To delete this record, type 'DELETE'.
  To return to the main menu, press 'Enter'.
  >>> ''')
    if update_delete == 'DELETE':
      query = 'delete from customers where customer_id = ?'
      cud_record(query,cid)
    elif update_delete.upper() in columns.keys():
      column = columns[update_delete]
      value = input(f'\nWhat value would you like to assign to the {column} field: ')
      values = (value,cid[0])
      query = f'update customers set {column} = ? where customer_id = ?'
      cud_record(query,values)
      print(f'\nSUCCESS: {column} updated!\n')
      display_detail(query_detail,cid)

  elif choice == '2':
    search = ('%' + input('Enter a Customer name to search: ') + '%',)
    query = 'select customer_id,Name,City,State,Phone,Email from customers where name like ?'
    display_records(query,search)
  elif choice == '3':
    print('Please fill out the form below to add a new Customer:\n\n')
    name = input('Name:    ')
    address = input('Address: ')
    city = input('City:    ')
    state = input('State:   ')
    zipcode = input('Zipcode: ')
    phone = input('Phone:   ')
    email = input('Email:   ')
    values = (name, address, city, state, zipcode, phone, email)
    query = 'insert into customers (name, street_address, city, state, postal_code, phone, email) values (?,?,?,?,?,?,?)'
    cud_record(query, values)
    print(f'SUCCESS: Customer {name} successfully added!')