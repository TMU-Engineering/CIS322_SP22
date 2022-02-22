from testing_base import *

def test_win_eval_function():

    deck1 = Deck()
    dealer = Player("john")
    player2 = Player("jeff")
    player3 = Player("george")
    player4 = Player("jack")
    blackjack_player_list = [dealer, player2, player3, player4]
    dealer1 = Dealer()

    dealer1.dealCards(2, [dealer, player2, player3, player4], deck1)

    dealer1.winEvaluation(blackjack_player_list)