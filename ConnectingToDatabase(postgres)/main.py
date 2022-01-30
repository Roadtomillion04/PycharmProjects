import psycopg2
# we need psycopg2 to connect to a database
from queries import * # script that contains queries


# to establish a connection
con = psycopg2.connect(
    user = 'postgres', # by default
    password = '123456',
    host = '127.0.0.1', # its default for all computers its just refers local host
    port = '5432', # default
    database = 'postgres' # just name of the service
)

# to check its connected
#print(con.closed) # if 0 its connected
# as we are closing
#con.close()
#print(con.closed) # if 1 its not connected

cur = con.cursor() # cursor is a temp memory allocated by database it is response to represent data properly
cur.execute(create_row_query(["'orange'", 3, 200])) # query
#cur.execute(update_row_query(
#    column_value_pair = "quantity = 50",
#    filter_expression = "name = 'banana'"
#)) # query
cur.execute(delete_rows_query(filter_expression = "name = 'apple'")) # query
cur.execute(read_all_queries()) # query
print(cur.fetchall()) # grabs all data

con.commit() # it makes sure all the change we did are persistent
# finally after performing all tasks we don't want in memory
cur.close()
con.close()
