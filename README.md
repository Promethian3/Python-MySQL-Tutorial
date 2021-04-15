# Python-MySQL Tutorial

## Prerequisites

You must have:

* Python 3.6+
* MySQL 8.0+: [Page](https://www.mysql.com/)
* Have a MySQL user '`testuser`' with password '`mypassword`'
* Knowledge in Python's virtualenv (venv). If you don't, follow the Installing virtualenv, Creating a virtual environment, Activating a virtual environment, and Leaving a virtual environment sections in the following [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* Knowledge with pip installations. If you don't, just follow the related sections in the link above.

There are more pointers about the repo on this file's `Notes` section.

## MySQL Connector/Python versions

Since we're all using Python 3.6+ and I personally got MySQL8.0:

Connector/Python Version | MySQL Server Versions | Supported Python Versions
------------------------ | --------------------- | --------------------------
8.0 | 8.0, 5.7, 5.6, 5.5 | 3.6, 3.5, 3.4, 2.7

To install the MySQL Python connector, simply run:

`pip install mysql-connector-python`

If the installation fails, try running this one instead:

`pip install mysql-connector-python==8.0.17`

To verify installation, open up IDLE, and run the following code:

```python
>>> import mysql.connector
>>> mysql.connector.connect(host='localhost',database='mysql',user='testuser',password='mypassword')
```

## Connecting to MySQL Database

Related Files:

* [connect.py](connect.py)
* [config.ini](config.ini)
* [python_mysql_dbconfig.py](python_mysql_dbconfig.py)
* [connect2.py](connect2.py)

Follow the instructions in [this](https://www.mysqltutorial.org/python-connecting-mysql-databases/) link.

## Querying

Related Files:

* [FetchOne.py](FetchOne.py)
* [FetchAll.py](FetchAll.py)
* [FetchMany.py](FetchMany.py)

To query data in a MySQL database from Python, you need to do the following steps:

1. Connect to the MySQL Database, you get a `MySQLConnection` object.
2. Instantiate a  `MySQLCursor` object from the the `MySQLConnection` object.
3. Use the cursor to execute a query by calling its `execute()` method.
4. Use `fetchone()`, `fetchmany()` or `fetchall()` method to fetch data from the result set.
5. Close the cursor as well as the database connection by calling the `close()` method of the corresponding object.

## Inserting

Related Files:

* [InsertOne.py](InsertOne.py)
* [InsertMany.py](InsertMany.py)

To insert new rows into a MySQL table, you follow these steps:

1. Connect to the MySQL database server by creating a new `MySQLConnection` object.
2. Initiate a `MySQLCursor` object from the `MySQLConnection` object.
3. Execute the `INSERT` statement to insert data into the table and commit the change.
4. Close the database connection.

## Updating

Related Files:

* [Updating.py](Updating.py)

To update data in a MySQL table in Python, you follow these steps:

1. Connect to the database by creating a new `MySQLConnection` object.
2. Create a new `MySQLCursor` object from the `MySQLConnection` object and call the `execute()` method of the `MySQLCursor` object. To accept the changes, you call the `commit()` method of the `MySQLConnection` object after calling the `execute()` method. Otherwise, no changes will be made to the database.
3. Close the cursor and database connection.

## Deleting

Related Files:

* [Deleting.py](Deleting.py)

To delete data from a table from a Python program, you follow these steps:

1. Connect to the database by creating a new `MySQLConnection` object.
2. Instantiate a new cursor object and call its `execute()` method. To commit the changes, you should always call the `commit()` method of the `MySQLConnection` object after calling the `execute()` method.
3. Close the cursor and database connection by calling `close()` method of the corresponding objects.

## Stored Procedures

Related Files:

* [find_all.sql](find_all.sql)
* [find_by_isbn.sql](find_by_isbn.sql)
* [call_find_all_sp.py](call_find_all_sp.py)
* [call_find_by_isbn.py](call_find_by_isbn.py)

To call a stored procedure in Python, you follow the steps below:

1. Connect to the database by creating a new `MySQLConnection` object.
2. Instantiate a new `MySQLCursor` object from the `MySQLConnection` object by calling the `cursor()` method.
3. Call  `callproc()` method of the `MySQLCursor` object. You pass the stored procedure’s name as the first argument of the  `callproc()` method. If the stored procedure requires parameters, you need to pass a list as the second argument to the  `callproc()` method. In case the stored procedure returns a result set, you can invoke the  `stored_results()` method of the `MySQLCursor` object to get a list iterator and iterate this result set by using the  `fetchall()` method.
4. Close the cursor and database connection as always.

Notice how in the two related python files: `call_find_all_sp.py` and `call_find_by_isbn.py` we don't actually write the stored procedures. We simply used the python files to call on those two already existing stored procedures. This means we have to actually define those stored procedures on the `MySQL Workbench` or in the `MySQL Shell`/ `shell` application directly.

## Updating BLOB data in Python

Related Files:

* [UpdateBLOB.py](UpdateBLOB.py)

A walk through the code:

1. First, we call the `read_file()` function to read data from a file and return it.
2. Second, we compose an `UPDATE` statement that updates photo column for an author specified by `author_id`. The  args variable is a tuple that contains file data and `author_id`. We will pass this variable to the  `execute()` method together with the query .
3. Third, inside the `try except` block, we connect to the database, instantiate a cursor, and execute the query with `args`. To make the change effective, we call `commit()` method of the `MySQLConnection` object.
4. Fourth, we close the cursor and database connection in the `finally` block.

## Reding BLOB data in Python

Related Files:

* [ReadBLOB.py](ReadBLOB.py)

A walk through the code:

1. First, compose a `SELECT` statement that retrieves the photo of a specific author.
2. Second, get the database configuration by calling the `read_db_config()` function.
3. Third, connect to the database, instantiate cursor, and execute the query. Once receiving the BLOB data, we use the `write_file()` function to write it into a file specified by the `filename`.
4. Finally, close the cursor and database connection.

### Notes

* __Unrelated__ to the tutorial, but still __important__: Make sure to `activate` the environment before running any of the files, and `deactivate` it when you're done with the files.
* You should always use `commit()` after calling the `execute()` to make sure that the change on your table or database persists.
* You should always use placeholders inside any query that you pass to the `execute()` method. This helps you avoid a __SQL injection__.

__Original Tutorial was found [here](https://www.mysqltutorial.org/python-mysql/)__
