import CardGames
import New_Values

class BlackJackDealer(CardGames.Dealer):
  def __init__(self, name, money: int = 0):
    self.hand = []
    self.knownCards = []

  def sumDealerCards(self):
    Sum=0
    for i in self.hand:
      if i.value <= 10:
        Sum=Sum + i.value
      elif i.value > 10 and i.value < 14:
        Sum=Sum + 10
      else:
        Sum=Sum+11
    return Sum

  def addCard(self, card: CardGames.Card, isKnown: bool = True):
    self.hand.append(card)
    if isKnown:
      self.knownCards.append(True)
    else:
      self.knownCards.append(False)

  def printDealerCards(self, printShort: bool = False):
    for idx in range(6):#len(self.hand)):
      for i, card in enumerate(self.hand):
        if printShort and i < len(self.hand)-1:
          image = card.shortImage[idx]  if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
      print()
      

  def dealDealerCards(self, deck: CardGames.Deck, showCard: False):
    self.addCard(deck.getCard(), showCard)
    #self.addCard(deck.getCard(), False)
    return True

  def Dealers_Moves(self, deck):

    print(BlackJackDealer.printDealerCards(self))
    dealSum = New_Values.Hand_Value(self)   #   Find the sum of the Dealer's hand.
    print(f"Dealer Sum: {dealSum}")
    #   Will be using this command later.
    #Sum = BlackJack.Hand_Value(dealer)

    #   Rule of the Dealer is that the Dealer always hits when their hand is below 16.
    while dealSum < 17:
      #   Will be using this command later.
    #while BlackJack.Hand_Value(dealer) < 17:
      print('Dealer Hits')
      BlackJackDealer.dealDealerCards(self,deck, False)        #   Dealer receives a card.
      print(BlackJackDealer.printDealerCards(self))
      print(f"Dealer Sum: {New_Values.Hand_Value(self)}")

      dealSum = New_Values.Hand_Value(self)        #   Find the sum of the Dealer's new hand.

      #   Will be using this commanad later.
      dealSum = New_Values.Hand_Value(self)

    if dealSum <= 21:
    #   Will be using this command later.
      print('Dealer Stands\n')
      print(BlackJackDealer.printDealerCards(self))
      print(f"Dealer Sum: {New_Values.Hand_Value(self)}")


    return dealSum
