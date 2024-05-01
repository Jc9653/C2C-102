#imported just in case seems to work
import mysql.connector
#importing connector_test in order to get functions
import connector_test

#global variables
run = True
signedIn = False
UserChoice = ""

#menu for account page
def accountPage(username, password):
    global signedIn
    while signedIn:
        print("-------------------------")
        print("1 --Deposit")
        print("2 --Widthdraw")
        print("3 --Delete Account")
        print("4 --Edit Account")
        print("5 --View Account Details")
        print("6 --Sign Out")
        print("-------------------------")
        print("")

        #code for user choosing account options
        userchoice = input("Select a choice(1-6): ")
        if(userchoice == "1"):
            amount = float(input("How much would you like to deposit: "))
            connector_test.Deposit(username, password, amount)
        elif(userchoice == "2"):
            amount = float(input("How much would you like to widthdraw: "))
            connector_test.Withdraw(username, password, amount)
        elif(userchoice == "3"):
            connector_test.deleteAccount(username, password)
        elif(userchoice == "4"):
            choice = input("Would you like to change UserName(n) or Password(p): ")
            
            if(choice == "p"):
                password = connector_test.editAccount(username, password, choice)
            elif(choice == "n"):
                username = connector_test.editAccount(username, password, choice)
        elif(userchoice =="5"):
            connector_test.viewAccountDetails(username, password)
        elif(userchoice == "6"):
            signedIn = False
        

#While loop used to keep code running
while run:
    
    #menu Screen
    print("Welcome User")
    print("What Would You Like to Do:")
    print("-------------------------")
    print("1 --Create Account")
    print("2 --Sign In")
    print("3 --Exit")
    print("-------------------------")
    print("")

    #code for Options the User can make
    UserChoice = input("Select Option(1-3): ")
    if(UserChoice == "1"):
        username = input("Enter A UserName: ")
        password = input("Enter A password: ")
        balance = input("Enter Initial Balance: ")
        connector_test.addAccount(username, password, balance)
        print("You have Created an account")
        signedIn = True
        accountPage(username, password)
    elif(UserChoice == "2"):
        username = input("Enter A UserName: ")
        password = input("Enter A Password: ")
        signedIn = True
        accountPage(username, password)
        print("You are now Sign In")
    elif(UserChoice == "3"):
        run = False



