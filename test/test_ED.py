from testing_base import *

sampleDeck = Deck()
def testCardlen():
    while sampleDeck.size > 0:
        emptyD = sampleDeck.checkEmptyDeck()
        print(emptyD)
        var = sampleDeck.getCard()

    if sampleDeck.size == 0:
        emptyD = sampleDeck.checkEmptyDeck()
        print(emptyD)

testCardlen()