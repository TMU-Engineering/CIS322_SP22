import sys
from testing_base import *

from source.CardGames import *
from source.Cheat import *

def test_initalizePlayers():
    John = Player("John")
    Jane = Player("Jane")
    Joe = Player("Joe")
    Jay = Player("Jay")
    initializePlayers(John, Jane, Joe, Jay)

    assert len(John.hand) == 13
    assert len(Jane.hand) == 13
    assert len(Joe.hand) == 13
    assert len(Jay.hand) == 13