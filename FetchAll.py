from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

"""
This is very similar to the fetchone() method except it loads
all the data into memory, which you probably wouldn't want unless
you know that you don't have that many entries. 
"""

def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchall()