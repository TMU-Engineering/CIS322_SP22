from testing_base import *


def printAllPlayerCards_test(self):
  deck1 = Deck()
  player1 = Player("john")
  player2 = Player("jeff")
  player3 = Player("george")
  dealer1 = Dealer()


  dealer1.dealCards(2, [player1], deck1)
  dealer1.dealCards(3, [player2], deck1)
  dealer1.dealCards(4, [player3], deck1)

  TotalPlayers = [player1, player2, player3]
  for i in TotalPlayers:
    self.printPlayerCards(i)


  


