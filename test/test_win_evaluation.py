from testing_base import *
from source.win_evaluation import *


def test_evaluation():

    player=Player("player1", 0)
    dealer=Player("dealer", 0)
    five = Card("Spades", 5, [], [])
    three = Card("hearts", 3, [], [])
    ten = Card("hearts", 10, [],[])
    queen = Card("hearts", 10, [],[])

    player.hand.append(five)
    player.hand.append(three)
    dealer.hand.append(ten)
    dealer.hand.append(queen)



    assert evaluation(player, dealer) == results
