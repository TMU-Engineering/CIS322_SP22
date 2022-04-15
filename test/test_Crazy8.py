from testing_base import *

currentSuit = "Spade"

sampleDeck = Deck()
sampleeightCard = sampleDeck.findCard(8, "Spades", True)


def test_eightCard():
    newSuit = sampleeightCard.eightCard("Spades")
    print("The new suit for the stack is: " + newSuit)

#set suit for the rest of the game as newSuit

test_eightCard()