from testing_base import *

################ I copy and paste my regular code because importing the file doesnt work
################    
def call(player1): #matches current bet amount and continues playing
    
    BetAmount=int(10)#sample bet amount
    
    ######## code will need to be altered when merged, this is sample code    
    amount=BetAmount #because I dont know the function this is a sample function
                         #enter correct function when merging code
    
    player1.append(amount)
    ########

def Raise(player1):
    #user enters amount they wish to raise
    raise_amount = int(10)
    
    BetAmount=int(10)#sample bet amount
    
    #adds raise to current bet amount
    BetAmount=BetAmount+raise_amount #BetAmount will be replaced with correct function 
    player1.append(BetAmount)
    
###############
###############

def test_actions():
    BetAmount=int(10)
    player1 = Player("Joe", 50)
    listofplayers = [player1]
    
    call(listofplayers)
    assert listofplayers[1]==10

test_actions()

def test_Actions():
    BetAmount=int(10)
    player1 = Player("Joe", 50)
    listofplayers = [player1]    
    Raise(listofplayers)    
    assert listofplayers[1]==20
test_Actions()
    

