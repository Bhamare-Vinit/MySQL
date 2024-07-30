import mysql.connector
from mysql.connector import Error

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vinit@2002'
    )

def grant_privileges(cursor, db_name, user, host, privileges):
    try:
        for priv in privileges:
            query = f"GRANT {priv} ON {db_name}.* TO '{user}'@'{host}'"
            cursor.execute(query)
        print("Privileges granted successfully.")
    except Error as e:
        print(f"Error granting privileges: {e}")

def revoke_privileges(cursor, db_name, user, host, privileges):
    try:
        for priv in privileges:
            query = f"REVOKE {priv} ON {db_name}.* FROM '{user}'@'{host}'"
            cursor.execute(query)
        print("Privileges revoked successfully.")
    except Error as e:
        print(f"Error revoking privileges: {e}")

def main():
    try:
        conn = connect_to_db()
        if conn.is_connected():
            print("Connected to MySQL server")

            cursor = conn.cursor()
            action = input("Do you want to do with vinit?\n1. Grant access\n2. Revoke access\nEnter(1 or 2): ")

            if action == '1':
                print("Available Databases:")
                cursor.execute("SHOW DATABASES")
                databases = cursor.fetchall()
                print("Databases:")
                for db in databases:
                    print(db[0])
                db_name = input("Enter the database name: ").strip()
                user = 'vinit'
                host = 'localhost'
                privileges = input("Enter the privileges to grant (comma-separated, e.g., SELECT, INSERT, UPDATE): ").strip().upper().split(',')
                privileges = [priv.strip() for priv in privileges]
                
                grant_privileges(cursor, db_name, user, host, privileges)

            elif action == '2':
                print("Available Databases:")
                cursor.execute("SHOW DATABASES")
                databases = cursor.fetchall()
                print("Databases:")
                for db in databases:
                    print(db[0])
                db_name = input("Enter the database name: ").strip()
                user = 'vinit'
                host = 'localhost'
                privileges = input("Enter the privileges to revoke (comma-separated, e.g., SELECT, INSERT, UPDATE): ").strip().upper().split(',')
                privileges = [priv.strip() for priv in privileges]

                revoke_privileges(cursor, db_name, user, host, privileges)

            else:
                print("Invalid action. Please choose 'grant' or 'revoke'.")

            conn.commit()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    main()
