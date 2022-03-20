from testing_base import *

def test_find_card_match():
    deck1 = Deck()
    deck1.shuffle()
    player1 = Player("john")
    player2 = Player("jeff")
    player1CardList = []
    player2CardList = []

    findCardMatch()
