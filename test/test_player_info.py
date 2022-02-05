from testing_base import *

def PlayerInfo():
    player=Player("Jacob", 200)
    player.hand=[1,2,3,4]
    player.knownCards=[1,2]
    info=player.info()
    return info

def test_PlayerInfo():
    assert "Jacob" in PlayerInfo() and "200" in PlayerInfo() and "[1, 2]" in PlayerInfo() and "[1, 2, 3, 4]" in PlayerInfo()
