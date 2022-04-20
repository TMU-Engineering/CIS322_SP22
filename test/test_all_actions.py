from testing_base import *

###I copy and paste regular code because importing doesn't work


def check(player1): #new check function for player to "check"
    
    BetAmount=0
    
    player1.append(BetAmount)##Player has option to stay without betting


def test_all_actions():
    player1 = Player("Joe", 50)
    listofplayers = [player1]
    
    check(listofplayers)
    assert listofplayers[1]==0
    print(listofplayers[1])

test_all_actions()

def test_Actions():
    player1 = Player("Joe", 50)
    listofplayers = [player1]


    user_in="f"

    if user_in == "f":
        listofplayers.pop()
       
    assert listofplayers==[]
    print(listofplayers)
test_Actions()
