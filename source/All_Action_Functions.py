from CardGames import *

def main():
    
    player1 = Player("Joe", 50)
    listofplayers = [player1]
    
###########Added on to previous code because that works best   
    user_in = input("Enter 'c' to call, 'r' to raise, ch to check, or f to fold:")
    if user_in == "c":
        call(listofplayers)
        print(listofplayers[1])
    elif user_in == "r":
        Raise(listofplayers)
        print(listofplayers[1])
        
    elif user_in == "ch": #####New code where player can check by inputing "ch"
        check(listofplayers)
        print(listofplayers[1])##temporary print to test
        
    elif user_in == "f":#####New code where player can enter "f" to fold
        listofplayers.pop()####cant pop player1 because Player object cant be interpreted as an integer
        print(listofplayers)#temporary print to test
        
#####################################Old code, look at action_functions branch for comments on these
    BetAmount=int(10) 

def call(player1): 
    
    BetAmount=int(10)
    
       
    amount=BetAmount 
                      
    
    player1.append(amount)


def Raise(player1):
    
    raise_amount = int(input("Enter amount to raise: "))
    
    BetAmount=int(10)
    
  
    BetAmount=BetAmount+raise_amount 
    player1.append(BetAmount)
####################################
    
###### New functions
def check(player1): #new check function for player to "check"
    
    BetAmount=0
    
    player1.append(BetAmount)##Player has option to stay without betting


main()




