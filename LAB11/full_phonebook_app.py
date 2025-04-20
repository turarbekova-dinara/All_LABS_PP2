import psycopg2
import csv
from tabulate import tabulate 

# Дерекқормен байланыс
conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="181124",
    port=5432
)

cur = conn.cursor()

# Мұнда CREATE TABLE жоқ, себебі кесте pgAdmin-да дайын болуы керек

def insert_data():
    print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("INSERT INTO PhoneBook111 (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter a file path with proper extension: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Header жолын өткізіп жіберу
            for row in reader:
                cur.execute("INSERT INTO PhoneBook111 (name, surname, phone) VALUES (%s, %s, %s)", tuple(row))
    conn.commit()

def update_data():
    column = input('Type the name of the column that you want to change: ')
    value = input(f"Enter {column} that you want to change: ")
    new_value = input(f"Enter the new {column}: ")
    cur.execute(f"UPDATE PhoneBook111 SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()

def delete_data():
    phone = input('Type phone number which you want to delete: ')
    cur.execute("DELETE FROM PhoneBook111 WHERE phone = %s", (phone,))
    conn.commit()
    
def query_data():
    column = input("Type the name of the column which will be used for searching data: ")
    value = input(f"Type {column} of the user: ")
    cur.execute(f"SELECT * FROM PhoneBook111 WHERE {column} = %s", (value,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))

def display_data():
    cur.execute("SELECT * from PhoneBook111;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

while True:
    print("""
    List of the commands:
    1. "i/I" - INSERT data to the table.
    2. "u/U" - UPDATE data in the table.
    3. "q/Q" - make specific QUERY in the table.
    4. "d/D" - DELETE data from the table.
    5. "s/S" - see the values in the table.
    6. "f/F" - close the program.
    """)

    command = input().lower()

    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        query_data()
    elif command == "s":
        display_data()
    elif command == "f":
        break

cur.close()
conn.close()
