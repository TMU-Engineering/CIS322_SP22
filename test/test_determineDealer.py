from testing_base import *

from source.CardGames import *
from source.crazyEights import *


def test_determineDealer():
    unshuffled_deck = Deck()

    playerOne = Player('Chris') #will get 13 of diamonds bc it is unshuffled, is dealer because it is higher
    playerTwo = Player('notChris') #will get 12 of diamonds bc it is unshuffled

    assert determineDealer(playerOne, playerTwo, unshuffled_deck).name == 'Chris'

'''
Testing Code:

test_determineDealer()

unshuffled_deck = Deck()
print(unshuffled_deck.getCard())
print(unshuffled_deck.getCard())
'''