import os
from random import randint, seed
from random import random
from datetime import datetime
from tkinter import PhotoImage

global profile
window = ""

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
    deck = [("2 Hearts", PhotoImage(file="images/2_of_hearts.png"))
            , ("3 Hearts", PhotoImage(file="images/3_of_hearts.png"))
            , ("4 Hearts", PhotoImage(file="images/4_of_hearts.png"))
            , ("5 Hearts", PhotoImage(file="images/5_of_hearts.png"))
            , ("6 Hearts", PhotoImage(file="images/6_of_hearts.png"))
            , ("7 Hearts", PhotoImage(file="images/7_of_hearts.png"))
            , ("8 Hearts", PhotoImage(file="images/8_of_hearts.png"))
            , ("9 Hearts", PhotoImage(file="images/9_of_hearts.png"))
            , ("10 Hearts", PhotoImage(file="images/10_of_hearts.png"))
            , ("J Hearts", PhotoImage(file="images/jack_of_hearts2.png"))
            , ("Q Hearts", PhotoImage(file="images/queen_of_hearts2.png"))
            , ("K Hearts", PhotoImage(file="images/king_of_hearts2.png"))
            , ("A Hearts", PhotoImage(file="images/ace_of_hearts.png"))
            , ("2 Clubs", PhotoImage(file="images/2_of_clubs.png"))
            , ("3 Clubs", PhotoImage(file="images/3_of_clubs.png"))
            , ("4 Clubs", PhotoImage(file="images/4_of_clubs.png"))
            , ("5 Clubs", PhotoImage(file="images/5_of_clubs.png"))
            , ("6 Clubs", PhotoImage(file="images/6_of_clubs.png"))
            , ("7 Clubs", PhotoImage(file="images/7_of_clubs.png"))
            , ("8 Clubs", PhotoImage(file="images/8_of_clubs.png"))
            , ("9 Clubs", PhotoImage(file="images/9_of_clubs.png"))
            , ("10 Clubs", PhotoImage(file="images/10_of_clubs.png"))
            , ("J Clubs", PhotoImage(file="images/jack_of_clubs2.png"))
            , ("Q Clubs", PhotoImage(file="images/queen_of_clubs2.png"))
            , ("K Clubs", PhotoImage(file="images/king_of_clubs2.png"))
            , ("A Clubs", PhotoImage(file="images/ace_of_clubs.png"))
            , ("2 Diamonds", PhotoImage(file="images/2_of_diamonds.png"))
            , ("3 Diamonds", PhotoImage(file="images/3_of_diamonds.png"))
            , ("4 Diamonds", PhotoImage(file="images/4_of_diamonds.png"))
            , ("5 Diamonds", PhotoImage(file="images/5_of_diamonds.png"))
            , ("6 Diamonds", PhotoImage(file="images/6_of_diamonds.png"))
            , ("7 Diamonds", PhotoImage(file="images/7_of_diamonds.png"))
            , ("8 Diamonds", PhotoImage(file="images/8_of_diamonds.png"))
            , ("9 Diamonds", PhotoImage(file="images/9_of_diamonds.png"))
            , ("10 Diamonds", PhotoImage(file="images/10_of_diamonds.png"))
            , ("J Diamonds", PhotoImage(file="images/jack_of_diamonds2.png"))
            , ("Q Diamonds", PhotoImage(file="images/queen_of_diamonds2.png"))
            , ("K Diamonds", PhotoImage(file="images/king_of_diamonds2.png"))
            , ("A Diamonds", PhotoImage(file="images/ace_of_diamonds.png"))
            , ("2 Spades", PhotoImage(file="images/2_of_spades.png"))
            , ("3 Spades", PhotoImage(file="images/3_of_spades.png"))
            , ("4 Spades", PhotoImage(file="images/4_of_spades.png"))
            , ("5 Spades", PhotoImage(file="images/5_of_spades.png"))
            , ("6 Spades", PhotoImage(file="images/6_of_spades.png"))
            , ("7 Spades", PhotoImage(file="images/7_of_spades.png"))
            , ("8 Spades", PhotoImage(file="images/8_of_spades.png"))
            , ("9 Spades", PhotoImage(file="images/9_of_spades.png"))
            , ("10 Spades", PhotoImage(file="images/10_of_spades.png"))
            , ("J Spades", PhotoImage(file="images/jack_of_spades2.png"))
            , ("Q Spades", PhotoImage(file="images/queen_of_spades2.png"))
            , ("K Spades", PhotoImage(file="images/king_of_spades2.png"))
            , ("A Spades", PhotoImage(file="images/ace_of_spades.png"))]
            

    def resetDeck(self):
        deck = [("2 Hearts", PhotoImage(file="images/2_of_hearts.png"))
            , ("3 Hearts", PhotoImage(file="images/3_of_hearts.png"))
            , ("4 Hearts", PhotoImage(file="images/4_of_hearts.png"))
            , ("5 Hearts", PhotoImage(file="images/5_of_hearts.png"))
            , ("6 Hearts", PhotoImage(file="images/6_of_hearts.png"))
            , ("7 Hearts", PhotoImage(file="images/7_of_hearts.png"))
            , ("8 Hearts", PhotoImage(file="images/8_of_hearts.png"))
            , ("9 Hearts", PhotoImage(file="images/9_of_hearts.png"))
            , ("10 Hearts", PhotoImage(file="images/10_of_hearts.png"))
            , ("J Hearts", PhotoImage(file="images/jack_of_hearts2.png"))
            , ("Q Hearts", PhotoImage(file="images/queen_of_hearts2.png"))
            , ("K Hearts", PhotoImage(file="images/king_of_hearts2.png"))
            , ("A Hearts", PhotoImage(file="images/ace_of_hearts.png"))
            , ("2 Clubs", PhotoImage(file="images/2_of_clubs.png"))
            , ("3 Clubs", PhotoImage(file="images/3_of_clubs.png"))
            , ("4 Clubs", PhotoImage(file="images/4_of_clubs.png"))
            , ("5 Clubs", PhotoImage(file="images/5_of_clubs.png"))
            , ("6 Clubs", PhotoImage(file="images/6_of_clubs.png"))
            , ("7 Clubs", PhotoImage(file="images/7_of_clubs.png"))
            , ("8 Clubs", PhotoImage(file="images/8_of_clubs.png"))
            , ("9 Clubs", PhotoImage(file="images/9_of_clubs.png"))
            , ("10 Clubs", PhotoImage(file="images/10_of_clubs.png"))
            , ("J Clubs", PhotoImage(file="images/jack_of_clubs2.png"))
            , ("Q Clubs", PhotoImage(file="images/queen_of_clubs2.png"))
            , ("K Clubs", PhotoImage(file="images/king_of_clubs2.png"))
            , ("A Clubs", PhotoImage(file="images/ace_of_clubs.png"))
            , ("2 Diamonds", PhotoImage(file="images/2_of_diamonds.png"))
            , ("3 Diamonds", PhotoImage(file="images/3_of_diamonds.png"))
            , ("4 Diamonds", PhotoImage(file="images/4_of_diamonds.png"))
            , ("5 Diamonds", PhotoImage(file="images/5_of_diamonds.png"))
            , ("6 Diamonds", PhotoImage(file="images/6_of_diamonds.png"))
            , ("7 Diamonds", PhotoImage(file="images/7_of_diamonds.png"))
            , ("8 Diamonds", PhotoImage(file="images/8_of_diamonds.png"))
            , ("9 Diamonds", PhotoImage(file="images/9_of_diamonds.png"))
            , ("10 Diamonds", PhotoImage(file="images/10_of_diamonds.png"))
            , ("J Diamonds", PhotoImage(file="images/jack_of_diamonds2.png"))
            , ("Q Diamonds", PhotoImage(file="images/queen_of_diamonds2.png"))
            , ("K Diamonds", PhotoImage(file="images/king_of_diamonds2.png"))
            , ("A Diamonds", PhotoImage(file="images/ace_of_diamonds.png"))
            , ("2 Spades", PhotoImage(file="images/2_of_spades.png"))
            , ("3 Spades", PhotoImage(file="images/3_of_spades.png"))
            , ("4 Spades", PhotoImage(file="images/4_of_spades.png"))
            , ("5 Spades", PhotoImage(file="images/5_of_spades.png"))
            , ("6 Spades", PhotoImage(file="images/6_of_spades.png"))
            , ("7 Spades", PhotoImage(file="images/7_of_spades.png"))
            , ("8 Spades", PhotoImage(file="images/8_of_spades.png"))
            , ("9 Spades", PhotoImage(file="images/9_of_spades.png"))
            , ("10 Spades", PhotoImage(file="images/10_of_spades.png"))
            , ("J Spades", PhotoImage(file="images/jack_of_spades2.png"))
            , ("Q Spades", PhotoImage(file="images/queen_of_spades2.png"))
            , ("K Spades", PhotoImage(file="images/king_of_spades2.png"))
            , ("A Spades", PhotoImage(file="images/ace_of_spades.png"))]
    
    def drawCard(self):
        seed(datetime.now())
        card = self.deck[randint(0, len(self.deck)-1)]
        self.deck.remove(card)
        return card

def clearWindow():
    try:
        for x in window.winfo_children():
            x.destroy()
    except:
        print("No window found.")