from testing_base import *
from io import StringIO

#Setup
player = Player("John Smith")
deck = Deck()
player.addCard( deck.findCard(5, 'Hearts'))
player.addCard( deck.findCard(7, 'Spades'))
player.addCard( deck.findCard(1, 'Clubs'))
player.addCard( deck.findCard(8, 'Diamonds'))

def test_cheatBet():
    outputList = player.cheatBet('Ace')


    assert str(outputList) == "[5 of Hearts, 1 of Clubs]" #user function 1, 2, then 0
#test_cheatBet()