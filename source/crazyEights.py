import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source import CardGames

#input has two players and a deck
#draws two cards from deck
#output returns player that had the higher card
def determineDealer(p1, p2, Deck):
    p1Card = Deck.getCard()
    p2Card = Deck.getCard()

    cardlist = [p1Card, p2Card]
    if p1Card == CardGames.findHighCard(cardlist):
        return p1
    else:
        return p2
