from testing_base import *
def test_sum():
    playerOne=Player('johnny', 6)
    three=Card('Spade', 1, [], [])
    four=Card('Diamond', 1, [], [])
    seven=Card('Hearts', 1, [], [])
    five=Card('Spade', 1, [], [])
    nine=Card('Heart', 2, [], [])
    
    playerOne.hand.append(three)
    playerOne.hand.append(four)
    playerOne.hand.append(seven)
    playerOne.hand.append(five)
    playerOne.hand.append(nine)
    assert playerOne.sumOfCards()==6