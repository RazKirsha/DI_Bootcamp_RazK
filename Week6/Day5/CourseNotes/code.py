# importing the database library - pgamdin
import psycopg2
# importing the database library to get the column names -pgamdin
import psycopg2.extras

# setting up the connection
# IP of program (?)
HOSTNAME = '127.0.0.1'
# user name
USERNAME = 'postgres'
# my password
PASSWORD = 'Lala1421'
# name of a database
DATABASE = 'dvdrental'

# setting up the connection using our data from above
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

# opening a query window
# cursor = connection.cursor()

# getting the data and their type
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# this is the query
query = "SELECT * FROM film order by film_id limit 10"

# execute this query
cursor.execute(query)

# appending it to results
results = cursor.fetchall()

# closing the connection
connection.close()

# now the database is in "results" as a list of tupples
# looping through the list to get each row
for item in results:
    print(item)

print('BREAK!!!!')
# getting the first row of the list
print(results[0])
