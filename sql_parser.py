query = '''SELECT name, make, model, price FROM Products WHERE price = 49.99 ORDER BY price DESC LIMIT 5'''

def parse_sql(query):
   sql_dict = {}
   clauses = {}
   keywords = ['SELECT','FROM','WHERE','ORDER BY','LIMIT']
   subquery = query
   for i in range(len(keywords) - 1):
      if keywords[i] in subquery:
         subquery = subquery.partition(keywords[i] + ' ')[2]
         for k in range(1,len(keywords) - 1):
            if keywords[i+k] in subquery:
               clauses[keywords[i]] = subquery.partition(' ' + keywords[i+k])[0]
               break
         if not clauses[keywords[i]]:
            clauses[keywords[i]] = subquery
   if keywords[len(keywords) - 1] in subquery:
      clauses[keywords[len(keywords) - 1]] = subquery.partition(keywords[len(keywords) - 1] + ' ')[2]
   print(clauses)
   if clauses['SELECT']:
      sql_dict['fields'] = clauses['SELECT'].split(', ')
   if clauses['FROM']:
      sql_dict['table'] = clauses['FROM']
   if clauses['WHERE']:
      sql_dict['where'] = {}
      sql_dict['where'][clauses['WHERE'].split(' = ')[0]] = clauses['WHERE'].split(' = ')[0]
   if clauses['ORDER BY']:
      sql_dict['order_by'] = {}
      sql_dict['order_by']['field'] = clauses['ORDER BY'].split(' ')[0]
      sql_dict['order_by']['order'] = clauses['ORDER BY'].split(' ')[1]
   if clauses['LIMIT']:
      sql_dict['limit'] = clauses['LIMIT']
   return sql_dict

print(parse_sql(query))