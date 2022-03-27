import CardGames
import New_Values


def Player_input(player, deck, dealer):
    
    #Continous loop until player wants to stand
    while True:

        #PRINTS USER HAND AND SUM OF CARDS
        dealer.printPlayerCards(player, True)
        print("\n Your current hand sum is %d" % (New_Values.Hand_Value(player)))

        
        #Input
        
        User_in = input(" \n Enter '1' to HIT and '0' to STAND: ")
       
        #Case: Hit

        if User_in == "1":
            dealer.dealCards(1, [player], deck)

            
            #After hit check to see if hand is over 21
            
            if player.SumCards() > 21: #Hand_Value(player)
                dealer.printPlayerCards(player, True)
                return (False, print("\nBUST!"))

        #Case: Stand

        if User_in== "0":
            return False
        
