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

        cur.execute("GRANT SELECT ON workbench.* TO 'vinit'@'localhost';")

        conn.commit()

except Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
        print("MySQL connection is closed")
