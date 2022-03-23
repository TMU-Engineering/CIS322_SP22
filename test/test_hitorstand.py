from testing_base import *

def test_HoS():

    player = Player("Fred", 500)
    deck = Deck()
    deck.shuffle()

    player.addCard( deck.findCard(5, 'Hearts'))
    player.addCard( deck.findCard(7, 'Spades'))
    player.HitorStand(deck)

test_HoS()