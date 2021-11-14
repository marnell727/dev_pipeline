query = '''SELECT name, make, model, price FROM Products  WHERE price = 49.99
ORDER BY price DESC
LIMIT 5'''

def parse_sql(query):
    sql_dict = {}
    if 'SELECT ' in query:
        if ' FROM' in query:
            select_cl = query.partition('SELECT ')[2].partition(' FROM')[0]
        else:
            select_cl = query.partition('SELECT ')[2]
    if 'FROM ' in query:
        if ' WHERE' in query:
            from_cl = query.partition('FROM ')[2].partition(' WHERE')[0]
    if 'WHERE ' in query:
        if ' ORDER BY' in query:
            where_cl = query.partition('WHERE ')[2].partition(' ORDER BY')[0]
    if 'ORDER BY ' in query:
        if ' LIMIT' in query:
            order_cl = query.partition('ORDER BY ')[2].partition(' LIMIT')[0]
    if 'LIMIT ' in query:
            limit_cl = query.partition('ORDER BY ')[2]


print(parse_sql(query))

{
   'fields': [
      'name', 
      'make', 
      'model', 
      'price'
   ],
   'table': 'Products',
   'where': {
      'price': 49.99
   },
   'order_by': {
      'field': 'price',
      'order': 'DESC'
   },
   'limit': 5
}