table_name = 'store' # we created in pgAdmin4

def read_all_queries():
    return f'SELECT * FROM {table_name}'

def create_row_query(data_list:list): # i.e ["'banana'", 5, 100] because we want 'banana'
    string_values = ', '.join(map(str, data_list))
    print(string_values)
    return f'''
    INSERT INTO {table_name}
    VALUES ({string_values});
'''

def update_row_query(column_value_pair, filter_expression):
    return f'''
    UPDATE {table_name}
    SET {column_value_pair}
    WHERE {filter_expression}; # "name = 'banana'" sql may think its variable if not quoted

'''

def delete_rows_query(filter_expression):
    return f'''
    DELETE FROM {table_name}
    WHERE {filter_expression};
'''