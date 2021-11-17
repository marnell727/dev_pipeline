query = "SELECT name, make, model, price FROM Products WHERE price = 49.99 ORDER BY price DESC LIMIT 5"

def parse_sql(query):
   sql_dict = {}
   clauses = {}
   keywords = ['SELECT','FROM','WHERE','ORDER BY','LIMIT']
   subquery = query
   for i in range(len(keywords) - 1):
      if keywords[i] in subquery:
         subquery = subquery.partition(keywords[i] + ' ')[2]
         for k in range(1,len(keywords) - i):
            if keywords[i+k] in subquery:
               clauses[keywords[i]] = subquery.partition(' ' + keywords[i+k])[0]
               break
         if keywords[i] not in clauses:
            clauses[keywords[i]] = subquery
   if keywords[len(keywords) - 1] in subquery:
      clauses[keywords[len(keywords) - 1]] = subquery.partition(keywords[len(keywords) - 1] + ' ')[2]
   print(clauses)
   if 'SELECT' in clauses:
      sql_dict['fields'] = [x.strip() for x in clauses['SELECT'].split(',')]
   if 'FROM' in clauses:
      sql_dict['table'] = clauses['FROM']
   if 'WHERE' in clauses:
      sql_dict['where'] = {}
      sql_dict['where'][clauses['WHERE'].split('=')[0].strip()] = clauses['WHERE'].split('=')[1].strip()
   if 'ORDER BY' in clauses:
      sql_dict['order_by'] = {}
      sql_dict['order_by']['field'] = clauses['ORDER BY'].split(' ')[0]
      sql_dict['order_by']['order'] = clauses['ORDER BY'].split(' ')[1]
   if 'LIMIT' in clauses:
      sql_dict['limit'] = clauses['LIMIT']
   return sql_dict

def to_sql(sql_dict):
    clauses ={}
    clauses['SELECT'] = 'SELECT ' + ', '.join(sql_dict['fields'])
    clauses['FROM'] = 'FROM ' + sql_dict['table']
    if 'where' in sql_dict:
        where_conditions = []
        for i in range(len(sql_dict['where']['AND'])):
            where_conditions.append(sql_dict['where']['AND'][i]['field'] + \
            ' ' + sql_dict['where']['AND'][i]['operator'] + \
            ' ' + str(sql_dict['where']['AND'][i]['value']))
        clauses['WHERE'] = 'WHERE ' + ' AND '.join(where_conditions)
    if 'order_by' in sql_dict:
        clauses['ORDER BY'] = 'ORDER BY ' + sql_dict['order_by']['field'] + ' ' + sql_dict['order_by']['order']
    if 'limit' in sql_dict:
        clauses['LIMIT'] = 'LIMIT ' + str(sql_dict['limit'])
    query = ' '.join(clauses.values()).replace('lessthan','<')\
            .replace('greaterthan','>')\
            .replace('greaterthanorequal','>=')\
            .replace('lessthanorequal','<=')\
            .replace('notequal','!=')
    return query

print(to_sql(parse_sql(query)))