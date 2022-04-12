from testing_base import *

def add_player_cards():
    deck = Deck()
    dealer = Dealer()
    deck.shuffle()
      
    #Choose one player's hand
    player1 = Player("jayden")
    player2 = Player("chris")
    PlayerList = [player1, player2]
    dealer.dealCards(5, PlayerList, deck)
    dealer.printCards(player1.hand, True)
    print(values)
    assert len(PlayerList) == 2

add_player_cards()