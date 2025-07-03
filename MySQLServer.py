#!/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode

DB_NAME = "alx_book_store"

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2001"  # ← Change this to your actual root password
        )
        cursor = connection.cursor()

        # Try to create the database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Always clean up
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

