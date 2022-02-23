from testing_base import *

    
def evaluation(player, dealer):

    #Player Busts, Dealer is under or equal to 21
    if player.SumCards()>21 and dealer.SumCards()<=21:
        print('dealer wins!')
        
    #Dealer Busts, Player is under or equal to 21
    elif dealer.SumCards()>21 and player.SumCards()<=21:
        print('Player wins!')

    #Both Dealer and Player are under 21
    elif dealer.SumCards()<=21 and player.SumCards()<=21:

        #Dealer is closer to 21 
        if dealer.SumCards()>player.SumCards():
            print('Dealer wins!')

        #Both hands are equal
        elif dealer.SumCards()==player.SumCards():
            print('tie!')

        #Player is closer to 21
        else:
            print("Player wins!")
        


