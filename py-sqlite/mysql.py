import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myusername",
    password="mypassword",
    database="mydatabase"
)

print(mydb)


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASE")

for x in mycursor:
    print(x)


mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREENT PRIMARY KEY")

