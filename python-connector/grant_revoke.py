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
        print("Access granted")

        conn.commit()

        try:
            test_conn = mysql.connector.connect(
                host='localhost',
                user='vinit',
                password='Vinit@2002', 
                database='workbench'
            )

            if test_conn.is_connected():
                print("Connected as 'vinit' to check SELECT privilege")

                test_cur = test_conn.cursor()
                test_cur.execute("SELECT 1 FROM DUAL;")
                test_cur.fetchone()

                print("Access verification succeeded: SELECT privilege is granted")
                test_cur.close()
                test_conn.close()

        except Error as test_error:
            print(f"Access verification failed: {test_error}")

except Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
        print("MySQL connection is closed")
