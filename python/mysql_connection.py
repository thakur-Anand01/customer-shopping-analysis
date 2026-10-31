
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=input("Enter your MySQL root password: ")
    )

    if connection.is_connected():
        print("Successfully connected to MySQL!")

        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()

        print("MySQL version:", version[0])

        cursor.execute("SHOW DATABASES")
        print("\nAvailable databases:")
        for database in cursor.fetchall():
            print(database[0])

        cursor.close()

except Error as e:
    print("MySQL connection failed:", e)

finally:
    if "connection" in locals() and connection.is_connected():
        connection.close()
        print("\nConnection closed.")
