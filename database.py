import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'testdb',
    )

my_cursor = mydb.cursor()

# create a database 
# my_cursor.execute('CREATE DATABASE testdb')

# show database
# my_cursor.execute('SHOW DATABASES')
# for db in my_cursor:
#     print(db[0])


# create table
# my_cursor.execute('CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY key)')
# my_cursor.execute('SHOW TABLES')
# for table in my_cursor:
#     print(table[0])

sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ('Daniel4', 'daniel4@zmail.com', 47)
print(sqlStuff, record1)

my_cursor.execute(sqlStuff, record1)
mydb.commit()