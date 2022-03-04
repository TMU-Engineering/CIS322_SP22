from testing_base import *

def test_printBlackjackHand():
    shuffled_deck = Deck()
    shuffled_deck.shuffle()

    Chris = Player('Chris')
    Christopher = Player('Christopher')

    #Horrible implementation to get an ace and a 9 from a deck with a while loop. Honestly kinda ashamed of this:
    while True:
        card1 = shuffled_deck.getCard()
        if card1.value == 1:
            shuffled_deck = Deck()
            shuffled_deck.shuffle()
            break

    while True:
        card2 = shuffled_deck.getCard()
        if card2.value == 9:
            shuffled_deck = Deck()
            shuffled_deck.shuffle()
            break

    while True:
        card3 = shuffled_deck.getCard()
        if card3.value == 13:
            shuffled_deck = Deck()
            shuffled_deck.shuffle()
            break

    print(card1.value, 'Ace')
    print(card2.value, 'Nine')    

    print(card3.value, 'King')

    #adds two aces and a 9, first ace will be worth 11 and second one will be worth 1.
    Chris.addCard(card1)
    Chris.addCard(card1)
    Chris.addCard(card2)

    Christopher.addCard(card3)
    Christopher.addCard(card1)

    #nine + ace(11 because it wont bust) + ace(1 because it would bust)
    assert Chris.printHandValue() == 21

    #add one more time to test that ace = 1 over 21
    Chris.addCard(card1)

    #nine + ace(11) + ace(1) + ace(1)
    assert Chris.printHandValue() == 22

    #king(10) + ace(11) =
    assert Christopher.printHandValue() == 21

