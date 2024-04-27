import psycopg2
import csv
from config import load_config
def main():
    connection = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password= "Lolkek3103"
    )
    on=True
    mode='ASC'
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS phonebook(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(20) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
        ) """)
    while on:
        a=int(input("type:\n 1-add,\n2-delete,\n3-edit,\n4-look,\n5-clear book,\n6-resort,\n7-import from scv, \n8 pattern search, \n9 insert new user or phone, \n10 delete data, \n:"))
        if a == 1:
            name_to_insert=input("enter name: ")
            number_to_insert=input("enter phone number: ")
            with connection.cursor() as cursor:
                cursor.execute(f"""INSERT INTO phonebook(first_name,phone_number)
                VALUES ('{name_to_insert}','{number_to_insert}')""")
        elif a == 4:
            with connection.cursor() as cursor:
                if mode=='ASC':
                    cursor.execute(f"""SELECT * FROM phonebook ORDER BY first_name ASC""")
                if mode=='DESC':
                    cursor.execute(f"""SELECT * FROM phonebook ORDER BY first_name DESC""")
                all=cursor.fetchall()
                for _,name,phone in all:
                    print("|"+name+"---"+phone+"|")
        elif a == 2:
            
            name_to_delete=input("enter to delete: ")
            with connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM phonebook WHERE first_name = '{name_to_delete}' OR phone_number='{name_to_delete}'")
        elif a == 3:
            editing_name=input("what contact you will edit?: ")
            new_name=input("new name: ")
            new_number=input("new phone number: ")
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE phonebook SET first_name='{new_name}' WHERE first_name='{editing_name}'")
                cursor.execute(f"UPDATE phonebook SET phone_number='{new_number}' WHERE first_name='{new_name}'")
        elif a == 5:
            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE phonebook;")
        elif a ==6:
            mode_change=input("1-by alphabetical,2-by inverse alphabetical")
            if mode_change=='1':
                mode='ASC'
            else:
                mode='DESC'
        elif a == 7:
            path=input("give path,NOT RELATIVE")

            with open(path, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='|',)
                for row in spamreader:
                     with connection.cursor() as cursor:
                        cursor.execute(f"""INSERT INTO phonebook(first_name,phone_number)
                        VALUES ('{row[0]}','{row[1]}')""")
        elif a == 8:
            pattern = input("Enter the search pattern: ")
            query = """
            SELECT * FROM phonebook
            WHERE first_name ILIKE %s
            OR phone_number ILIKE %s
            """

            print("Executing query:", query)
            print("Pattern:", pattern)

            with connection.cursor() as cursor:
                try:
                    cursor.execute(query, (f"%{pattern}%", f"%{pattern}%"))
                    matching_records = cursor.fetchall()
                    if matching_records:
                        print("Matching records:")
                        for record in matching_records:
                            print(record)
                    else:
                        print("No matching records found.")
                except Exception as e:
                    print("An error occurred:", e)
        if a==9:
            new_user=input("enter new user: ")
            new_phone=input("enter new phone: ")
            with connection.cursor() as cursor:
                try:
                    cursor.callproc('insert_or_update_user', (new_user, new_phone))
                    connection.commit()
                    print("Procedure executed successfully!")
                except (Exception, psycopg2.DatabaseError) as error:
                    print("Error while executing procedure:", error)
        if a == 10:
            delete_user = input("Enter username to delete: ")
            delete_phone = input("Enter phone number to delete: ")
            with connection.cursor() as cursor:
                try:
                    cursor.execute("CALL delete_phone_or_user(%s, %s)", (delete_user, delete_phone))
                    connection.commit()
                    print("Procedure executed successfully!")
                except (Exception, psycopg2.DatabaseError) as error:
                    print("Error while executing procedure:", error)


    connection.close()

if __name__ == '__main__':
    main()