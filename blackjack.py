'''
Kevin Garcia
Leroy Lints
Giovanni Echave

Time to make: 

I pledge that this program represents my own
program code. I received help from Kevin Garcia,
Leroy Lints, and Giovanni Echave
in designing and debugging my program.

This program is playing blackjack 21 with the user
and the computer.
'''
import random

player_cards = []
dealer_cards = []
BLACKJACK = 21      #used to determine blackjacks(wins)
ACE = 11            #used to adjust value of aces
ACE_CONDENSED = 1       #ace value adjusted down to this number

def main():
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(2, 11))
        aceCheck(dealer_cards)
        if len(dealer_cards) == 2:
            print("Dealer has X &", dealer_cards[1])

    while len(player_cards) != 2:
        player_cards.append(random.randint(2, 11))
        aceCheck(player_cards)
        if len(player_cards) == 2:
            print("You have a total of", str(sum(player_cards)), player_cards)

    #calls the dealer's move function
    dealer_move()
            
    if sum(dealer_cards) == 21:
        print("Dealer has 21 and wins!")
    elif sum(dealer_cards) > 21:
        print("Dealer has busted!")

    #OUTCOME
    stay = False #gets rid of looping stay glitch
    while sum(player_cards) < 21 and stay != True:
        action_taken = str(input("\nWould you like to stay or hit?"))
        if action_taken == "hit":
            player_cards.append(random.randint(2, 11))
            aceCheck(player_cards)
            print("\nYou now have a total of", str(sum(player_cards)), player_cards)
        else:
            stay = True
            print("\nThe dealer has a total of", str(sum(dealer_cards)), "with", dealer_cards)
            print("You have a total of", str(sum(player_cards)), "with", player_cards)
            if sum(dealer_cards) > sum(player_cards):
                print("\nDealer wins!")
                break
            elif sum(dealer_cards) < sum(player_cards):
                print("\nYou win!")
                break

    if sum(player_cards) > 21:
        print("\nYou BUSTED! Dealer wins.")
    elif sum(player_cards) == 21:
        print("\nYou have BLACKJACK! You Win!! 21")
    elif sum(player_cards) == sum(dealer_cards):
        print('You tied!', sum(player_cards), ':', sum(dealer_cards))

#decides the dealer's move
def dealer_move():
    dealer_stay = False  #used to determine if dealer wants to hit or stay

    #loop used to determine if dealer wants to hit or stay
    while dealer_stay == False:
        percent = int((sum(dealer_cards) / BLACKJACK) * 100)
        choice = random.randrange(100) + 1
        if choice > percent:
            dealer_cards.append(random.randint(2, 11))
            aceCheck(dealer_cards)
        else:
            dealer_stay = True

#prevents bust from an ace being worth too much
def aceCheck(hand):
    for x in range(len(hand)):
        card = hand[x]
        if card == ACE:
            if sum(hand) > BLACKJACK:
                hand[x] = ACE_CONDENSED

main()

