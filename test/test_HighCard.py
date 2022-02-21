from testing_base import *


def test_HighCardFunc():
    player1 = Player("player1", 0)
    ace = Card("Hearts", 14, [], [])
    four = Card("Clubs", 3, [], [])
    seven = Card("Spades", 6, [], [])
    jack = Card("Hearts", 11, [], [])
    king = Card("Diamonds", 13, [], [])
    player1.hand.append(ace)
    player1.hand.append(four)
    player1.hand.append(seven)
    player1.hand.append(jack)
    player1.hand.append(king)
    assert(Player.highCard(player1)==14)
   


