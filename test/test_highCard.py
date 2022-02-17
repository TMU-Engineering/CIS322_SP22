from testing_base import *

def test_highCard():
    randomCardList = []
    intCardList = []
    
    shuffled_deck = Deck()
    shuffled_deck.shuffle()

    for i in range(5):
        randomCardList.append(shuffled_deck.getCard())

        #Makes an integer card list that we can use to compare values later
        currentCard_int = int(randomCardList[i].value)
        intCardList.append(currentCard_int)

        #Prints out each card iterated for debug purposes 
        #print(randomCardList[i].value, randomCardList[i].suit)

    assert int(findHighCard(randomCardList).value) == max(intCardList)

#running for non-pytest debugging
#test_highestCard()