from testing_base import *

def test_noCardsLeft():
    StarterDeck = Deck()
    DiscardPile = Deck()
    Dealer1 = Dealer()
    StarterDeck.shuffle()
    player1 = Player("john")
    player2 = Player("jeff")
    Dealer1.dealCards(2, [player1], StarterDeck)
    Dealer1.dealCards(3, [player2], StarterDeck)

    noCardsLeftFunction()
