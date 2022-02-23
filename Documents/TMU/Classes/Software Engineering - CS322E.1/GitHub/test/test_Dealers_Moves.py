from testing_base import *
from source.BlackJackDealer import *

def test_Dealers_Moves(self):
    dealer = BlackJackDealer("Dealer", 0)
    nine = Card("Hearts", 9, [], [])
    eight = Card("Clubs", 8, [], [])
    BlackJackDealer.hand.append(nine)
    BlackJackDealer.hand.append(eight)
    assert(BlackJackDealer.dealersTurn()==17)

test_Dealers_Moves(self)
