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
        globals.profile = "guest"
        loadGameMenu()

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    createAccountButton = tk.Button(frame, text="Create Account", command=loadCreateAccount)
    createAccountButton.config(width=10, height=5)
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
            try:
                sql = 'INSERT INTO user_account (user_name, password, name, bank_account_number, drivers_license_number, wallet) values(?, ?, ?, ?, ?, ?)'
                data = [
                    user_name,
                    password,
                    name,
                    bank_account,
                    drivers_license_number,
                    50
                ]
                with userDB:
                    userDB.execute(sql, data)
                    cursor = userDB.cursor()
                    cursor.execute("SELECT * FROM user_account WHERE user_name = ? AND password = ?", (user_name, password))
                    data = cursor.fetchall()
                    userDB.commit()
                    globals.profile = globals.Profile(str(data[0][0]), data[0][1], data[0][2], data[0][3], data[0][4], data[0][5])
                    mainMenu.loadMainMenu()
                
            except:
                print("Failed to create account")

 
    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    backButton = tk.Button(frame, text="Back", command=back)
    backButton.config(width=10, height=5)
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
    globals.profile = "back"

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    backButton = tk.Button(frame, text="Back", command=back)
    backButton.config(width=10, height=5)
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
def loadWallet():

    def back():
        globals.clearWindow()
        loadMainMenu()

    globals.clearWindow()

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    backButton = tk.Button(frame, text="Back", command=back)
    backButton.config(width=10, height=5)
    backButton.pack(side="top", anchor="nw")

    guest = (globals.profile == "guest")
    welcome = ""
    if guest:
        welcome = "Welcome Guest!"
    else:
        welcome = "Welcome" + str(globals.profile.name) + "!"

    userNameLabel = tk.Label(frame, text=welcome, image=image, compound=tk.CENTER, height=20, width=300)
    userNameLabel.config(font=("Areial bold", 30))
    userNameLabel.pack(pady=(60,100))
    
    blackJackButton = tk.Button(frame, text="Black Jack", command=loadBlackJack)
    blackJackButton.config(width=10, height=5, font=("Areial bold", 20))
    blackJackButton.pack(pady=20)

    texasButton = tk.Button(frame, text="Texas Hold'em", command=print("Texas Hold'em"))
    texasButton.config(width=10, height=5, font=("Areial bold", 20))
    texasButton.pack(pady=20)

    slotsButton = tk.Button(frame, text="Slots", command=print("Slots"))
    slotsButton.config(width=10, height=5, font=("Areial bold", 20))
    slotsButton.pack(pady=20)

    if not guest:
        walletButton = tk.Button(frame, text="Wallet", command=loadWallet)
        walletButton.config(width=10, height=5, font=("Areial bold", 20))
        walletButton.pack(pady=20)

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

    backButton = tk.Button(frame, text="Back", command=back)
    backButton.config(width=10, height=5)
    backButton.pack(side="top", anchor="nw")

    guest = (globals.profile == "guest")
    welcome = ""
    if guest:
        welcome = "Welcome Guest!"
    else:
        welcome = "Welcome " + str(globals.profile.name)

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

    if not guest:
        walletButton = tk.Button(frame, text="Wallet", command=loadWallet)
        walletButton.config(width=20, height=2, font=("Areial bold", 20))
        walletButton.pack(pady=20)

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
        deck = globals.deck()
        playerhand  = [deck.drawCard()]
        comphand = [deck.drawCard()]
        playerScore = 0
        compScore = 0
        playerhand.append(deck.drawCard())
        comphand.append(deck.drawCard())
        globals.cls()
        displayTable(playerhand, comphand, False)
        playerScore = calculateScore(playerhand)
        compScore = calculateScore(comphand)
        if playerScore == 21 and compScore != 21:
            winnings = choice * 1.5
            globals.profile.wallet += winnings
        elif playerScore != 21 and compScore == 21:
            globals.profile.wallet -= choice

    def back():
        if not guest:
            userAccounts.save()
        loadGameMenu()

    def playBlackJack(bet):
        print("playing")
    
    globals.clearWindow()

    image = tk.PhotoImage(master=globals.window, file='images/GreenBackground.png')
    background_label = tk.Label(globals.window, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(globals.window)
    image = tk.PhotoImage(master=frame, file='images/GreenBackground.png')
    background_label = tk.Label(frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    backButton = tk.Button(frame, text="Back", command=back)
    backButton.config(width=10, height=5)
    backButton.pack(side="left", anchor="nw")

    wallet = ""
    guest = (globals.profile == "guest")

    if guest:
        wallet = 50
    else:
        wallet = globals.profile.wallet

    walletLabel = tk.Label(frame, text=str(wallet) + " coins", image=image, compound=tk.CENTER, width=100, height=100)
    walletLabel.config(font=("Areial bold", 15))
    walletLabel.pack(side="right", anchor="ne")

    blackJackMenu = tk.Label(frame, text="Welcome to Black Jack!", image=image, compound=tk.CENTER, height=30, width=500)
    blackJackMenu.config(font=("Areial bold", 30))
    blackJackMenu.pack(pady=(200,100))

    if wallet >= 5:
        backButton = tk.Button(frame, text="Bet 5", command=partial(playBlackJack, 5))
        backButton.config(width=10, height=5)
        backButton.pack(side="left", padx=10, expand=True, anchor="e")

    if wallet >= 10:
        backButton = tk.Button(frame, text="Bet 10", command=partial(playBlackJack, 10))
        backButton.config(width=10, height=5)
        backButton.pack(side="left", padx=10, expand=True, anchor="e")

    if wallet >= 25:
        backButton = tk.Button(frame, text="Bet 25", command=partial(playBlackJack, 25))
        backButton.config(width=10, height=5)
        backButton.pack(side="left", padx=10, expand=True, anchor="e")

    if wallet >= 50:
        backButton = tk.Button(frame, text="Bet 50", command=partial(playBlackJack, 50))
        backButton.config(width=10, height=5)
        backButton.pack(side="right", padx=10, expand=True, anchor="e")
    
    if wallet >= 100:
        backButton = tk.Button(frame, text="Bet 100", command=partial(playBlackJack, 100))
        backButton.config(width=10, height=5)
        backButton.pack(side="right", padx=10, expand=True, anchor="e")

    if not guest:
        walletButton = tk.Button(frame, text="Wallet", command=loadWallet)
        walletButton.config(width=10, height=5, font=("Areial bold", 20))
        walletButton.pack(pady=20)

    frame.pack(fill="both", expand=True)
    globals.window.mainloop()


loadMainMenu()

def closeDB():
    userDB.close()