"""
This file is the landing page for the project
"""

import globals
import mainMenu
import userAccounts

while True:
    print("WELCOME")
    print("\nPlease choose one of the following:")
    print("1. Login")
    print("2. Create Account")
    print("3. Continue as Guest (Guests cannot cashout or add funds)")
    print("4. Exit")
    choice = input("Your Selection: ")
    if choice == "1":
        userAccounts.login()
        if globals.profile != "back":
            mainMenu.mainMenu()
    elif choice == "2":
        userAccounts.createAccount()
        if globals.profile != "back":
            mainMenu.mainMenu()
    elif choice == "3":
        globals.profile = globals.Profile("guest", "password", "Guest", "0", "0", 50)
        mainMenu.mainMenu()
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice\n\n")
        input("Press Enter key to continue...")
    globals.cls()
    
