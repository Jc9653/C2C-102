import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'example',
    password = 'Cv@#nmDg%!8'
)

cursor = connection.cursor()
#addData = ("INSERT INTO bankaccounts(UserName, Password, Balance)VALUES('bimmy', '123Password', 520.3)")

#cursor.execute(addData)


#connection.commit()
cursor.execute("UPDATE bankaccounts SET balance = (balance + 50) WHERE id = 6")
#cursor.execute("SELECT * FROM bankaccounts")
cursor.execute("SELECT balance FROM bankaccounts WHERE id = 6") 


for item in cursor:
    print(item)


cursor.close()
connection.close()





#adds an account to data base
def addAccount(userName, password, balance):
    addQuery = ("INSERT INTO bankaccounts (UserName, Password, Balance) VALUES (" + userName + ", " + password + ", " + str(balance) + ")")
    cursor.execute(addQuery) 
    connection.commit()
#deletes account from database
def deleteAccount(id):
    deleteQuery = ("DELETE FROM bankaccounts WHERE ID = " + str(id))
    cursor.execute(deleteQuery)
    print("Account Deleted")

#Adds money to account balance
def Deposit(id, amount):
    cursor.execute("UPDATE bankaccounts SET balance = (balance +" + str(amount) + ") WHERE id = " + str(id))

#widthdraws money from account balance
def Withdraw(id, amount):
    cursor.execute("UPDATE bankaccounts SET balance = (balance -" + str(amount) + ") WHERE id = " + str(id))

#prints the balance
def ViewBalance(id):
    cursor.execute("SELCET balance FROM bankaccounts WHERE id = " + str(id))
    for item in cursor:
        print(item)

def GetIdNum(username):
    return cursor.execute("SELECT id FROM bankaccounts WHERE UserName = " + username)
    