import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'example',
    password = 'Cv@#nmDg%!8'
)

cursor = connection.cursor()

#green code below was some testing to see what works and what doesn't
#addData = ("INSERT INTO bankaccounts(UserName, Password, Balance)VALUES('bimmy', '123Password', 520.3)")
#cursor.execute(addData)
#cursor.execute("UPDATE bankaccounts SET Balance = (balance + 50) WHERE id = 6")
#cursor.execute("SELECT * FROM bankaccounts")
#cursor.execute("SELECT Balance FROM bankaccounts WHERE id = 6") 
#for item in cursor:
    #print(item)
#connection.commit()
#cursor.close()
#connection.close()







#adds an account to data base
def addAccount(username, password, balance):
    addQuery = ("INSERT INTO bankaccounts (UserName, Password, Balance) VALUES ( '"+ username + "', '" + password + "', " + str(balance) + ")")
    cursor.execute(addQuery) 
    connection.commit()
#deletes account from database
def deleteAccount(username, password):
    deleteQuery = ("DELETE FROM bankaccounts WHERE UserName = '" + username + "' AND Password = '" + password + "'")
    cursor.execute(deleteQuery)
    connection.commit()
    print("Account Deleted")

#Adds money to account balance
def Deposit(username, password, amount):
    cursor.execute("UPDATE bankaccounts SET Balance = (balance + " + str(amount) + ") WHERE UserName = '" + username + "' AND Password = '" + password + "'")
    connection.commit()

#widthdraws money from account balance
def Withdraw(username, password, amount):
    cursor.execute("UPDATE bankaccounts SET Balance = (balance -" + str(amount) + ") WHERE UserName = '" + username + "' AND Password = '" + password + "'")
    connection.commit()

#Allows user to edit account
def editAccount(username, password, choice):
    #choice determines whether to change password or username
    if(choice == "p"):
        newPassword = input("What is your new Password: ")
        cursor.execute("UPDATE bankaccounts SET Password = '" + newPassword + "' WHERE UserName = '" + username + "' AND Password = '" + password + "'")
        connection.commit()
        return newPassword
    elif(choice == "n"):
        newUsername = input("What is your new UserName: ")
        cursor.execute("UPDATE bankaccounts SET UserName = '" + newUsername + "' WHERE UserName = '" + username + "' AND Password = '" + password + "'")
        connection.commit()
        return newUsername
#allows user to view account details including balance
def viewAccountDetails(username, password):
    cursor.execute("SELECT * FROM bankaccounts WHERE UserName = '" + username + "' AND Password = '" + password + "'")
    for item in cursor:
        print(item)
    print("(account id, userName, password, balance)")
    input("Enter to continue")

    