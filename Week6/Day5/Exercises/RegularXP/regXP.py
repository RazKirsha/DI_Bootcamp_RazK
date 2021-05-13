import psycopg2


class MenuItem:

    def __init__(self, name='a', price='0'):
        self.name = name
        self.price = price

    def save(self):
        query = f"insert into dishes(name,price) values ('{self.name}',{self.price})"
        return self.run_sql(query)

    def delete(self, name):
        query = f"delete from dishes where name = '{name}'"
        return self.run_sql(query)

    def update(self, name):
        new_price = int(input('Enter a new price: '))
        query = f"update dishes set  price = {new_price} where name = '{name}'"
        return self.run_sql(query)

    @classmethod
    def all(cls):
        query = 'select * from dishes'
        results = cls.run_sql(query, 'get')
        for id, item, price in results:
            print(f'dish: {item}, price: {price}')

    @staticmethod
    def run_sql(query, type='post'):
        HOSTNAME = '127.0.0.1'
        USERNAME = 'postgres'
        PASSWORD = 'Lala1421'
        DATABASE = 'menu'
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        if type == 'get':
            results = cursor.fetchall()
            connection.close()
            return results
        connection.close()
