from testing_base import *

def testTurns():
    gamePlayers = []
    player1 = 0
    player2 = 1
    player3 = 2
    player4 = 3
    player5 = 4
    
    gamePlayers.append(player1)
    gamePlayers.append(player2)
    gamePlayers.append(player3)
    gamePlayers.append(player4)
    gamePlayers.append(player5)
    
    assert Dealer.turns(gamePlayers)