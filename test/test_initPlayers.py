import sys

#Change to your own personal path
sys.path.append("C:/Users/Chris/SoftwareEng/CIS322_SP22")

from source.CardGames import *
from source.War import *

def test_initalizePlayers():
    John = Player("John")
    Jane = Player("Jane")
    initializePlayers(John, Jane)

    assert len(John.hand) == 26
    assert len(Jane.hand) == 26