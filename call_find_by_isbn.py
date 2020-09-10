from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def call_find_by_isbn():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        # Since this stored procedure requires 2 arguments, yet you
        # have to invoke stored_results() on it to get the result set,
        # you put 0 on the second element of the args list.
        # (where the result variable would usually go)


        #  The second element of the args list (0) 
        #  is just a placeholder to hold the p_title parameter.
        args = ['1236400967773', 0]
        result_args = cursor.callproc('find_by_isbn', args)

        print(result_args[1])

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

# The  callproc() method returns a list ( result_args ) 
# that contains two elements: the second element (result_args[1]) 
# holds the value of the  p_title parameter.


if __name__ == '__main__':
    call_find_by_isbn()