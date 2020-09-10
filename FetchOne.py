from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


"""
1. First, connect to the database by creating a new  MySQLConnection object
2. Next, instantiate a new  MySQLCursor object from the  MySQLConnection object
3. Then, execute a query that selects all rows from the books table.
4. After that, fetch the next row in the result set  by calling the fetchone(). In the  while loop block, display the contents of the row and move to the next row until all rows are fetched.
5. Finally, close both cursor and connection objects by invoking the  close() method of the corresponding object.
"""

def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchone()