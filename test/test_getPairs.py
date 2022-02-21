from sqlalchemy import null
from testing_base import *


def test_getPairs():
    np = Player("test", 0)
    
    ace = Card("Clubs", 14, [], [])
    queen = Card("Hearts", 12, [], [])
    queen2 = Card("Clubs", 12, [], [])
    two = Card("Spades", 2, [], [])
    five = Card("Diamonds", 5, [], [])
    np.hand.append(ace)
    np.hand.append(queen)
    np.hand.append(queen2)
    np.hand.append(two)
    np.hand.append(five)
    print("hand: ")
    for i in np.hand:
        print(i.value)

    pairsList = np.getPairs()
    print(pairsList)
    assert pairsList[0] == [queen, queen2]

