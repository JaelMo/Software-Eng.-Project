import globals
import userAccounts

def play(deck, choice):
    deck.resetDeck()
    playerhand  = [deck.drawCard()]
    comphand = [deck.drawCard()]
    playerScore = 0
    compScore = 0
    playerhand.append(deck.drawCard())
    comphand.append(deck.drawCard())
    globals.cls()
    displayTable(playerhand, comphand, False)
    playerScore = calculateScore(playerhand)
    compScore = calculateScore(comphand)
    if playerScore == 21 and compScore != 21:
        winnings = choice * 1.5
        globals.profile.wallet += winnings
    elif playerScore != 21 and compScore == 21:
        globals.profile.wallet -= choice
        
    #Player plays
    while True:
        playerChoice = input("\nHit(1) or Stand(2): ")
        if playerChoice == "1":
            playerhand.append(deck.drawCard())
            displayTable(playerhand, comphand, False)
            playerScore = calculateScore(playerhand)
            if playerScore > 21:
                print("Bust!")
                globals.profile.wallet -= choice
                break
        elif playerChoice == "2":

            break
        else:
            print("Invalid choice\n\n")

    #Dealer plays
    if playerScore <= 21:
        while True:
            displayTable(playerhand, comphand, True)
            if compScore < playerScore:
                comphand.append(deck.drawCard())
                compScore = calculateScore(comphand)
                displayTable(playerhand, comphand, True)
                if compScore > 21:
                    print("Dealer Bust!")
                    globals.profile.wallet += choice
                    break
                elif compScore >= playerScore:
                    print("Dealer Stand")
                    if compScore > playerScore:
                        print("Dealer Wins!")
                        globals.profile.wallet -= choice
                    else:
                        print("Tie!")
                    break
            elif compScore > playerScore and compScore <= 21:
                print("Dealer Stand")
                print("Dealer Wins!")
                globals.profile.wallet -= choice
                break
            elif compScore == playerScore:
                print("Tie")
                break
    userAccounts.save()


def displayTable(player, comp, dealerTurn):
    globals.cls()
    if not dealerTurn:
        print("Dealer Hand: " + comp[0] +  " ?\n\n")
        print("Your Hand: ", end='')
        for x in player:
            print(x + "  ", end='')
    else:
        print("Dealer Hand: ", end='')
        for x in comp:
            print(x + "  ", end='')
        print("\n\n")
        print("Your Hand: ", end='')
        for x in player:
            print(x + "  ", end='')
    print("")

def calculateScore(hand):
    count = 0
    numAces = 0
    for x in hand:
        curCard = x[0]
        if curCard == 'J':
            count += 10
        elif curCard == 'Q':
            count += 10
        elif curCard == 'K':
            count += 10
        elif curCard == 'A':
            count += 11
            numAces += 1
        elif curCard == '1':
            count += 10
        else:
            count += int(x[0])
    if count > 21 and numAces > 0:
        count -= 10
        numAces -= 1
    return count

def gameStatus(playerScore, compScore, playerHand, compHand):
    if playerScore == 21 and compScore != 21 and len(playerHand) == 2:
        return "Player Blackjack"
    elif compScore == 21 and playerScore != 21 and len(compHand) == 2:
        return "Comp Blackjack"
    elif playerScore > 21 and compScore < 21:
        return "Player Bust"
    elif playerScore < 21 and compScore > 21:
        return "Comp Bust"
    elif playerScore > 21 and compScore > 21:
        return "Both Bust"
    elif playerScore > compScore:
        return "Player Win"
    elif compScore > playerScore:
        return "Comp Win"
    elif compScore == playerScore:
        return "Tie"
    else:
        return "Unknown Game State"

globals.cls()

while True:
    print("******************************************************************\n")
    print("Welcome " + globals.profile.name + " to Blackjack!\n\n")
    print("You have " + str(globals.profile.wallet) + " coins\n")
    print("Select bet amount")
    print("1. 5 coins")
    print("2. 10 coins")
    print("3. 25 coins")
    print("4. 50 coins")
    print("5. 100 coins")
    print("6. Back to main menu")
    choice = input("Your Selection: ")

    if choice == "1":
        if globals.profile.wallet < 5:
            print("You don't have enough coins")
        else:
            deck = globals.Deck()
            play(deck, 5)
    elif choice == "2":
        if globals.profile.wallet < 10:
            print("You don't have enough coins")
        else:
            deck = globals.Deck()
            play(deck, 10)
    elif choice == "3":
        if globals.profile.wallet < 25:
            print("You don't have enough coins")
        else:
            deck = globals.Deck()
            play(deck, 25)
    elif choice == "4":
        if globals.profile.wallet < 50:
            print("You don't have enough coins")
        else:
            deck = globals.Deck()
            play(deck, 50)
    elif choice == "5":
        if globals.profile.wallet < 100:
            print("You don't have enough coins")
        else:
            deck = globals.Deck()
            play(deck, 100)
    elif choice == "6":
        break

    input("Press Enter to continue...")
    globals.cls()