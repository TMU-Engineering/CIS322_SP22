from testing_base import *
from source.Straight_hand import *
from source.Find_Flush import *
from source.River_Class import *

def test_main():
    Joe = Player("Joe")

    eight = Card("Diamonds", 8, [], [])
    ten = Card("Diamonds", 10, [], [])

    Joe.hand.append(eight)
    Joe.hand.append(ten)
    
    assert straight(Joe, River) == (True, 13)
    assert straight_flush(Joe, River)  == (True, 13)
    
test_main()
