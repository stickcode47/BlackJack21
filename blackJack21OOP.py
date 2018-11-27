'''
Kevin Garcia
Leroy Lints
Giovanni Echave

Time to make: approx. 25 - 30 hours? 

I pledge that this program represents my own
program code. I received help from Kevin Garcia,
Leroy Lints, and Giovanni Echave
in designing and debugging my program.

This program is playing blackjack 21 with the user
and the computer.
'''
import random

BLACKJACK = 21      #used to determine blackjacks(wins)
ACE = 11            #used to adjust value of aces
ACE_CONDENSED = 1       #ace value adjusted down to this number

class card:
    def __init__(self):
       self.__player = []
       self.__dealer = []

    def dealer_draw(self):
        self.__dealer.append(random.randint(2, 11))

    def player_draw(self):
        self.__player.append(random.randint(2, 11))
    
    def show(self, hand):
        if hand == 'dealer_cards':
            hand = self.__dealer
        else:
            hand = self.__player
        return hand[0 : len(hand)]

    #prevents bust from an ace being worth too much
    def ace_check(self, hand):
        if hand == 'dealer_cards':
            self.__hand = self.__dealer
        else:
            self.__hand = self.__player
        for x in range(len(self.__hand)):
            card = self.__hand[x]
            if card == ACE:
                if sum(self.__hand) > BLACKJACK:
                    self.__hand[x] = ACE_CONDENSED
        
def main():
    mycards = card()
    dealer_cards = mycards.show('dealer_cards')
    player_cards = mycards.show('player_cards')
    while len(dealer_cards) != 2:
        mycards.dealer_draw()
        mycards.ace_check('dealer')
        dealer_cards = mycards.show('dealer_cards')
        if len(dealer_cards) == 2:
            print("Dealer has X &", dealer_cards[1])
            print()

    while len(mycards.show(player_cards)) != 2:
        mycards.player_draw()
        mycards.ace_check(player_cards)
        if len(mycards.show(player_cards)) == 2:
            print("You have a total of", str(sum(mycards.show(player_cards))),mycards.show(player_cards))

    dealer_stay = False  #used to determine if dealer wants to hit or stay

    #loop used to determine if dealer wants to hit or stay
    while dealer_stay == False:
        dealer_cards = mycards.show(dealer_cards)
        percent = int((sum(dealer_cards) / BLACKJACK) * 100)
        choice = random.randrange(100) + 1
        if choice > percent:
            mycards.dealer_draw()
        else:
            dealer_stay = True
            
    if sum(mycards.show(dealer_cards)) == 21:
        print("Dealer has 21 and wins!")
    elif sum(mycards.show(dealer_cards)) > 21:
        print("Dealer has busted!")
    else:
        #OUTCOME
        stay = False #gets rid of looping stay glitch
        while sum(player_cards) < 21 and stay != True:
            action_taken = str(input("\nWould you like to stay or hit?"))
            if action_taken == "hit":
                mycards.player_draw()
                mycards.ace_check(player_cards)
                player_cards = mycards.show(player_cards)
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
        
main()
