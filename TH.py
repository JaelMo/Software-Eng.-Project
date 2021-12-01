from random import randint
from tkinter.constants import NONE
from globals import Deck
from math import floor, trunc
thdeck = Deck
global player_hand
global ai_hand
global flopcards
global turncard
global rivercard
global communitycards

player_hand = []
ai_hand = []
flopcards = []
turncard = None
rivercard = None
communitycards = []

def dealPlayer():
    print("Player's Hand")
    player_hand.append(thdeck.drawCard(thdeck))
    player_hand.append(thdeck.drawCard(thdeck))
    print(player_hand)
    return player_hand

def dealAI():
    print("Ai's Hand")
    ai_hand.append(thdeck.drawCard(thdeck))
    ai_hand.append(thdeck.drawCard(thdeck))
    print(ai_hand)
    return ai_hand

def flop():
    for count in range(3):
        flopcards.append(thdeck.drawCard(thdeck))
    return flopcards

def turn():
    turncard = thdeck.drawCard(thdeck)
    return turncard

def river():
    rivercard = thdeck.drawCard(thdeck)
    return rivercard



    
def community_cards():
    print("The community cards at play are:")
    communitycards = list(flopcards)
    communitycards.append(turncard)
    communitycards.append(rivercard)
    print(communitycards)
    return communitycards

def getPosition(cards):
    cardset = []
    deck = []
    lst = []
    deck = thdeck.resetDeck(thdeck)
    lst1 = list(zip(*cards))
    lst2 = list(zip(*deck))
    deck0 = lst2[0]
    cardset = lst1[0]
    #print(deck0)
    #print(len(deck0))
    for counter in range(len(cardset)):
        for counter2 in range(len(deck0)):
            if deck0[counter2] == cardset[counter]:
                lst.append(counter2)
    #if len(deck0) == 52:
        #print("all cards are there")
    #for counting in range(len(cardset)):
        #print(cardset[counting])
    return lst
                
def royalF(cards):
    pos = []
    
    pos.append(getPosition(cards))
    for count in range(3):
        if any(count*13+8 in s for s in pos):
            if any(count*13+9 in s for s in pos):
                if any(count*13+10 in s for s in pos):
                    if any(count*13+11 in s for s in pos):
                        if any(count*13+12 in s for s in pos):
                            return True
    else:
        return False



def straightF(cards):
    suitcount = 0
    sfcounter = 0
    pos = []
    pos= getPosition(cards)
    pos.sort()
    print(pos)
    for m in range(len(pos)-1):
        if floor(pos[m]/13)==floor(pos[m+1]/13):
            suitcount+=1
    for n in range(0,len(pos)-1):
        if pos[n]+1 == pos[n+1]:
            sfcounter += 1
    if sfcounter >=5 and suitcount >=5:
        return True
    else:
        return False

def fofk(cards):
    temp = 0
    pos = []
    pos = getPosition(cards)
    pos.sort()
    for n in range(len(pos)):
        for m in range(len(pos)):
            if pos[n] == pos[m]+13:
                temp+=1
    if temp == 4:
        return True
    else:
        return False

def fullhouse():
    return True

def totk(cards):
    temp = 0
    temp2 = 0
    pos = []
    pos = getPosition(cards)
    pos.sort()
    for n in range(len(pos)):
        for m in range(len(pos)):
            for v in range(len(pos)):
                if pos[n] == pos[m]+13:
                    temp+=1
                if pos[n] == pos[v]+13 and pos[v] != pos[m]:
                    temp2+=1
    #start here
    
    if temp2 == 2 and temp == 3:
        return  temp+temp2
    elif temp == 3 and temp2 < 2:
        return temp
    elif temp ==2 and temp2==2:
        return temp+temp2
    elif temp == 2 and temp2 < 2:
        return temp

def highcard():
    lst1 = []
    lst2= []
    lst1 = getPosition(player_hand)
    lst2 = getPosition(ai_hand)
    lst1.sort()
    lst2.sort()

    playerhigh = floor(lst1[1]/4)
    aihigh = floor(lst2[1]/4)

    if playerhigh > aihigh:
        print("PLAYER WINS BY HIGH CARD")
    elif playerhigh < aihigh:
        print("AI WINS BY HIGH CARD")
    else:
        print("Tie")
    
def points(hand,comCards):
    playable_cards = []
    for count in range(len(hand)):
        playable_cards.append(hand[count])
    for count in range(len(comCards)):
        playable_cards.append(comCards[count])

    #print(len(thdeck.resetDeck(thdeck)))
    #for card in range(len(playable_cards)):
        #print(playable_cards[card][0])
    if royalF(playable_cards):
        print("Royal Flush")
    elif straightF(playable_cards) and royalF(playable_cards) == False:
        print("Straight Flush")
    elif fofk(playable_cards):
        print("Four of A Kind")
    elif totk(playable_cards) == 5:
        print("Full House")
    elif totk(playable_cards) == 3 and fofk(playable_cards)==False:
        print("three of a kind")
    elif totk(playable_cards)== 4:
        print('2 pairs')
    elif totk(playable_cards) == 2:
        print("Pair")
    else:
        highcard()

player_hand = []
ai_hand = []
flopcards = []
turncard = None
rivercard = None
communitycards = []
    




player_hand = dealPlayer()
ai_hand = dealAI()
flopcards = flop()
turncard = turn()
rivercard = river()
communitycards = community_cards()
print("\n\nplayer points:")
playerpoints = points(player_hand,communitycards)
#print("------------------------------------------------------")
print("Ai points:")
aipoints = points(ai_hand,communitycards)

