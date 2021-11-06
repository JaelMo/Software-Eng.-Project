import sqlite3 as sl
import uuid
from random import random
from random import seed

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

class Profile:
    def __init__(name, bank_account, wallet):
        self.name = name
        self.bank_account = bank_account
        self.wallet = wallet


def createAccount(user_name, password, name, bank_account, drivers_license_number):
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

def login(user_name, password):
    try:
        with userDB:
            data = userDB.execute("SELECT * FROM user_account WHERE user_name = ? AND password = ?", (user_name, password))
            for row in data:
                print(row)
    except:
        print("invalid login")

def getUserName():
    while True:
        user_name = input("Enter Username: ")
        with userDB:
            cursor = userDB.cursor()
            count = cursor.execute("SELECT COUNT(*) FROM user_account WHERE user_name = ?", (user_name,))
            userDB.commit()
            count = cursor.fetchone()[0]
            if count > 0:
                print("User name already exists")
            else:
                return user_name
                


user_name = getUserName()
password = input("Enter Password: ")
name = input("Enter name: ")
bank_account = input("Enter bank account number: ")
drivers_license_number = input("Enter drivers license number: ")

createAccount(user_name, password, name, bank_account, drivers_license_number)

user_name = input("Enter Username: ")
password = input("Enter Password: ")

login(user_name, password)