from testing_base import *

currentSuit = "Spade"

sampleDeck = Deck()
sampleeightCard = sampleDeck.findCard(8, "Spades", True)


def test_eightCard(card1):
    newSuit = card1.eightCard()
    print("The new suit for the stack is: " + newSuit)

#set suit for the rest of the game as newSuit

test_eightCard(sampleeightCard)