import sys

sys.path.append("C:/Users/Chris/SoftwareEng/CIS322_SP22")

from source.CardGames import *

def initializePlayers(p1, p2):
    #Takes input of two players
    #Makes a shuffled deck and deals 26 cards to each player
    #initializes dealer as well.

    shuffled_deck = Deck()
    shuffled_deck.shuffle()

    dealer = Dealer()

    playerlist = [p1, p2]

    dealer.dealCards(26, playerlist, shuffled_deck)

    #Below are commands to show shuffled deck, however the shuffle function is already builtin and tested and therefore does not need further testing.
    #dealer.printPlayerCards(p1, True)
    #dealer.printPlayerCards(p2, Ture)

