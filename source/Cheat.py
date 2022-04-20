import sys

sys.path.append("C:/Users/peter/SoftwareEng/CIS322_SP22")

from source.CardGames import *

def initializePlayers(p1, p2, p3, p4):

    shuffled_deck = Deck()
    shuffled_deck.shuffle()

    dealer = Dealer()

    Playerlist = [p1, p2, p3, p4]

    dealer.dealCards(13, Playerlist, shuffled_deck)