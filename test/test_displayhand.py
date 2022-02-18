from testing_base import *

def test_something():

  deck1 = Deck()
  player1 = Player("john")
  player2 = Player("jeff")
  player3 = Player("george")
  player_hand_list = [player1, player2, player3]
  dealer1 = Dealer()
  
  dealer1.dealCards(5, [player1, player2, player3], deck1)

  
  dealer1.printAllPlayerCards_test(player_hand_list)


  


