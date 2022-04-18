from testing_base import *
from source.CardGames import *
from source.PokerSetup import *
def test_blinds():
    Game = PokerGameSetup("game", 100)
    Joe = Player('Joe', 100)
    John = Player('John', 100)
    Jacob = Player('Jacob', 100)
    Andrew = Player('Andrew', 100)
    Player_List = [Joe, John, Jacob, Andrew]
    BlindList = Game.Blinds(Player_List, 1)
    
    assert(len(BlindList)) == 2

    
    

test_blinds()
    
   
