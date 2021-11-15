sql_dict = {
   'fields': [
      'name', 
      'model', 
      'price'
   ],
   'table': 'Products',
   'where': {
      'AND': [
      	 {
            'field': 'make',
            'value': '%Apple%',
            'operator': 'LIKE'
         },
         {
            'field': 'price',
            'value': 1100.00,
            'operator': 'lessthan'
         }
      ]
   },
   'order_by': {
      'field': 'price',
      'order': 'DESC'
   },
   'limit': 0
}

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

print(to_sql(sql_dict))