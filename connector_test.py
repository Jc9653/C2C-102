import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'example',
    password = 'Cv@#nmDg%!8'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM bankaccounts")
cursor.execute(testQuery)

for item in cursor:
    print(item)


cursor.close()
connection.close()

