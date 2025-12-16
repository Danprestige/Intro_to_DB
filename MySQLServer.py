#!/usr/bin/python3
import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="alx_book_store"
        )
        return conn
    except mysql.connector.Error:
        return None


if __name__ == "__main__":
    pass
