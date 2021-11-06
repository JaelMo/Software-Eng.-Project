import sqlite3 as sl

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
    def __init__(self, user_name, password, name, bank_account, drivers_license, wallet):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.bank_account = bank_account
        self.drivers_license = drivers_license
        self.wallet = wallet


def createAccount():
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
        return Profile(str(data[0][0]), data[0][1], data[0][2], data[0][3], data[0][4], data[0][5])

def login():
    while True:
            user_name = input("Enter Username: ")
            password = input("Enter Password: ")
            with userDB:
                cursor = userDB.cursor()
                cursor.execute("SELECT * FROM user_account WHERE user_name = ? AND password = ?", (user_name, password))
                data = cursor.fetchall()
                return Profile(str(data[0][0]), data[0][1], data[0][2], data[0][3], data[0][4], data[0][5])

def getUserName():
    while True:
        user_name = input("Enter Username: ")
        with userDB:
            cursor = userDB.cursor()
            count = cursor.execute("SELECT COUNT(*) FROM user_account WHERE user_name = ?", (user_name,))
            count = cursor.fetchone()[0]
            if count > 0:
                print("User name already exists")
            else:
                return user_name

def save(profile):
    sql = 'INSERT INTO user_account (user_name, password, name, bank_account_number, drivers_license_number, wallet) values(?, ?, ?, ?, ?, ?)'
    data = [
        profile.user_name,
        profile.password,
        profile.name,
        profile.bank_account,
        profile.drivers_license,
        profile.wallet
    ]
    with userDB:
        userDB.execute("DELETE FROM user_account WHERE user_name = ?", (profile.user_name,))
        userDB.execute(sql, data)
        userDB.commit()

def addMoneyToWallet(profile):
    print("WALLET")
    print(str(profile.wallet) + " coins")
    amount = int(input("Enter funds to be added :"))
    profile.wallet += amount
    print(str(amount) + " coins added to wallet")
    save(profile)

def withdrawMoney(profile):
    print("WALLET")
    print(str(profile.wallet) + " coins")
    while True:
        amount = int(input("Enter funds to be withdrawn: "))
        if profile.wallet >= amount:
            profile.wallet -= amount
            print(str(amount) + " coins added to account " + str(profile.bank_account))
            break
        else:
            print("Invalid amount")
    save(profile)

profile = ''      
while True:
    menuSelect = input("Choose:\nLogin(1)\nCreate Account(2)\n")
    if menuSelect == "1":
        profile = login()
        break;
    elif menuSelect == "2":
        profile = createAccount()
        break;

while True:
    menuSelect = input("Choose:\nAdd Funds(1)\nWithdraw Funds(2)\n")
    if menuSelect == "1":
        addMoneyToWallet(profile)
        break;
    elif menuSelect == "2":
        withdrawMoney(profile)
        break;
print(profile.wallet)
userDB.close()
import texasHoldem