import random

player_cards = []
dealer_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have a total of", str(sum(player_cards)), player_cards)

if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

#OUTCOME
while sum(player_cards) < 21:
    action_taken = str(input("\nWould you like to stay or hit?"))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("\nYou now have a total of", str(sum(player_cards)), player_cards)
    else:
        print("\nThe dealer has a total of", str(sum(dealer_cards)), "with", dealer_cards)
        print("You have a total of", str(sum(player_cards)), "with", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("\nDealer wins!")
            break
        else:
            print("\nYou win!")
            break

if sum(player_cards) > 21:
    print("\nYou BUSTED! Dealer wins.")
elif sum(player_cards) == 21:
    print("\nYou have BLACKJACK! You Win!! 21")
