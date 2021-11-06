from random import randint

class card:
    def _init_ (self, rank, suit):
        self.rank = rank
        self.suit = suit

ranks = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
suits = ["Clubs","Diamonds","Hearts","Spades"]

player_hand = []
community_cards = []
aIhand = []

def card_define():
    carD = card()
    carD.rank = ranks[randint(0,12)]
    carD.suit = suits[randint(0,3)]
    #print(carD.rank,carD.suit)
    return carD

def dealPlayer():
    print("User's cards")
    for count in range(0,2):
        player_hand.append(card_define())
    if player_hand[0] == player_hand[1]:
        player_hand[1] = card_define()
    for count in range(0,2):
        
        print(player_hand[count].rank, player_hand[count].suit )
    print("----------")
    dealAI()

def dealAI():
    print("AI's cards")
    for count in range(0,2):
        aIhand.append(card_define())
    if aIhand[0] == aIhand[1]:
            aIhand[1] = card_define()
    for count in range(0,2):
        print(aIhand[count].rank, aIhand[count].suit)
    print("----------")
    dealCommunity()    
        
def dealCommunity():
    print("Community cards")
    for count in range(0, 5):
        community_cards.append(card_define())
        for count2 in range(0,len(community_cards)-1):
                if community_cards[count] == community_cards[count2]:
                    community_cards[count2] = card_define()
    checkForDupe()
    for count in range(0, 5):
        print(community_cards[count].rank, community_cards[count].suit )
   
def checkForDupe():
    for count1 in range(0, len(player_hand)):
        for count2 in range(0,len(aIhand)):
            for  count3 in range(0,len(community_cards)):
                while player_hand[count1] == aIhand[count2] == community_cards[count3]:
                    aIhand[count2] = card_define()
                    community_cards[count3] = card_define()
                    if aIhand[0]==aIhand[1]:
                        aIhand[1] = card_define()
                        for count4 in range(0,len(community_cards)):
                            if community_cards[count3] == community_cards[count4]:
                                community_cards[count4] = card_define()

def compare():
    playerscore = 1
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

def uservsAicompare():
    gameTie = False
    for count in range(0,2):
        for secondcount in range(0,2):
            if player_hand[count].rank == aIhand[secondcount].rank:
                highcard(count)

def highcard(position):
    userhigh = 0
    aihigh = 0
    for count in range (0,len(ranks)):
        if ranks[count] == player_hand[position].rank:
            userhigh = ranks.index(ranks[count])
            aihigh = ranks.index(ranks[count])
        if userhigh > aihigh:
            print("User wins by high card")
        if userhigh < aihigh:
            print("User loses by high card")

def compare2():
    count = 0
    while count < len(community_cards):
        a = sum(c.rank == community_cards[count].rank  for c in community_cards)
        count+=1
    if a == 1:
        print("no pairs")
        uservsAicompare()
    else:   
        print(a-1," pair for user")

dealPlayer()
#compare()
compare2()
uservsAicompare()