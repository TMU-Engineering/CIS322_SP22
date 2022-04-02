from testing_base import *
from source.PokerPlayer4Functions import *

def test_4_Functions():
    deck=Deck()
    deck.shuffle()
    player=Player("player", 200)
    player2=PokerPlayer("player2", 200)
    dealer=Dealer()
    dealer.dealCards(7, [player, player2], deck)
    dealer.printPlayerCards(player2)
    player2.highCard(deck)
    player2.getPairs(deck)
    player2.get2Pairs(deck)
    player2.threeOfAKind(deck)

test_4_Functions()
