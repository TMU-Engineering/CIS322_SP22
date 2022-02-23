from testing_base import *
from source.BlackJackDealer import *

def test_Dealers_Moves():
    deck=Deck()
    deck.shuffle()
    player=Player("player", 200)
    house_dealer=BlackJackDealer("player2", 200)
    dealer=Dealer()
    dealer.dealCards(2, [player, house_dealer], deck)
    dealer.printPlayerCards(house_dealer)
    house_dealer.hand[0].value=int(input("\nEnter value of the Dealer's first card (1-10 - 10 if it is a Face Value Card - Ace can be either a 1 or a 10): "))
    house_dealer.hand[1].value=int(input("\nEnter value of the Dealer's first card (1-10 - 10 if it is a Face Value Card - Ace can be either a 1 or a 10): "))
    house_dealer.Dealers_Moves(deck)

test_Dealers_Moves()
