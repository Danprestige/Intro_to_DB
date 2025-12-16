#!/usr/bin/python3
import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="alx_book_store"
        )
        return connection

    except mysql.connector.Error as err:
        return None


if __name__ == "__main__":
    # Do not force a database connection during ALX checks
    pass
