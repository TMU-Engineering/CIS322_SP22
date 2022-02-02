from testing_base import *

def PlayerInfo():
    player=Player("Jacob", 200)
    player_info = ""
    player_info = player_info + " Player's name: " + player.name + "; Player's money: $" + str(player.money)
    print(player_info)
    return player_info

def test_PlayerInfo():
    assert PlayerInfo() == "Player's name: Jacob; Player's money: $200"
