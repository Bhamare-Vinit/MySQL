import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',      
        user='root',   
        password='Vinit@2002'
    )

    if conn.is_connected():
        print("Connected to MySQL server")

        cur = conn.cursor()

        cur.execute("SHOW DATABASES")

        databases = cur.fetchall()
        for db in databases:
            print(db)

        database_name = 'Workbench'

        cur.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = cur.fetchone()

        if result:
            print(f"Database '{database_name}' already exists.")
        else:
            cur.execute(f"CREATE DATABASE `{database_name}`")
            print(f"Database '{database_name}' created successfully.")

        conn.commit()

except Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
        print("MySQL connection is closed")
