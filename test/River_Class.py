from CardGames import *

class River:
    ### First start with the river and the deck
    def __init__(self, deck):
        self.river = []
        self.deck = deck
        
    ### In the first turn, three cards are shown
    def roundOne(self, deck):
        self.river.append(deck.getCard())
        self.river.append(deck.getCard())
        self.river.append(deck.getCard())
        return self.river

    ### In the second turn, another card is added after a card is discarded
    def roundTwo(self, deck):
        discard=deck.getCard()
        self.river.append(deck.getCard())
        return self.river

    ### In the third turn, the final card is added after a card is discarded
    def roundThree(self, deck):
        discard=deck.getCard()
        self.river.append(deck.getCard())
        return self.river

    ### This function allows someone to print the river at anytime of the game
    def printRiver(self, cards: CardList, showFront: bool, printShort: bool = True):
        for idx in range(6):
          for i, card in enumerate(cards):
            if printShort and i < len(cards)-1:
              image = card.shortImage[idx] if showFront else card.cardBack[idx]
              print(image, end="")
            else:
              image = card.image[idx] if showFront else card.cardBack[idx]
              print(image, end="")
          print()
          
