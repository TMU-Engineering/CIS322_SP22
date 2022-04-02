from CardGames import *


def Player_Setup(Playerlist):

    #Finding out number of players with an error for invalid inputs
    NumOfPlayers = input("How many people are playing? ")


    #A loop for creating various players with name and money amounts
    try: 
        for player in range(int(NumOfPlayers)):
            
            playername = input("\nEnter player {}'s name: ".format(player+1))
            playermoney = int(input("\nEnter the amount of money for player {} to start with: ".format(player+1)))
                
            playername = Player(playername, playermoney)
            
            #Appending each player to a list
            Playerlist.append(playername)
            
    except ValueError:
            print("\nPlease enter an integer for the amount of players AND the amount of money added...")

            
