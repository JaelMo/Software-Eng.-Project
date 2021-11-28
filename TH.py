from random import randint
from globals import Deck

thdeck = Deck
player_hand = []
ai_hand = []
flopcards = []
turncard = None
rivercard = None
def dealPlayer():
    print("User's cards")
    check = True
    while(check):
        slot1 = randint(0,51)
        slot2 = randint(0,51)
        if slot1 != slot2:
            check = False

    player_hand.append(thdeck.deck[slot1])
    player_hand.append(thdeck.deck[slot2])
    player_hand.sort()
    print(player_hand[0], player_hand[1])

def dealAI():
    print("AI's cards")
    check = True
    while(check):
        aislot1 = randint(0,51)
        aislot2 = randint(0,51)
        if aislot1 != aislot2:
            check = False
    ai_hand.append(thdeck.deck[aislot1])
    ai_hand.append(thdeck.deck[aislot2])
    ai_hand.sort()
    print(ai_hand[0],ai_hand[1])

def flop():
    check = True
    while(check):
        flopcards = []
        for count in range(0,3):
            flopcards.append(thdeck.deck[randint(0,51)])
        if flopcards[0] is flopcards[1] or flopcards[0] is flopcards[2] or flopcards[1] is flopcards[2]:
            check = True
        else:
            check = False
    checkCards()
    print("flop is", flopcards[0], flopcards[1], flopcards[2])

def turn():
    turncard = None
    turncard = thdeck.deck[randint(0,51)]
    checkCards()
    print("turn is", turncard)

def river():
    rivercard = None
    rivercard = thdeck.deck[randint(0,51)]
    checkCards()
    print("River is", rivercard)

def checkCards():
    for count in range(len(player_hand)):
        if player_hand[count] is ai_hand:
            dealAI()
    for count in range(len(flopcards)):
        if flopcards[count] in player_hand or flopcards[count] in ai_hand:
            flop()
    for count in range(len(player_hand)):
        for count2 in range(len(ai_hand)):
            for count3 in range(len(flopcards)):
                if turncard is player_hand[count] or turncard in ai_hand[count2] or turncard in flopcards[count3]:
                    turn()
                if rivercard is player_hand[count] or rivercard in ai_hand[count2] or rivercard in flopcards[count3]:
                    river()

def points():
    c= 0


dealPlayer()
dealAI()
flop()
turn()
river()
print(flopcards)