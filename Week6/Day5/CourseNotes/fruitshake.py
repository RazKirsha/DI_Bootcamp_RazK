import sqlite3
from tabulate import tabulate


def order():
    choice = None
    while choice != "x":
        print("Moti's Fruit Shake Stand with questionable hygiene")
        inv = get_inv()
        print(tabulate(inv, headers=['Fruit', 'Amount']))
        choice = input("What do you want to add to your shake?")
        update_inv(choice)
    else:
        print("Bye")


def update_inv(choice):
    query = f"UPDATE fruits SET quantity=quantity-1 WHERE fruit = '{choice}';"
    return run_query(query)


def get_inv():
    query = "SELECT fruit, quantity FROM fruits ORDER BY fruit ASC;"
    return run_query(query)


# this is connecting to the SQLite
def run_query(query):
    connection = sqlite3.connect("first_db.db")
    cursor = connection.cursor()
    cursor.execute(query)
    # applying changes to original database
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results


order()
