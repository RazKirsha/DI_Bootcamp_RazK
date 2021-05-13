import psycopg2
import requests
import random


def run_sql(query, type='get'):
    HOSTNAME = '127.0.0.1'
    USERNAME = 'postgres'
    PASSWORD = 'Lala1421'
    DATABASE = 'countries'
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    if type == 'get':
        results = cursor.fetchall()
        connection.close()
        return results
    connection.close()


resp = requests.get('https://restcountries.eu/rest/v2/all')
resp = resp.json()
random.shuffle(resp)

for i in range(10):
    country = resp[i]['name']
    capital = resp[i]['capital']
    flag = resp[i]['flag']
    subregion = resp[i]['subregion']
    population = resp[i]['population']

    query = f"""
    insert into country(name, capital, flag, subregion, population)
    values
    ('{country}','{capital}','{flag}','{subregion}',{population})
    """
    run_sql(query, 'post')

query = 'select * from country'
print(run_sql(query, 'get'))
