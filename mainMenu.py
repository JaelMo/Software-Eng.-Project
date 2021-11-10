import globals
import userAccounts
import blackjack

def mainMenu():

    def checkWallet():
        globals.cls()
        print("You have " + str(globals.profile.wallet) + " coins.")
        choice = input("Withdraw(1) or Add(2) funds: ")
        if choice == "1":
            userAccounts.withdrawMoney()
            print("You now have " + str(globals.profile.wallet) + " coins left")
        elif choice == "2":
            userAccounts.addMoneyToWallet()
            print("You now have " + str(globals.profile.wallet) + " coins")
        else:
            print("Please enter \"1\" or \"2\"\n")

    globals.cls()

    while True:
        if globals.profile.user_name == "guest":
            print("******************************************************************\n")
            print("Welcome to Go For Broke!\n\n")
        else:
            print("******************************************************************\n")
            print("Welcome " + globals.profile.name + "\n\n")
        
        print("Select an option:\n")
        print("1. Texas Hold'em")
        print("2. Blackjack")
        print("3. Wallet")
        print("4. Log Out")
        choice = input("Your Selection: ")
        
        if choice == "1":
            #import texasHoldem
            print("Not ready yet")
        elif choice =="2":
            blackjack.blackjack()
        elif choice == "3":
            if globals.profile.user_name == "guest":
                print("Wallet is not avaliable to guests")
                input("Press Enter key to continue...")
            else:
                checkWallet()
                input("Press Enter key to continue...")
        elif choice == "4":
            userAccounts.save()
            globals.profile = ""
            break
        else:
            print("Invalid choice\n\n")
            input("Press Enter key to continue...")
        globals.cls()
