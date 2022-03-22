import CardGames

class BlackJackDealer(CardGames.Dealer):
  def __init__(self, name, money: int = 0):
    self.hand = []
    self.knownCards = []

  def sumDealerCards(self):
    Sum=0
    for i in self.hand:
      Sum=Sum + i.value
    return Sum

  def addCard(self, card: CardGames.Card, isKnown: bool = True):
    self.hand.append(card)
    if isKnown:
      self.knownCards.append(True)
    else:
      self.knownCards.append(False)

  def printDealerCards(self, printShort: bool = False):
    for idx in range(6):
      for i, card in enumerate(self.hand):
        if printShort and i < len(self.hand)-1:
          image = card.shortImage[idx]  if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
      print()

  def dealDealerCards(self, deck: CardGames.Deck):
    self.addCard(deck.getCard())
    self.addCard(deck.getCard(), False)
    return True

  def Dealers_Moves(self, deck):
    print(BlackJackDealer.printDealerCards(self))
    Sum = BlackJackDealer.sumDealerCards(self)          #   Find the sum of the Dealer's hand.

    #   Will be using this command later.
    #Sum = BlackJack.Hand_Value(dealer)

    #   Rule of the Dealer is that the Dealer always hits when their hand is below 16.
    while Sum < 17:
      #   Will be using this command later.
    #while BlackJack.Hand_Value(dealer) < 17:
      print('Dealer Hits')
      BlackJackDealer.dealDealerCards(self,deck)        #   Dealer receives a card.
      print(BlackJackDealer.printDealerCards(self))
      Sum = BlackJackDealer.sumDealerCards(self)        #   Find the sum of the Dealer's new hand.

      #   Will be using this commanad later.
      #Sum = BlackJack.Hand_Value(dealer)

    if Sum <= 21:
    #   Will be using this command later.
    #if BlackJack.Hand_Value(dealer) <= 21:
      print('Dealer Stands\n')

    return Sum
