import sqlite3 as sl
from time import time
import requests

connection = sl.connect('jokes.db')

cursor = connection.cursor()
start = time()
for i in range(100):
    data = requests.get('https://api.chucknorris.io/jokes/random')
    data = data.json()
    joke = data['value']
    joke = joke.replace('"', '`')
    joke = joke.replace("'", '`')
    query = f"insert into jokes(joke) values ('{joke}')"


cursor.execute(query)

connection.commit()

connection.close()

end = time()

print(end - start)
