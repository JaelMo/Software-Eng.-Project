from random import randint
from numpy import std
playerhand = []
playerval = 0
comphand = []
compval = 0

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


def deal():
    hand = []
    for count in range(0, 2):
        card = deck[randint(0, 12)]
        hand.append(card)
    return hand


def score(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


def hit(hand):
    hand.append(deck[randint(0, 12)])
    return hand


playerhand = deal()
x = 1000
blackjack = False
totalscore = 0
scores = []
bust = 0

for i in range(x):
    print('Game', i+1, 'Card:', end=' ')
    logic = True
    playerval = 0
    playerhand.clear()
    while logic:
        playerval = score(playerhand)
        totalscore += playerval
        scores.append(playerval)
        if playerval == 21:
            print(*playerhand, sep=', ')
            print('Blackjack!!!')
            logic = False
        elif playerval < 17:
            playerhand = hit(playerhand)
        else:
            print(*playerhand, sep=', ')
            logic = False
            if playerval > 21:
                print('Bust!!')
                bust +=1
            elif playerval < 21:
                print('You Win!!!')


avgscore = totalscore / x
print('Average score:', avgscore)
print('Standard deviation', std(scores))
prob_of_bust = bust / x * 100
print("Probability of Bust:", prob_of_bust, '%')
