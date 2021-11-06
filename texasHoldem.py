from random import randint
from numpy import std


class card:
    def _init_ (self, rank, suit):
        self.rank = rank
        self.suit = suit

ranks = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
suits = ["Clubs","Diamonds","Hearts","Spades"]

player_hand = []

aIhand = []

def  card_define():
    carD = card()
    carD.rank = ranks[randint(0,12)]
    carD.suit = suits[randint(0,3)]
    #print(carD.rank,carD.suit)
    return carD

def dealPlayer():
    for count in range(0,2):
        player_hand.append(card_define())
    if player_hand[0] == player_hand[1]:
        player_hand[1] = card_define()
    for count in range(0,2):   
        print(player_hand[count].rank, player_hand[count].suit )

def dealAI():
    for count in range(0,2):
        aIhand.append(card_define())
    if aIhand[0] == aIhand[1]:
        aIhand[1] = card_define()
    for count in range(0,2): 
        print(aIhand[count].rank, aIhand[count].suit)

community_cards = []

def dealCommunity():
    for count in range(0,5):
        community_cards.append(card_define())
        for count2 in range(0,len(community_cards)-1):
                if community_cards[count2] == community_cards[count]:
                    community_cards[count2] = card_define()
        print(community_cards[count].rank, community_cards[count].suit )


    
dealPlayer()
print("----------")
dealCommunity()
print("----------")
#dealAI()

def compare():
    playerscore = 0
    for count in range(0,5):

        if player_hand[0].rank == community_cards[count].rank:
            if player_hand[0].suit != community_cards[count].suit:
                playerscore += 1
        if player_hand[1].rank == community_cards[count].rank:
            if player_hand[1].suit != community_cards[count].suit:
                playerscore += 1
        for count2 in range (0,count): 
            if count != count2:
                if community_cards[count].rank == community_cards[count2].rank:
                    playerscore += 1
    if player_hand[0].rank ==  player_hand[1].rank:
            playerscore += 1 
    print(playerscore)




#compare()
from collections import Counter
def compare2():
    a = dict(Counter(community_cards))
    print(a)

compare2()