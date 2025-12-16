#!/usr/bin/python3
import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = conn.cursor()
        # ALX expects this exact string
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        return conn

    except mysql.connector.Error:
        return None


if __name__ == "__main__":
    pass
