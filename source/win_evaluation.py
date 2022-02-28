from testing_base import *

    
def evaluation(player, dealer):
    results=""
    #Player Busts, Dealer is under or equal to 21
    if player.SumCards()>21 and dealer.SumCards()<=21:
        print('dealer wins!')
        
    #Dealer Busts, Player is under or equal to 21
    elif dealer.SumCards()>21 and player.SumCards()<=21:
        print('Player wins!')
        
    #If dealer and player are both over 21
    elif dealer.SumCards()>21 and player.SumCards()>21:
        print("Dealer wins!")
        
    #Both Dealer and Player are under 21
    elif dealer.SumCards()<=21 and player.SumCards()<=21:

        #Dealer is closer to 21 
        if dealer.SumCards()>player.SumCards():
            #print('Dealer wins!')
            results="Dealer wins!"
            print(results)

        #Both hands are equal
        elif dealer.SumCards()==player.SumCards():
            print('tie!')

        #Player is closer to 21
        else:
            print("Player wins!")
        

    return results

player=Player("player1", 0)
dealer=Player("dealer", 0)
five = Card("Spades", 5, [], [])
three = Card("hearts", 3, [], [])
ten = Card("hearts", 10, [],[])
queen = Card("hearts", 10, [],[])
player.hand.append(five)
player.hand.append(three)
dealer.hand.append(ten)
dealer.hand.append(queen)
evaluation(player, dealer)
