from random import sample
from testing_base import *

sampleDeck = Deck()
sampleDeck.shuffle()
sampleCard = sampleDeck.getCard()
sampleCard.setValue()


print(sampleCard.image,sampleCard.value)