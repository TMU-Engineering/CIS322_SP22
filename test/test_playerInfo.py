from testing_base import *

def test_PlayerDetails():
    testPlayer1 = Player("Joanna")
    testPlayer2 = Player("Peter")
    testPlayer3 = Player("Chris")
    testPlayer4 = Player("Jayden")
    testPlayer5 = Player("Ryan")

    Players = [testPlayer1, testPlayer2, testPlayer3, testPlayer4, testPlayer5]

    for a in Players:
        print(a)