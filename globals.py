import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Profile:
    def __init__(self, user_name, password, name, bank_account, drivers_license, wallet):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.bank_account = bank_account
        self.drivers_license = drivers_license
        self.wallet = wallet

global profile