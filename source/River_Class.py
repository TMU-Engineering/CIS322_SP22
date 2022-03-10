from CardGames import *

class River:
    def __init__(self, deck):
        self.hand = []
        self.deck = deck

    def roundOne(self):
        self.hand.append(deck.getCard())
        self.hand.append(deck.getCard())
        self.hand.append(deck.getCard())
        return self.hand

    def roundTwo(self):
        discard=deck.getCard()
        self.hand.append(deck.getCard())
        return self.hand

    def roundThree(self):
        discard=deck.getCard()
        self.hand.append(deck.getCard())
        return self.hand

    def printHand(self, cards: CardList, showFront: bool, printShort: bool = True):
        for idx in range(6):
          for i, card in enumerate(cards):
            if printShort and i < len(cards)-1:
              image = card.shortImage[idx] if showFront else card.cardBack[idx]
              print(image, end="")
            else:
              image = card.image[idx] if showFront else card.cardBack[idx]
              print(image, end="")
          print()
          
deck=Deck()
River=River(deck)
River.roundOne()
River.printHand(River.hand, True)
River.roundTwo()
River.printHand(River.hand, True)
River.roundThree()
River.printHand(River.hand, True)
