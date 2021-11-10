import os
from random import randint, seed
from random import random
from datetime import datetime

global profile

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

class Deck:
    deck = ["2 Hearts", "2 Spades", "2 Clubs", "2 Diamonds",
            "3 Hearts", "3 Spades", "3 Clubs", "3 Diamonds",
            "4 Hearts", "4 Spades", "4 Clubs", "4 Diamonds",
            "5 Hearts", "5 Spades", "5 Clubs", "5 Diamonds",
            "6 Hearts", "6 Spades", "6 Clubs", "6 Diamonds",
            "7 Hearts", "7 Spades", "7 Clubs", "7 Diamonds",
            "8 Hearts", "8 Spades", "8 Clubs", "8 Diamonds",
            "9 Hearts", "9 Spades", "9 Clubs", "9 Diamonds",
            "10 Hearts", "10 Spades", "10 Clubs", "10 Diamonds",
            "J Hearts", "J Spades", "J Clubs", "J Diamonds",
            "Q Hearts", "Q Spades", "Q Clubs", "Q Diamonds",
            "K Hearts", "K Spades", "K Clubs", "K Diamonds",
            "A Hearts", "A Spades", "A Clubs", "A Diamonds"]

    def resetDeck(self):
        deck = ["2 Hearts", "2 Spades", "2 Clubs", "2 Diamonds",
                "3 Hearts", "3 Spades", "3 Clubs", "3 Diamonds",
                "4 Hearts", "4 Spades", "4 Clubs", "4 Diamonds",
                "5 Hearts", "5 Spades", "5 Clubs", "5 Diamonds",
                "6 Hearts", "6 Spades", "6 Clubs", "6 Diamonds",
                "7 Hearts", "7 Spades", "7 Clubs", "7 Diamonds",
                "8 Hearts", "8 Spades", "8 Clubs", "8 Diamonds",
                "9 Hearts", "9 Spades", "9 Clubs", "9 Diamonds",
                "10 Hearts", "10 Spades", "10 Clubs", "10 Diamonds",
                "J Hearts", "J Spades", "J Clubs", "J Diamonds",
                "Q Hearts", "Q Spades", "Q Clubs", "Q Diamonds",
                "K Hearts", "K Spades", "K Clubs", "K Diamonds",
                "A Hearts", "A Spades", "A Clubs", "A Diamonds"]
    
    def drawCard(self):
        seed(datetime.now())
        card = self.deck[randint(0, len(self.deck)-1)]
        self.deck.remove(card)
        return card