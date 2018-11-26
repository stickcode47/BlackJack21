import random

#CARD
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print ("{} of {}".format(self.value, self.suit)) #MAKES FULL CARD VALUE
#DECK
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Hearts","Diamonds","Clubs","Spades"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))#ADDS ALL 52 CARDS TO A DECK

    def show(self):
        for c in self.cards:
            c.show()#SHOWS THE WHOLE DECK

    def shuffle(self):
        for x in range(len(self.cards)-1, 0, -1):
            y = random.randint(0, x)
            self.cards[x], self.cards[y] = self.cards[y], self.cards[x]#SHUFFLES THE WHOLE DECK

    def drawCard(self):
        return self.cards.pop()#REMOVES CARD FROM DECK
#PLAYER
class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.drawCard())#DRAWS CARD FROM DECK AND ADDS TO HAND
        return self

    def show(self):
        for card in self.hand:
            card.show()#SHOWS THE CARD IN THE HAND

#TESTING THE CLASSES BEFORE IMPORTING INTO GAME
'''
deck = Deck()
deck.shuffle()

dealer = Player("Dealer")
dealer.draw(deck).draw(deck)
dealer.show()
