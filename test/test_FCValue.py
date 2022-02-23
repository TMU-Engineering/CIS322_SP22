from random import sample
from testing_base import *

sampleDeck = Deck()
sampleDeck.shuffle()
sampleCard = sampleDeck.getCard()
def test_setValue():
    sampleCard.setValue()
    print(sampleCard.image,sampleCard.value)

test_setValue()