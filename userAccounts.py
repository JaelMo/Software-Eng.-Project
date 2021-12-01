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
            bank_account_number TEXT,
            drivers_license_number TEXT,
            wallet INTEGER
        );
    """)
except:
    print("db exists")
globals.cls()       

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


def createAccount(user_name, password, name, bank_account, drivers_license_number):
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
            return True
    except:
        print("Failed to create account")
        return False

def closeDB():
    userDB.close()