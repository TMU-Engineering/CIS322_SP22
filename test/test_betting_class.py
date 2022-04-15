from CardGames import *
from Betting_Class import *

def testing():    
    player1=Player("Player1", 200)
    player2=Player("Player2", 200)
    List=[player1, player2]
    pot=betting(List)
    player1.makeBet(20, pot)
    player2.makeBet(20, pot)
    return pot.square(List)

x = testing()

def test_betting_class:
    assert x == True
