import CardGames
import New_Values

def changeToVisibleAndPrint(player, dealer):
    for i in dealer.hand:
        i.isKnown = True

    print("\nDealer's Hand:\n")
    dealer.printDealerCards()
    print("\nPlayer's Hand:\n")
    dealer.printPlayerCards(player, True)
    
    
def evaluation(player, dealer):
    results=""
    #Player Busts, Dealer is under or equal to 21
    if New_Values.Hand_Value(player)>21 and New_Values.Hand_Value(dealer)<=21:
        print('dealer wins!')
        changeToVisibleAndPrint(player, dealer)
    #Dealer Busts, Player is under or equal to 21
    elif New_Values.Hand_Value(dealer)>21 and New_Values.Hand_Value(player)<=21:
        print('Player wins!')
        changeToVisibleAndPrint(player, dealer)
    #If dealer and player are both over 21
    elif New_Values.Hand_Value(dealer)>21 and New_Values.Hand_Value(player)>21:
        print("Dealer wins!")
        changeToVisibleAndPrint(player, dealer)
    #Both Dealer and Player are under 21
    elif New_Values.Hand_Value(dealer)<=21 and New_Values.Hand_Value(player)<=21:

        #Dealer is closer to 21 
        if New_Values.Hand_Value(dealer)>New_Values.Hand_Value(player):
            #print('Dealer wins!')
            results="Dealer wins!"
            print(results)
            changeToVisibleAndPrint(player, dealer)
        #Both hands are equal
        elif New_Values.Hand_Value(dealer)==New_Values.Hand_Value(player):
            print('tie!')
            changeToVisibleAndPrint(player, dealer)
        #Player is closer to 21
        else:
            print("Player wins!")
            changeToVisibleAndPrint(player, dealer)

    return results

    """

player=CardGames.Player("player1", 0)
dealer=CardGames.Player("dealer", 0)
five = CardGames.Card("Spades", 5, [], [])
three = CardGames.Card("hearts", 3, [], [])
ten = CardGames.Card("hearts", 10, [],[])
queen = CardGames.Card("hearts", 10, [],[])
player.hand.append(five)
player.hand.append(three)
dealer.hand.append(ten)
dealer.hand.append(queen)
evaluation(player, dealer)
"""