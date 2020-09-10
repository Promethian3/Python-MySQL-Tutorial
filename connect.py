'''
This example is very crude, just to get an idea 
of how we're supposed to use the mysql.connector object
to connect to the database.

Preferably, we would like to actually connect using a config file.
'''

import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect( host='localhost', 
                                        database='python_mysql',
                                        user='testuser', 
                                        password='mypassword')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()