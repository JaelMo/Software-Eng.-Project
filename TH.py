from random import randint
from globals import Deck

thdeck = Deck
global player_hand
global ai_hand
global flopcards
global turncard
global rivercard
global communitycards


def dealPlayer():
    check = True
    while(check):
        slot1 = randint(0,51)
        slot2 = randint(0,51)
        if slot1 != slot2:
            check = False

    player_hand.append(thdeck.deck[slot1])
    player_hand.append(thdeck.deck[slot2])
    player_hand.sort()
    
    return player_hand

def dealAI():
    
    check = True
    while(check):
        aislot1 = randint(0,51)
        aislot2 = randint(0,51)
        if aislot1 != aislot2:
            check = False
    ai_hand.append(thdeck.deck[aislot1])
    ai_hand.append(thdeck.deck[aislot2])
    ai_hand.sort()
    
    return ai_hand
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

    return flopcards
def turn():
    turncard = None
    turncard = thdeck.deck[randint(0,51)]
    return turncard
def river():
    rivercard = None
    rivercard = thdeck.deck[randint(0,51)]
    return rivercard

def checkCards():
    if player_hand[0] == player_hand[1]:
        dealPlayer()
    check1 = True
    while(check1):
        if player_hand[0] == ai_hand[0] or player_hand[1] is ai_hand[1] or player_hand[0] is ai_hand[1] or player_hand[1] is ai_hand[0]:
            dealAI()
        else:
            check1 = False
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
    print("User's cards")
    print(player_hand[0], player_hand[1])
    print("AI's cards")
    print(ai_hand[0],ai_hand[1])
def community_cards():
    print("The community cards at play are:")
    communitycards = list(flopcards)
    communitycards.append(turncard)
    communitycards.append(rivercard)
    for count in range(len(communitycards)):
        print(communitycards[count])
    return communitycards

def points():
    c = 0
    thdeck.resetDeck(thdeck)
    for count in range(len(communitycards)):
        #print(thdeck.deck.index(communitycards[count]))
        #check if royal flush
        if thdeck.deck.index(player_hand[0]) in range(32,51):
            if thdeck.deck.index(player_hand[1]) in range(32,51):
                if thdeck.deck.index(communitycards[count]) in range(32,51):
                    if thdeck.deck.index(player_hand[0]) in range(32,35):
                        if thdeck.deck.index(player_hand[1]) in range(36,39):
                            if thdeck.deck.index(communitycards[0]) in range(40,43) or thdeck.deck.index(communitycards[1]) in range(40,43) or thdeck.deck.index(communitycards[2]) in range(40,43) or thdeck.deck.index(communitycards[3]) in range(40,43) or thdeck.deck.index(communitycards[4]) in range(40,43):
                                if thdeck.deck.index(communitycards[0]) in range(44,47) or thdeck.deck.index(communitycards[1]) in range(44,47) or thdeck.deck.index(communitycards[2]) in range(44,47) or thdeck.deck.index(communitycards[3]) in range(44,47) or thdeck.deck.index(communitycards[4]) in range(44,47):
                                    if thdeck.deck.index(communitycards[0]) in range(48,51) or thdeck.deck.index(communitycards[1]) in range(48,51) or thdeck.deck.index(communitycards[2]) in range(48,51) or thdeck.deck.index(communitycards[3]) in range(48,51) or thdeck.deck.index(communitycards[4]) in range(48,51):
                                        print("ROYAL FLUSH!!!")


                    if thdeck.deck.index(player_hand[0]) in range(36,39):
                        if thdeck.deck.index(player_hand[1]) in range(32,35):
                            if thdeck.deck.index(communitycards[0]) in range(40,43) or thdeck.deck.index(communitycards[1]) in range(40,43) or thdeck.deck.index(communitycards[2]) in range(40,43) or thdeck.deck.index(communitycards[3]) in range(40,43) or thdeck.deck.index(communitycards[4]) in range(40,43):
                                if thdeck.deck.index(communitycards[0]) in range(44,47) or thdeck.deck.index(communitycards[1]) in range(44,47) or thdeck.deck.index(communitycards[2]) in range(44,47) or thdeck.deck.index(communitycards[3]) in range(44,47) or thdeck.deck.index(communitycards[4]) in range(44,47):
                                    if thdeck.deck.index(communitycards[0]) in range(48,51) or thdeck.deck.index(communitycards[1]) in range(48,51) or thdeck.deck.index(communitycards[2]) in range(48,51) or thdeck.deck.index(communitycards[3]) in range(48,51) or thdeck.deck.index(communitycards[4]) in range(48,51):
                                        print("ROYAL FLUSH!!!")

                            
                    if thdeck.deck.index(player_hand[0]) in range(40,43):
                        if thdeck.deck.index(player_hand[1]) in range(36,39):
                            if thdeck.deck.index(communitycards[0]) in range(32,35) or thdeck.deck.index(communitycards[1]) in range(32,35) or thdeck.deck.index(communitycards[2]) in range(32,35) or thdeck.deck.index(communitycards[3]) in range(32,35) or thdeck.deck.index(communitycards[4]) in range(32,35):
                                if thdeck.deck.index(communitycards[0]) in range(44,47) or thdeck.deck.index(communitycards[1]) in range(44,47) or thdeck.deck.index(communitycards[2]) in range(44,47) or thdeck.deck.index(communitycards[3]) in range(44,47) or thdeck.deck.index(communitycards[4]) in range(44,47):
                                    if thdeck.deck.index(communitycards[0]) in range(48,51) or thdeck.deck.index(communitycards[1]) in range(48,51) or thdeck.deck.index(communitycards[2]) in range(48,51) or thdeck.deck.index(communitycards[3]) in range(48,51) or thdeck.deck.index(communitycards[4]) in range(48,51):
                                        print("ROYAL FLUSH!!!")

                    if thdeck.deck.index(player_hand[0]) in range(44,47):
                        if thdeck.deck.index(player_hand[1]) in range(36,39):
                            if thdeck.deck.index(communitycards[0]) in range(32,35) or thdeck.deck.index(communitycards[1]) in range(32,35) or thdeck.deck.index(communitycards[2]) in range(32,35) or thdeck.deck.index(communitycards[3]) in range(32,35) or thdeck.deck.index(communitycards[4]) in range(32,35):
                                if thdeck.deck.index(communitycards[0]) in range(40,43) or thdeck.deck.index(communitycards[1]) in range(40,43) or thdeck.deck.index(communitycards[2]) in range(40,43) or thdeck.deck.index(communitycards[3]) in range(40,43) or thdeck.deck.index(communitycards[4]) in range(40,43):
                                    if thdeck.deck.index(communitycards[0]) in range(48,51) or thdeck.deck.index(communitycards[1]) in range(48,51) or thdeck.deck.index(communitycards[2]) in range(48,51) or thdeck.deck.index(communitycards[3]) in range(48,51) or thdeck.deck.index(communitycards[4]) in range(48,51):
                                        print("ROYAL FLUSH!!!")

                    if thdeck.deck.index(player_hand[0]) in range(48,51):
                        if thdeck.deck.index(player_hand[1]) in range(36,39):
                            if thdeck.deck.index(communitycards[0]) in range(32,35) or thdeck.deck.index(communitycards[1]) in range(32,35) or thdeck.deck.index(communitycards[2]) in range(32,35) or thdeck.deck.index(communitycards[3]) in range(32,35) or thdeck.deck.index(communitycards[4]) in range(32,35):
                                if thdeck.deck.index(communitycards[0]) in range(40,43) or thdeck.deck.index(communitycards[1]) in range(40,43) or thdeck.deck.index(communitycards[2]) in range(40,43) or thdeck.deck.index(communitycards[3]) in range(40,43) or thdeck.deck.index(communitycards[4]) in range(40,43):
                                    if thdeck.deck.index(communitycards[0]) in range(44,47) or thdeck.deck.index(communitycards[1]) in range(44,47) or thdeck.deck.index(communitycards[2]) in range(44,47) or thdeck.deck.index(communitycards[3]) in range(44,47) or thdeck.deck.index(communitycards[4]) in range(44,47):
                                        print("ROYAL FLUSH!!!")

    if thdeck.deck.index(player_hand[0]) in range(0,3) and thdeck.deck.index(player_hand[1]) in range(0,3):
        print("pair of 2's in player's hand")
        userpair = True
    if thdeck.deck.index(player_hand[0]) in range(4,7) and thdeck.deck.index(player_hand[1]) in range(4,7):
        print("pair of 3's in player's hand")
        userpair = True
    if thdeck.deck.index(player_hand[0])  in range(8,11) and thdeck.deck.index(player_hand[1]) in range(8,11):
        print("pair of 4's in player's hand")
        userpair = True
    if thdeck.deck.index(player_hand[0]) in range(12,15) and thdeck.deck.index(player_hand[1]) in range(12,15):
        print("pair of 5's in player's hand")
        userpair = True
    if thdeck.deck.index(player_hand[0]) in range(16,19) and thdeck.deck.index(player_hand[1]) in range(16,19):
        print("pair of 6's in player's hand")
    if thdeck.deck.index(player_hand[0])  in range(20,23) and thdeck.deck.index(player_hand[1]) in range(20,23):
        print("pair of 7's in player's hand")
    if thdeck.deck.index(player_hand[0]) in range(24,27) and thdeck.deck.index(player_hand[1]) in range(24,27):
        print("pair of 8's in player's hand")
    if thdeck.deck.index(player_hand[0]) in range(28,31) and thdeck.deck.index(player_hand[1]) in range(28,31):
        print("pair of 9's in player's hand")
    if thdeck.deck.index(player_hand[0])  in range(32,35) and thdeck.deck.index(player_hand[1]) in range(32,35):
        print("pair of 10's in player's hand")
    if thdeck.deck.index(player_hand[0]) in range(36,39) and thdeck.deck.index(player_hand[1]) in range(36,39):
        print("pair of J's in player's hand")
    if thdeck.deck.index(player_hand[0]) in range(40,43)and thdeck.deck.index(player_hand[1]) in range(40,43):
        print("pair of Q's in player's hand")
    if thdeck.deck.index(player_hand[0]) in range(44,47) and thdeck.deck.index(player_hand[1]) in range(44,47):
        print("pair of K's in player's hand")
    if thdeck.deck.index(player_hand[0])  in range(48,51) and thdeck.deck.index(player_hand[1]) in range(48,51):
        print("pair of A's in player's hand")
    for count in range(0,4):
        if thdeck.deck.index(player_hand[0]) in range(0,3) and thdeck.deck.index(player_hand[1]) in range(0,3) and thdeck.deck.index(communitycards[count]) in range(0,3):
            print("three of a kind of 2's")
    if thdeck.deck.index(player_hand[0]) in range(4,7) and thdeck.deck.index(player_hand[1]) in range(4,7) and thdeck.deck.index(communitycards[count]) in range(4,7):
            print("three of a kind of 3's:")
    if thdeck.deck.index(player_hand[0])  in range(8,11) and thdeck.deck.index(player_hand[1]) in range(8,11) and thdeck.deck.index(communitycards[count]) in range(8,11):
            print("three of a kind of 4's:")
    if thdeck.deck.index(player_hand[0]) in range(12,15) and thdeck.deck.index(player_hand[1]) in range(12,15) and thdeck.deck.index(communitycards[count]) in range(12,15):
            print("three of a kind of 5's:")
    if thdeck.deck.index(player_hand[0]) in range(16,19) and thdeck.deck.index(player_hand[1]) in range(16,19) and thdeck.deck.index(communitycards[count]) in range(16,19):
            print("three of a kind of 6's:")
    if thdeck.deck.index(player_hand[0])  in range(20,23) and thdeck.deck.index(player_hand[1]) in range(20,23) and thdeck.deck.index(communitycards[count]) in range(20,23):
            print("three of a kind of 7's:")
    if thdeck.deck.index(player_hand[0]) in range(24,27) and thdeck.deck.index(player_hand[1]) in range(24,27) and thdeck.deck.index(communitycards[count]) in range(24,27):
            print("three of a kind of 8's:")
    if thdeck.deck.index(player_hand[0]) in range(28,31) and thdeck.deck.index(player_hand[1]) in range(28,31) and thdeck.deck.index(communitycards[count]) in range(28,31):
            print("three of a kind of 9's:")
    if thdeck.deck.index(player_hand[0])  in range(32,35) and thdeck.deck.index(player_hand[1]) in range(32,35) and thdeck.deck.index(communitycards[count]) in range(32,35):
            print("three of a kind of 10's:")
    if thdeck.deck.index(player_hand[0]) in range(36,39) and thdeck.deck.index(player_hand[1]) in range(36,39) and thdeck.deck.index(communitycards[count]) in range(36,39):
            print("three of a kind of J's:")
    if thdeck.deck.index(player_hand[0]) in range(40,43)and thdeck.deck.index(player_hand[1]) in range(40,43) and thdeck.deck.index(communitycards[count]) in range(40,43):
            print("three of a kind of Q's:")
    if thdeck.deck.index(player_hand[0]) in range(44,47) and thdeck.deck.index(player_hand[1]) in range(44,47) and thdeck.deck.index(communitycards[count]) in range(44,47):
            print("three of a kind of K's:")
    if thdeck.deck.index(player_hand[0])  in range(48,51) and thdeck.deck.index(player_hand[1]) in range(48,51) and thdeck.deck.index(communitycards[count]) in range(48,51):
            print("three of a kind of A's:")






testnumber = 100
for count in range(testnumber):
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
    checkCards()
    communitycards = community_cards()
    c = points()
    print("------------------------------------------------------")


print("number of royal flushes", c)