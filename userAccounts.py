"""
This file houses all database interactions for the project.
-createAccount
-login
-getUserName -> helper function used by createAccount to ensure user_names are not duplicated
-save -> saves the current state of the user profile
-addMoneyToWallet
-withdrawMoney
-closeDB -> shuts down connection to SQLite Database
"""

import sqlite3 as sl
import globals

userDB = sl.connect('userDB.db')
try:
    with userDB:
        userDB.execute("""
        CREATE TABLE user_account (
            user_name TEXT NOT NULL PRIMARY KEY,
            password TEXT NOT NULL,
            name TEXT,
            bank_account_number INTEGER,
            drivers_license_number INTEGER,
            wallet INTEGER
        );
    """)
except:
    print("db exists")
globals.cls()

def createAccount():
    try:
        user_name = getUserName()
        password = input("Enter password: ")
        name = input("Enter name: ")
        bank_account = input("Enter bank account number: ")
        drivers_license_number = input("Enter driver's license number: ")

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
    except:
        print("Failed to create account")
        globals.profile = "back"

def login():
    while True:
        try:
            print("You may enter \"back\" at any time to return to the login page\n\n")
            user_name = input("Enter Username: ")
            password = input("Enter Password: ")
            if user_name == "back" or password == "back":
                globals.profile = "back"
                break
            with userDB:
                cursor = userDB.cursor()
                cursor.execute("SELECT * FROM user_account WHERE user_name = ? AND password = ?", (user_name, password))
                data = cursor.fetchall()
                globals.profile = globals.Profile(str(data[0][0]), data[0][1], data[0][2], data[0][3], data[0][4], data[0][5])
            return
        except:
            print("Invalid Username/Password")
    globals.profile = "back"

def getUserName():
    while True:
        user_name = input("Enter Username: ")
        if user_name != "guest":
            with userDB:
                cursor = userDB.cursor()
                count = cursor.execute("SELECT COUNT(*) FROM user_account WHERE user_name = ?", (user_name,))
                count = cursor.fetchone()[0]
                if count > 0:
                    print("User name already exists")
                else:
                    return user_name
        else:
            print("User name cannot be \"guest\"")

def save():
    sql = 'INSERT INTO user_account (user_name, password, name, bank_account_number, drivers_license_number, wallet) values(?, ?, ?, ?, ?, ?)'
    data = [
        globals.profile.user_name,
        globals.profile.password,
        globals.profile.name,
        globals.profile.bank_account,
        globals.profile.drivers_license,
        globals.profile.wallet
    ]
    with userDB:
        userDB.execute("DELETE FROM user_account WHERE user_name = ?", (globals.profile.user_name,))
        userDB.execute(sql, data)
        userDB.commit()

def addMoneyToWallet():
    print("WALLET")
    print(str(globals.profile.wallet) + " coins")
    amount = int(input("Enter funds to be added :"))
    globals.profile.wallet += amount
    print(str(amount) + " coins added to wallet")
    save()

def withdrawMoney():
    print("WALLET")
    print(str(globals.profile.wallet) + " coins")
    while True:
        amount = int(input("Enter funds to be withdrawn: "))
        if globals.profile.wallet >= amount:
            globals.profile.wallet -= amount
            print(str(amount) + " coins added to account " + str(globals.profile.bank_account))
            break
        else:
            print("Invalid amount")
    save()

def closeDB():
    userDB.close()