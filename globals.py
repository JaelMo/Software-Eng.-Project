import os
from random import randint, seed
from random import random
from datetime import datetime
import tkinter as tk

global profile
window = tk.Tk(className="Go For Broke!",)

window.geometry("900x800")

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
    deck = [("2 Hearts", tk.PhotoImage(file="images/2_of_hearts.png"))
            , ("3 Hearts", tk.PhotoImage(file="images/3_of_hearts.png"))
            , ("4 Hearts", tk.PhotoImage(file="images/4_of_hearts.png"))
            , ("5 Hearts", tk.PhotoImage(file="images/5_of_hearts.png"))
            , ("6 Hearts", tk.PhotoImage(file="images/6_of_hearts.png"))
            , ("7 Hearts", tk.PhotoImage(file="images/7_of_hearts.png"))
            , ("8 Hearts", tk.PhotoImage(file="images/8_of_hearts.png"))
            , ("9 Hearts", tk.PhotoImage(file="images/9_of_hearts.png"))
            , ("10 Hearts", tk.PhotoImage(file="images/10_of_hearts.png"))
            , ("J Hearts", tk.PhotoImage(file="images/jack_of_hearts2.png"))
            , ("Q Hearts", tk.PhotoImage(file="images/queen_of_hearts2.png"))
            , ("K Hearts", tk.PhotoImage(file="images/king_of_hearts2.png"))
            , ("A Hearts", tk.PhotoImage(file="images/ace_of_hearts.png"))
            , ("2 Clubs", tk.PhotoImage(file="images/2_of_clubs.png"))
            , ("3 Clubs", tk.PhotoImage(file="images/3_of_clubs.png"))
            , ("4 Clubs", tk.PhotoImage(file="images/4_of_clubs.png"))
            , ("5 Clubs", tk.PhotoImage(file="images/5_of_clubs.png"))
            , ("6 Clubs", tk.PhotoImage(file="images/6_of_clubs.png"))
            , ("7 Clubs", tk.PhotoImage(file="images/7_of_clubs.png"))
            , ("8 Clubs", tk.PhotoImage(file="images/8_of_clubs.png"))
            , ("9 Clubs", tk.PhotoImage(file="images/9_of_clubs.png"))
            , ("10 Clubs", tk.PhotoImage(file="images/10_of_clubs.png"))
            , ("J Clubs", tk.PhotoImage(file="images/jack_of_clubs2.png"))
            , ("Q Clubs", tk.PhotoImage(file="images/queen_of_clubs2.png"))
            , ("K Clubs", tk.PhotoImage(file="images/king_of_clubs2.png"))
            , ("A Clubs", tk.PhotoImage(file="images/ace_of_clubs.png"))
            , ("2 Diamonds", tk.PhotoImage(file="images/2_of_diamonds.png"))
            , ("3 Diamonds", tk.PhotoImage(file="images/3_of_diamonds.png"))
            , ("4 Diamonds", tk.PhotoImage(file="images/4_of_diamonds.png"))
            , ("5 Diamonds", tk.PhotoImage(file="images/5_of_diamonds.png"))
            , ("6 Diamonds", tk.PhotoImage(file="images/6_of_diamonds.png"))
            , ("7 Diamonds", tk.PhotoImage(file="images/7_of_diamonds.png"))
            , ("8 Diamonds", tk.PhotoImage(file="images/8_of_diamonds.png"))
            , ("9 Diamonds", tk.PhotoImage(file="images/9_of_diamonds.png"))
            , ("10 Diamonds", tk.PhotoImage(file="images/10_of_diamonds.png"))
            , ("J Diamonds", tk.PhotoImage(file="images/jack_of_diamonds2.png"))
            , ("Q Diamonds", tk.PhotoImage(file="images/queen_of_diamonds2.png"))
            , ("K Diamonds", tk.PhotoImage(file="images/king_of_diamonds2.png"))
            , ("A Diamonds", tk.PhotoImage(file="images/ace_of_diamonds.png"))
            , ("2 Spades", tk.PhotoImage(file="images/2_of_spades.png"))
            , ("3 Spades", tk.PhotoImage(file="images/3_of_spades.png"))
            , ("4 Spades", tk.PhotoImage(file="images/4_of_spades.png"))
            , ("5 Spades", tk.PhotoImage(file="images/5_of_spades.png"))
            , ("6 Spades", tk.PhotoImage(file="images/6_of_spades.png"))
            , ("7 Spades", tk.PhotoImage(file="images/7_of_spades.png"))
            , ("8 Spades", tk.PhotoImage(file="images/8_of_spades.png"))
            , ("9 Spades", tk.PhotoImage(file="images/9_of_spades.png"))
            , ("10 Spades", tk.PhotoImage(file="images/10_of_spades.png"))
            , ("J Spades", tk.PhotoImage(file="images/jack_of_spades2.png"))
            , ("Q Spades", tk.PhotoImage(file="images/queen_of_spades2.png"))
            , ("K Spades", tk.PhotoImage(file="images/king_of_spades2.png"))
            , ("A Spades", tk.PhotoImage(file="images/ace_of_spades.png"))]
            

    def resetDeck(self):
        deck = [("2 Hearts", tk.PhotoImage(file="images/2_of_hearts.png"))
            , ("3 Hearts", tk.PhotoImage(file="images/3_of_hearts.png"))
            , ("4 Hearts", tk.PhotoImage(file="images/4_of_hearts.png"))
            , ("5 Hearts", tk.PhotoImage(file="images/5_of_hearts.png"))
            , ("6 Hearts", tk.PhotoImage(file="images/6_of_hearts.png"))
            , ("7 Hearts", tk.PhotoImage(file="images/7_of_hearts.png"))
            , ("8 Hearts", tk.PhotoImage(file="images/8_of_hearts.png"))
            , ("9 Hearts", tk.PhotoImage(file="images/9_of_hearts.png"))
            , ("10 Hearts", tk.PhotoImage(file="images/10_of_hearts.png"))
            , ("J Hearts", tk.PhotoImage(file="images/jack_of_hearts2.png"))
            , ("Q Hearts", tk.PhotoImage(file="images/queen_of_hearts2.png"))
            , ("K Hearts", tk.PhotoImage(file="images/king_of_hearts2.png"))
            , ("A Hearts", tk.PhotoImage(file="images/ace_of_hearts.png"))
            , ("2 Clubs", tk.PhotoImage(file="images/2_of_clubs.png"))
            , ("3 Clubs", tk.PhotoImage(file="images/3_of_clubs.png"))
            , ("4 Clubs", tk.PhotoImage(file="images/4_of_clubs.png"))
            , ("5 Clubs", tk.PhotoImage(file="images/5_of_clubs.png"))
            , ("6 Clubs", tk.PhotoImage(file="images/6_of_clubs.png"))
            , ("7 Clubs", tk.PhotoImage(file="images/7_of_clubs.png"))
            , ("8 Clubs", tk.PhotoImage(file="images/8_of_clubs.png"))
            , ("9 Clubs", tk.PhotoImage(file="images/9_of_clubs.png"))
            , ("10 Clubs", tk.PhotoImage(file="images/10_of_clubs.png"))
            , ("J Clubs", tk.PhotoImage(file="images/jack_of_clubs2.png"))
            , ("Q Clubs", tk.PhotoImage(file="images/queen_of_clubs2.png"))
            , ("K Clubs", tk.PhotoImage(file="images/king_of_clubs2.png"))
            , ("A Clubs", tk.PhotoImage(file="images/ace_of_clubs.png"))
            , ("2 Diamonds", tk.PhotoImage(file="images/2_of_diamonds.png"))
            , ("3 Diamonds", tk.PhotoImage(file="images/3_of_diamonds.png"))
            , ("4 Diamonds", tk.PhotoImage(file="images/4_of_diamonds.png"))
            , ("5 Diamonds", tk.PhotoImage(file="images/5_of_diamonds.png"))
            , ("6 Diamonds", tk.PhotoImage(file="images/6_of_diamonds.png"))
            , ("7 Diamonds", tk.PhotoImage(file="images/7_of_diamonds.png"))
            , ("8 Diamonds", tk.PhotoImage(file="images/8_of_diamonds.png"))
            , ("9 Diamonds", tk.PhotoImage(file="images/9_of_diamonds.png"))
            , ("10 Diamonds", tk.PhotoImage(file="images/10_of_diamonds.png"))
            , ("J Diamonds", tk.PhotoImage(file="images/jack_of_diamonds2.png"))
            , ("Q Diamonds", tk.PhotoImage(file="images/queen_of_diamonds2.png"))
            , ("K Diamonds", tk.PhotoImage(file="images/king_of_diamonds2.png"))
            , ("A Diamonds", tk.PhotoImage(file="images/ace_of_diamonds.png"))
            , ("2 Spades", tk.PhotoImage(file="images/2_of_spades.png"))
            , ("3 Spades", tk.PhotoImage(file="images/3_of_spades.png"))
            , ("4 Spades", tk.PhotoImage(file="images/4_of_spades.png"))
            , ("5 Spades", tk.PhotoImage(file="images/5_of_spades.png"))
            , ("6 Spades", tk.PhotoImage(file="images/6_of_spades.png"))
            , ("7 Spades", tk.PhotoImage(file="images/7_of_spades.png"))
            , ("8 Spades", tk.PhotoImage(file="images/8_of_spades.png"))
            , ("9 Spades", tk.PhotoImage(file="images/9_of_spades.png"))
            , ("10 Spades", tk.PhotoImage(file="images/10_of_spades.png"))
            , ("J Spades", tk.PhotoImage(file="images/jack_of_spades2.png"))
            , ("Q Spades", tk.PhotoImage(file="images/queen_of_spades2.png"))
            , ("K Spades", tk.PhotoImage(file="images/king_of_spades2.png"))
            , ("A Spades", tk.PhotoImage(file="images/ace_of_spades.png"))]
    
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