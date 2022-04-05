from CardGames import *

def main():
    
    player1 = Player("Joe", 50)
    listofplayers = [player1]
    
    ########### This code should be added to an actual game player function
    user_in = input("Enter 'c' to call, 'r' to raise:")
    if user_in == "c":
        call(listofplayers)
        print(listofplayers[1])
    elif user_in == "r":
        Raise(listofplayers)
        print(listofplayers[1])
########### another rough code example. May need to be edited to call function to
              # individual players for which code hasn't been made for yet

    BetAmount=int(10) #sample bet amout

def call(player1): #matches current bet amount and continues playing
    
    BetAmount=int(10)#sample bet amount
    
    ######## code will need to be altered when merged, this is sample code    
    amount=BetAmount #because I dont know the function this is a sample function
                         #enter correct function when merging code
    
    player1.append(amount)
    ########

def Raise(player1):
    #user enters amount they wish to raise
    raise_amount = int(input("Enter amount to raise: "))
    
    BetAmount=int(10)#sample bet amount
    
    #adds raise to current bet amount
    BetAmount=BetAmount+raise_amount #BetAmount will be replaced with correct function 
    player1.append(BetAmount)
    
main()

