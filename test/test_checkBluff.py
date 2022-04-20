from testing_base import *

sampleDeck = Deck()

firstEight = sampleDeck.findCard(8, "Spades", True)
secondEight = sampleDeck.findCard(8, "Hearts", True)
thirdEight = sampleDeck.findCard(8, "Diamonds", True)
firstFour = sampleDeck.findCard(4, "Spades", True)

sampleList = [firstEight, secondEight, thirdEight, firstFour]


def test_checkBluff():
    checkFalse = sampleDeck.checkBluff(8, 4, sampleList)
    checkTrue = sampleDeck.checkBluff(8, 3, sampleList)
    print(checkFalse, checkTrue)

test_checkBluff()
