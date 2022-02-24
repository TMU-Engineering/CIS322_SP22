from sqlalchemy import null
from testing_base import *
from source.BlackJack import *

def test_gameController():
    d = Deck()
    p = Player('Player1', 0)
    d1 = Dealer()
    bj = BlackJack(d, p, d1, 0)

    assert str(bj) != null
    