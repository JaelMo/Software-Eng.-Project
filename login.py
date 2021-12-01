"""
This file is the landing page for the project
"""

import globals
import userAccounts
import tkinter as tk
from tkinter.constants import END
import sqlite3 as sl
from functools import partial

userDB = sl.connect('userDB.db')
try:
    with userDB:
        userDB.execute("""
        CREATE TABLE user_account (
            user_name TEXT NOT NULL PRIMARY KEY,
            password TEXT NOT NULL,
            name TEXT,
            bank_account_number TEXT,
            drivers_license_number TEXT,
            wallet INTEGER
        );
    """)
except:
    print("db exists")
globals.cls()  

"""******************************************************************************************************************
loadMainMenu
    responsible for loading the main login menu and defining the functions of the buttons within
******************************************************************************************************************"""
def loadMainMenu():

    def guestFunc():
        globals.profile = ("guest", 50)
        loadGameMenu()

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    image2 = tk.PhotoImage(master=frame, file='images/createAccount.png')
    image2 = image2.subsample(7, 7)
    createAccountButton = tk.Button(frame, image=image2, command=loadCreateAccount)
    createAccountButton.config(width=75, height=75)
    createAccountButton.pack(side="top", anchor="ne")
    

    titleLabel = tk.Label(frame, image=image, text = "Go For Broke", compound=tk.CENTER, width=800, height=100)
    titleLabel.config(font=("Bernard MT Condensed", 50))
    titleLabel.pack(side="top", pady=100)

    loginButton = tk.Button(frame, text="Login", command=loadLoginWindow)
    loginButton.config(width = 15, height = 2, font=30)
    loginButton.pack(side="left", expand=True)

    guestButton = tk.Button(frame, text="Play As Guest", command=guestFunc)
    guestButton.config(width = 15, height = 2, font=30)
    guestButton.pack(side="right", expand=True)

    frame.pack(fill="both", expand=True)

    globals.window.mainloop()

"""******************************************************************************************************************
loadCreateAccount
    responsible for loading the create account screen and defining the functions of it's buttons
******************************************************************************************************************"""
def loadCreateAccount():
    globals.clearWindow()

    def back():
        globals.clearWindow()
        loadMainMenu()

    def getUserName(userName):
        with userDB:
            cursor = userDB.cursor()
            count = cursor.execute("SELECT COUNT(*) FROM user_account WHERE user_name = ?", (userName,))
            count = cursor.fetchone()[0]
            if count > 0:
                return False
            else:
                return True

    def submitCreateAccount(): 
        user_name = userNameField.get("1.0", END)
        password = passwordField.get("1.0", END)
        name = nameField.get("1.0", END)
        bank_account = bankNumberField.get("1.0", END)
        drivers_license_number = driverField.get("1.0", END)
        if not getUserName(user_name):
            errorLabel.pack(pady=(1,100))
        else:
            password = passwordField.get("1.0", END)
            name = nameField.get("1.0", END)
            bank_account = bankNumberField.get("1.0", END)
            drivers_license_number = driverField.get("1.0", END)
            if userAccounts.createAccount(user_name, password, name, bank_account, drivers_license_number):
                loadGameMenu()


 
    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    image2 = tk.PhotoImage(master=frame, file='images/back.png')
    image2 = image2.subsample(7, 7)
    backButton = tk.Button(frame, image=image2, command=back)
    backButton.config(width=75, height=75)
    backButton.pack(side="top", anchor="nw")

    userNameLabel = tk.Label(frame, text="User Name", image=image, compound=tk.CENTER, height=20, width=200)
    userNameLabel.config(font=("Areial bold", 18))
    userNameLabel.pack(pady=(30,5))
    userNameField = tk.Text(frame, height = 1, width = 20)
    userNameField.config(font=18)
    userNameField.pack(pady=(5,15))

    passwordLabel = tk.Label(frame, text="Password", image=image, compound=tk.CENTER, height=20, width=200)
    passwordLabel.config(font=("Areial bold", 18))
    passwordLabel.pack(pady=(30,5))
    passwordField = tk.Text(frame, height = 1, width = 20)
    passwordField.config(font=18)
    passwordField.pack(pady=(5,15))

    nameLabel = tk.Label(frame, text="Name", image=image, compound=tk.CENTER, height=20, width=200)
    nameLabel.config(font=("Areial bold", 18))
    nameLabel.pack(pady=(30,5))
    nameField = tk.Text(frame, height = 1, width = 20)
    nameField.config(font=18)
    nameField.pack(pady=(5,15))

    bankLabel = tk.Label(frame, text="Bank Number", image=image, compound=tk.CENTER, height=20, width=200)
    bankLabel.config(font=("Areial bold", 18))
    bankLabel.pack(pady=(30,5))
    bankNumberField = tk.Text(frame, height = 1, width = 20)
    bankNumberField.config(font=18)
    bankNumberField.pack(pady=(5,15))

    driverLabel = tk.Label(frame, text="Driver's License Number", image=image, compound=tk.CENTER, height=20, width=300)
    driverLabel.config(font=("Areial bold", 18))
    driverLabel.pack(pady=(30,5))
    driverField = tk.Text(frame, height = 1, width = 20)
    driverField.config(font=18)
    driverField.pack(pady=(5,15))

    submitButton = tk.Button(frame, text="Submit", command=submitCreateAccount, height=1, width=20)
    submitButton.config(font=("Areial bold", 18))
    submitButton.pack(pady=50)

    errorLabel = tk.Label(frame, text="User Name Invalid", image=image, compound=tk.CENTER, height=20, width=300)
    errorLabel.config(font=("Areial bold", 18))
    
    frame.pack(fill="both", expand=True)
    globals.window.mainloop()

"""******************************************************************************************************************
loadLoginWindow
    responsible for loading the login screen and defining the function of it's buttons
******************************************************************************************************************"""
def loadLoginWindow():
    globals.clearWindow()
    
    def back():
        globals.clearWindow()
        loadMainMenu()

    def submitLoginInfo():
        user_name = userNameField.get("1.0", END)
        password = passwordField.get("1.0", END)
        try:
            with userDB:
                cursor = userDB.cursor()
                cursor.execute("SELECT * FROM user_account WHERE user_name = ? AND password = ?", (user_name, password))
                data = cursor.fetchall()
                globals.profile = globals.Profile(str(data[0][0]), data[0][1], data[0][2], data[0][3], data[0][4], data[0][5])
                loadGameMenu()
            return
        except:
            print("Invalid Username/Password")
            errorLabel.pack(pady=(1,100))

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    image2 = tk.PhotoImage(master=frame, file='images/back.png')
    image2 = image2.subsample(7, 7)
    backButton = tk.Button(frame, image=image2, command=back)
    backButton.config(width=75, height=75)
    backButton.pack(side="top", anchor="nw")

    userNameLabel = tk.Label(frame, text="User Name", image=image, compound=tk.CENTER, height=20, width=300)
    userNameLabel.config(font=("Areial bold", 18))
    userNameLabel.pack(pady=(60,5))
    userNameField = tk.Text(frame, height = 1, width = 20)
    userNameField.config(font=18)
    userNameField.pack(pady=(5,15))

    passwordLabel = tk.Label(frame, text="Password", image=image, compound=tk.CENTER, height=20, width=300)
    passwordLabel.config(font=("Areial bold", 18))
    passwordLabel.pack(pady=(15,5))
    passwordField = tk.Text(frame, height = 1, width = 20)
    passwordField.config(font=18)
    passwordField.pack(pady=(5,15))

    submitButton = tk.Button(frame, text="Submit", command=submitLoginInfo, height=1, width=20)
    submitButton.config(font=("Areial bold", 18))
    submitButton.pack(pady=50)
    
    errorLabel = tk.Label(frame, text="User Name Invalid", image=image, compound=tk.CENTER, height=20, width=300)
    errorLabel.config(font=("Areial bold", 18))

    frame.pack(fill="both", expand=True)
    globals.window.mainloop()

"""
loadWallet
    responsible for loading the wallet page
"""
def loadWallet(nav):

    def back():
        userAccounts.save()
        if nav == "game":
            loadGameMenu()
        elif nav == "black jack":
            loadBlackJack()

    def addCoins():
        try:
            amount = int(numCoins.get("1.0", END))
            globals.profile.wallet += amount
            userAccounts.save()
            loadWallet(nav)
        except:
            print("bad input")
        
    def subCoins():
        try:
            amount = int(numCoins.get("1.0", END))
            if globals.profile.wallet >= amount:
                globals.profile.wallet -= amount
                userAccounts.save()
                loadWallet(nav)
            else:
                warningLabel = tk.Label(frame, text="You don't have enough coins", image=image, compound=tk.CENTER, width=500, height=200)
                warningLabel.config(font=("Areial bold", 20))
                warningLabel.pack(pady=(20, 100))
        except:
            print("bad input")

    globals.clearWindow()

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    image2 = tk.PhotoImage(master=frame, file='images/back.png')
    image2 = image2.subsample(7, 7)
    backButton = tk.Button(frame, image=image2, command=back)
    backButton.config(width=75, height=75)
    backButton.pack(side="left", anchor="nw")

    wallet = globals.profile.wallet
    walletLabel = tk.Label(frame, text=str(wallet) + " coins", image=image, compound=tk.CENTER, width=100, height=100)
    walletLabel.config(font=("Areial bold", 20))
    walletLabel.pack(pady=(20, 100))

    instructions = tk.Label(frame, text="Enter number of coins", image=image, compound=tk.CENTER, width=400, height=75)
    instructions.config(font=("Areial bold", 20))
    instructions.pack(pady=(20, 5))
    numCoins = tk.Text(frame, height = 1, width = 20)
    numCoins.config(font=18)
    numCoins.pack(pady=(5,15))

    addButton = tk.Button(frame, text="Add", command=addCoins, height=1, width=20)
    addButton.config(font=("Areial bold", 18))
    addButton.pack(side="left", pady=50, expand=True)

    withdrawButton = tk.Button(frame, text="Withdraw", command=subCoins, height=1, width=20)
    withdrawButton.config(font=("Areial bold", 18))
    withdrawButton.pack(side="right", pady=50, expand=True)

    frame.pack(fill="both", expand=True)
    globals.window.mainloop()





"""
loadGameMenu
    responsible for loading the game options and defining the buttons functions
"""

def loadGameMenu():

    def back():
        if not guest:
            userAccounts.save()
        globals.clearWindow()
        globals.profile = ""
        loadMainMenu()

    globals.clearWindow()

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    image2 = tk.PhotoImage(master=frame, file='images/back.png')
    image2 = image2.subsample(7, 7)
    backButton = tk.Button(frame, image=image2, command=back)
    backButton.config(width=75, height=75)
    backButton.pack(side="left", anchor="nw")

    guest = ""
    try:
        guest = globals.profile[0] == "guest"
    except:
        guest = False

    welcome = ""
    if guest:
        welcome = "Welcome Guest!"
    else:
        welcome = "Welcome " + str(globals.profile.name)

    if not guest:
        image3 = tk.PhotoImage(master=frame, file='images/bank.png')
        image3 = image3.subsample(7, 7)
        walletButton = tk.Button(frame, image=image3, command=partial(loadWallet, "game"))
        walletButton.config(width=75, height=75)
        walletButton.pack(side="right", anchor="ne")

    gameMenuLabel = tk.Label(frame, text=welcome, image=image, compound=tk.CENTER, height=100, width=700)
    gameMenuLabel.config(font=("Areial bold", 30))
    gameMenuLabel.pack(pady=(40))
    
    blackJackButton = tk.Button(frame, text="Black Jack", command=loadBlackJack)
    blackJackButton.config(width=20, height=2, font=("Areial bold", 20))
    blackJackButton.pack(pady=20)

    texasButton = tk.Button(frame, text="Texas Hold'em", command=print("Texas Hold'em"))
    texasButton.config(width=20, height=2, font=("Areial bold", 20))
    texasButton.pack(pady=20)

    slotsButton = tk.Button(frame, text="Slots", command=print("Slots"))
    slotsButton.config(width=20, height=2, font=("Areial bold", 20))
    slotsButton.pack(pady=20)

    frame.pack(fill="both", expand=True)
    globals.window.mainloop()

"""
loadBlackJack
    responsible for loading BlackJack Game screen
"""

def loadBlackJack():

    """
    playBlackJack
        responsible for loading the game board and running the game
    """

    def playBlackJack(bet):

        def back():
            try:
                if globals.profile[0] == "guest":
                    globals.profile = ("guest", globals.profile[1] - bet)
            except:
                globals.profile.wallet -= bet
                userAccounts.save()
            loadBlackJack()

        def hit(playerhand, playerCards):
            playerScore = calculateScore(playerhand)
            if playerScore < 21 and compScore < 21:
                card = deck.drawCard()
                playerhand.append(card)
                playerNextImage = card[1]
                playerNextImage = playerNextImage.subsample(5, 5)
                playerCards.append(playerNextImage)
                playerNext = tk.Label(botFrame, image=playerNextImage, width=100, height=150)
                playerNext.pack(side="left", padx=10, anchor="e")
                score = calculateScore(playerhand)
                if score > 21:
                    continueButton = tk.Button(frame, text="You Busted!\nYou Lose!\n(Click Here to Continue)", command=continueFunc)
                    continueButton.config(width=200, height=15, font=("Areial bold", 25))
                    continueButton.pack(side="top")
                    try:
                        if globals.profile[0] == "guest":
                            globals.profile = ("guest", globals.profile[1] - bet)
                    except:
                        globals.profile.wallet -= bet
                        userAccounts.save() 



        def stand():
            if calculateScore(playerhand) <= 21:
                hitButton.destroy()
                standButton.destroy()
                dealerSecond.destroy()
            
                dealerSecondImage = comphand[1][1]
                dealerSecondImage = dealerSecondImage.subsample(5, 5)
                dealerCards.append(dealerSecondImage)
                dealerSecondCard = tk.Label(topFrame, image=dealerSecondImage, width=100, height=150)
                dealerSecondCard.pack(side="left", padx=10, anchor="e")

                dealerScore = calculateScore(comphand)
                playerScore = calculateScore(playerhand)

                while dealerScore < 21 and dealerScore < playerScore:
                    card = deck.drawCard()
                    comphand.append(card)
                    dealerNextImage = card[1]
                    dealerNextImage = dealerNextImage.subsample(5, 5)
                    dealerCards.append(dealerNextImage)
                    dealerNext = tk.Label(topFrame, image=dealerNextImage, width=100, height=150)
                    dealerNext.pack(side="left", padx=10, anchor="e")
                    dealerScore = calculateScore(comphand)

                if dealerScore > 21:
                    continueButton = tk.Button(frame, text="Dealer Busted!\nYou Win!\n(Click Here to Continue)", command=continueFunc)
                    continueButton.config(width=200, height=15, font=("Areial bold", 25))
                    continueButton.pack(side="top")
                    try:
                        if globals.profile[0] == "guest":
                            globals.profile = ("guest", globals.profile[1] + bet)
                    except:
                        globals.profile.wallet += bet
                        userAccounts.save()
                elif dealerScore > playerScore:
                    continueButton = tk.Button(frame, text="Dealer Won!\n(Click Here to Continue)", command=continueFunc)
                    continueButton.config(width=200, height=15, font=("Areial bold", 25))
                    continueButton.pack(side="top")
                    try:
                        if globals.profile[0] == "guest":
                            globals.profile = ("guest", globals.profile[1] - bet)
                    except:
                        globals.profile.wallet -= bet
                        userAccounts.save()
                else:
                    continueButton = tk.Button(frame, text="Tie!\n(Click Here to Continue)", command=continueFunc)
                    continueButton.config(width=200, height=15, font=("Areial bold", 25))
                    continueButton.pack(side="top")

        def continueFunc():
            loadBlackJack()

        def calculateScore(hand):
            count = 0
            numAces = 0
            for x in hand:
                curCard = x[0][0]
                if curCard == 'J':
                    count += 10
                elif curCard == 'Q':
                    count += 10
                elif curCard == 'K':
                    count += 10
                elif curCard == 'A':
                    count += 11
                    numAces += 1
                elif curCard == '1':
                    count += 10
                else:
                    count += int(x[0][0])
            if count > 21 and numAces > 0:
                count -= 10
                numAces -= 1
            return count

        globals.clearWindow()

        image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
        background_label = tk.Label(globals.window, image=image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = tk.Frame(globals.window)
        image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
        background_label = tk.Label(frame, image=image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        deck = globals.Deck()
        playerhand  = [deck.drawCard()]
        comphand = [deck.drawCard()]
        playerScore = 0
        compScore = 0
        playerhand.append(deck.drawCard())
        comphand.append(deck.drawCard())
        playerScore = calculateScore(playerhand)
        compScore = calculateScore(comphand)
        playerCards = []
        dealerCards = []

        topFrame = tk.Frame(frame)
        image1 = tk.PhotoImage(master=topFrame, file='images/GreenBackground.png')
        background_label = tk.Label(topFrame, image=image1)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        image2 = tk.PhotoImage(master=frame, file='images/back.png')
        image2 = image2.subsample(7, 7)
        backButton = tk.Button(frame, image=image2, command=back)
        backButton.config(width=75, height=75)
        backButton.pack(side="top", anchor="nw")

        dealerTitle = tk.Label(topFrame, text="Dealer's Hand", image=image, compound=tk.CENTER, width=250, height=50)
        dealerTitle.config(font=("Areial bold", 25))
        dealerTitle.pack(side="top", pady=40)

        dealerFirstImage = comphand[0][1]
        dealerFirstImage = dealerFirstImage.subsample(5, 5)
        dealerCards.append(dealerFirstImage)
        dealerFirst = tk.Label(topFrame, image=dealerFirstImage, width=100, height=150)
        dealerFirst.pack(side="left", padx=10, anchor="e")

        dealerSecondImage = tk.PhotoImage(master=frame, file='images/card_back_red.png')
        dealerSecondImage = dealerSecondImage.subsample(5, 5)
        dealerSecond = tk.Label(topFrame, image=dealerSecondImage, width=100, height=150)
        dealerSecond.pack(side="left", padx=10, anchor="e")

        topFrame.pack(side="top", fill="both", expand=True)

        botFrame = tk.Frame(frame)
        image3 = tk.PhotoImage(master=botFrame, file='images/GreenBackground.png')
        background_label = tk.Label(botFrame, image=image3)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        playerTitle = tk.Label(botFrame, text="Player's Hand", image=image, compound=tk.CENTER, width=250, height=50)
        playerTitle.config(font=("Areial bold", 25))
        playerTitle.pack(side="top", pady=40)

        playerFirstImage = playerhand[0][1]
        playerFirstImage = playerFirstImage.subsample(5, 5)
        playerCards.append(playerFirstImage)
        playerFirst = tk.Label(botFrame, image=playerFirstImage, width=100, height=150)
        playerFirst.pack(side="left", padx=10, anchor="e")

        playerSecondImage = playerhand[1][1]
        playerSecondImage = playerSecondImage.subsample(5, 5)
        playerCards.append(playerSecondImage)
        playerSecond = tk.Label(botFrame, image=playerSecondImage, width=100, height=150)
        playerSecond.pack(side="left", padx=10, anchor="e")

        botFrame.pack(side="top", fill="both", expand=True)

        if playerScore == 21 and compScore != 21:
            try:
                if globals.profile[0] == "guest":
                    globals.profile = ("guest", globals.profile[1] + (bet * 1.5))
            except:
                globals.profile.wallet += bet * 1.5
                userAccounts.save()
            continueButton = tk.Button(frame, text="You Got Black Jack!\nYou Win!\n(Click Here to Continue)", command=continueFunc)
            continueButton.config(width=200, height=15, font=("Areial bold", 25))
            continueButton.pack(side="top")
        elif playerScore != 21 and compScore == 21:
            try:
                if globals.profile[0]  == "guest":
                    globals.profile = ("guest", globals.profile[1] - bet)
            except:
                globals.profile.wallet -= bet
                userAccounts.save()
            continueButton = tk.Button(frame, text="Dealer Got Black Jack!\nYou Lose!\n(Click Here to Continue)", command=continueFunc)
            continueButton.config(width=200, height=15, font=("Areial bold", 25))
            continueButton.pack(side="top")


        if playerScore < 21 and compScore < 21:
            hitButton = tk.Button(frame, text="Hit", command=partial(hit, playerhand, playerCards))
            hitButton.config(width=50, height=5)
            hitButton.pack(side="left", padx=5, pady=40, expand=True)

            standButton = tk.Button(frame, text="Stand", command=stand)
            standButton.config(width=50, height=5)
            standButton.pack(side="right", padx=5, pady=40, expand=True)
        
        frame.pack(fill="both", expand=True)
        globals.window.mainloop()

        
        



    def back():
        if not guest:
            userAccounts.save()
        loadGameMenu()
    
    globals.clearWindow()

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    image2 = tk.PhotoImage(master=frame, file='images/back.png')
    image2 = image2.subsample(7, 7)
    backButton = tk.Button(frame, image=image2, command=back)
    backButton.config(width=75, height=75)
    backButton.pack(side="left", anchor="nw")

    wallet = ""
    guest = ""
    try:
        guest = globals.profile[0] == "guest"
    except:
        guest = False

    if guest:
        wallet = globals.profile[1]
    else:
        wallet = globals.profile.wallet

    if not guest:
        image3 = tk.PhotoImage(master=frame, file='images/bank.png')
        image3 = image3.subsample(7, 7)
        walletButton = tk.Button(frame, image=image3, command=partial(loadWallet, "black jack"))
        walletButton.config(width=75, height=75)
        walletButton.pack(side="right", anchor="ne")

    blackJackMenu = tk.Label(frame, text="Welcome to Black Jack!", image=image, compound=tk.CENTER, height=30, width=500)
    blackJackMenu.config(font=("Areial bold", 30))
    blackJackMenu.pack(pady=(200,20))

    walletLabel = tk.Label(frame, text=str(wallet) + " coins", image=image, compound=tk.CENTER, width=100, height=100)
    walletLabel.config(font=("Areial bold", 20))
    walletLabel.pack(pady=(20, 100))

    if wallet >= 5:
        betFive = tk.Button(frame, text="Bet 5", command=partial(playBlackJack, 5))
        betFive.config(width=10, height=5)
        betFive.pack(side="left", padx=5, expand=True)

    if wallet >= 10:
        betTen = tk.Button(frame, text="Bet 10", command=partial(playBlackJack, 10))
        betTen.config(width=10, height=5)
        betTen.pack(side="left", padx=5, expand=True)

    if wallet >= 25:
        bet25 = tk.Button(frame, text="Bet 25", command=partial(playBlackJack, 25))
        bet25.config(width=10, height=5)
        bet25.pack(side="left", padx=5, expand=True)

    if wallet >= 50:
        bet50 = tk.Button(frame, text="Bet 50", command=partial(playBlackJack, 50))
        bet50.config(width=10, height=5)
        bet50.pack(side="left", padx=5, expand=True)
    
    if wallet >= 100:
        bet100 = tk.Button(frame, text="Bet 100", command=partial(playBlackJack, 100))
        bet100.config(width=10, height=5)
        bet100.pack(side="left", padx=5, expand=True)

    frame.pack(fill="both", expand=True)
    globals.window.mainloop()


loadMainMenu()

def closeDB():
    userDB.close()