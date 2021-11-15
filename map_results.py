import sqlite3

def map_results(result_set,field_names_list):
    result_dicts = []
    for row in result_set:
        next_dict = dict(zip(columns,list(row)))
        result_dicts.append(next_dict)
    return result_dicts


connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

rows = [('DNA 15 Slim Messenger Bag (Graphite)', 159.95), ('DNA 15 Slim Messenger Bag (Cobalt)', 159.95)]
# cursor.execute("SELECT name, price FROM Products WHERE make='Tenba'").fetchall()
columns = ['name', 'price']

results = map_results(rows, columns)

print(f'{"price":<9} {"name":<25}')

for row in results:
   print(f'{row["price"]:<9} {row["name"]:<25}')