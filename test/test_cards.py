from testing_base import *

def compare_shuffled_deck():
    ordered_deck = Deck()
    shuffled_deck = Deck()
    shuffled_deck.shuffle()

    dealer = Dealer()

    num_matches = 0
    for idx, card in enumerate(ordered_deck.cards):
        if card == shuffled_deck.cards[idx]: num_matches += 1

    return num_matches

# def test_shuffle():
#     assert compare_shuffled_deck() == 0

def test_find_card():
    deck = Deck()
    deck.shuffle()

    # suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    
    foundCards = []

    foundCards.append( deck.findCard(10, suits[0], remove=False) )
    foundCards.append( deck.findCard(11, suits[0], remove=False) )
    foundCards.append( deck.findCard(12, suits[0], remove=False) )
    foundCards.append( deck.findCard(13, suits[0], remove=False) )
    foundCards.append( deck.findCard(1, suits[0], remove=False) )

    dealer = Dealer()
    dealer.printCards( foundCards, True)

    valid = True
    for idx, card in enumerate( foundCards ):
        if idx < 4:
            valid &= card.value == idx + 10 and card.suit == "Spades"
        else:
            valid &= card.value == 1 and card.suit == "Spades"

    assert( valid )


