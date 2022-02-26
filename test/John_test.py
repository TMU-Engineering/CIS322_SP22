#   Create a display output (prints) for multiple player's hands of cards.
#   This should output the hands such that it is unambiguous whose cards are whose.
#   (hint: the Dealer class can print a list of cards.
#   Treat each "player's hand" as simple a list of cards)

from testing_base import *

def test_printAllPlayersCards():

    dealer = Dealer()
    deck = Deck()
    deck.shuffle()


    player1 = Player('John')
    player2 = Player('Jacob')
    player3 = Player('Jonathan')
    player4 = Player('Andrew')
    player5 = Player('Joe')

    dealer.dealCards( 5, [player1, player2, player3, player4, player5], deck)
    print()
    print(player1.name)
    dealer.printCards(player1.hand, True)
    print()
    print(player2.name)
    dealer.printCards(player2.hand, True)
    print()
    print(player3.name)
    dealer.printCards(player3.hand, True)
    print()
    print(player4.name)
    dealer.printCards(player4.hand, True)
    print()
    print(player5.name)
    dealer.printCards(player5.hand, True)

    print("""
------------------------------
Testing My Code
------------------------------
""")

    PlayerList = [player1, player2, player3, player4, player5]

    dealer.printAllPlayersCards(PlayerList, True)

test_printAllPlayersCards()
