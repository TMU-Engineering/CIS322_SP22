from testing_base import *

def test_CardPairs_True():

    deck = Deck()
    deck.shuffle()

    # suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    player1 = Player("Bob")

    card1 = deck.findCard(12, 'Hearts', remove=False) 
    card2 = deck.findCard(8, 'Hearts', remove=False) 
    card3 = deck.findCard(12, 'Clubs', remove=False) 
    card4 = deck.findCard(9, 'Hearts', remove=False) 
    card5 = deck.findCard(3, 'Hearts', remove=False) 
    player1.addCard(card1)
    player1.addCard(card2)
    player1.addCard(card3)
    player1.addCard(card4)
    player1.addCard(card5)

    assert player1.HasPair() == True
    
def test_CardPairs_False():

    deck = Deck()
    deck.shuffle()

    # suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    player1 = Player("Bob")

    card1 = deck.findCard(12, 'Hearts', remove=False) 
    card2 = deck.findCard(8, 'Hearts', remove=False) 
    card3 = deck.findCard(4, 'Clubs', remove=False) 
    card4 = deck.findCard(9, 'Hearts', remove=False) 
    card5 = deck.findCard(3, 'Hearts', remove=False) 
    player1.addCard(card1)
    player1.addCard(card2)
    player1.addCard(card3)
    player1.addCard(card4)
    player1.addCard(card5)

    assert player1.HasPair() == False