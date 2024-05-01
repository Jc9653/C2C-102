import connector_test
run = True
signedIn = False
UserChoice = ""
#menu for account page
def accountPage(username, password):
    while signedIn:
        print("-------------------------")
        print("1 --View Balance")
        print("2 --Deposit")
        print("3 --Widthdraw")
        print("4 --Sign Out")
        print("-------------------------")
        print("")

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
        print("You have Created an account")
        print(connector_test.GetIdNum(username))
        signedIn = True
    elif(UserChoice == "2"):
        username = input("Enter A UserName: ")
        password = input("Enter A Password: ")
        signedIn = True
        print("You are now Sign In")
    elif(UserChoice == "3"):
        run = False


