
from testing_base import *
from source.Player_input import *


def Test(): 
    Joe = Player("Joe", 500)

    BlackJackDealer = Dealer()

    BlackJackDeck = Deck()


    BlackJackDealer.dealCards(2, [Joe], BlackJackDeck)

    BlackJackDealer.printPlayerCards(Joe, True)
    #Player_input(Joe, BlackJackDeck, BlackJack)
    
    Player_input(Joe, BlackJackDeck, BlackJackDealer)
    
    assert len(Joe.hand) == 3

    Player_input(Joe, BlackJackDeck, BlackJackDealer)

    assert len(Joe.hand) == 3
    
Test()
