import sqlite3 as sl
from faker import Faker
from time import time

f = Faker()
connection = sl.connect("fake_data3.db")

cursor = connection.cursor()

start = time()

for i in range(100):
    query = f"insert into people(name,email) values ('{f.name()}','{f.email}')"
    cursor.execute(query)

connection.commit()

connection.close()

end = time()

print(end - start)
