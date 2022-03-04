from testing_base import *

def test_win_eval_function():

    deck1 = Deck()
    dealer = Player("john")
    player2 = Player("jeff")
    player3 = Player("george")
    player4 = Player("jack")
    blackjack_player_list = [dealer, player2, player3, player4]
    dealer1 = Dealer()

    dealer.addCard( deck1.findCard(13, "Hearts", remove=False) )
    dealer.addCard( deck1.findCard(10, "Hearts", remove=False) )
    print(f"{dealer.name}'s hand total is {dealer.getHandValue()}")

    player2.addCard( deck1.findCard(1, "Clubs", remove=False) )
    player2.addCard( deck1.findCard(10, "Spades", remove=False) )
    print(f"{player2.name}'s hand total is {player2.getHandValue()}")

    player3.addCard( deck1.findCard(9, "Diamonds", remove=False) )
    player3.addCard( deck1.findCard(1, "Hearts", remove=False) )
    print(f"{player3.name}'s hand total is {player3.getHandValue()}")

    player4.addCard( deck1.findCard(11, "Spades", remove=False) )
    player4.addCard( deck1.findCard(1, "Diamonds", remove=False) )
    print(f"{player4.name}'s hand total is {player4.getHandValue()}")

    winners = dealer1.winEvaluation(blackjack_player_list)

    for winner in winners:
        print(f'{winner.name} wins')
    
    assert winners[0].name == player2.name and winners[1].name == player4.name