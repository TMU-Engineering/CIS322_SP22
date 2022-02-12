
from logging import root
import random
from typing import List
import os

cardImages = []
values = list(range(1,14))
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def find_root_dir():
  cwd = os.getcwd()
  while 'source' not in os.listdir():
    os.chdir('..')
    cwd = os.path.join( cwd, '..')
  return cwd

class Card:
  def __init__(self, suit, value, image, cardBack):
    self.cardBack = cardBack
    self.suit = suit
    self.value = value
    self.image = image
    self.shortImage = []
    for line in self.image:
      self.shortImage.append(line[:4])

  def __eq__(self, other):
    if not type(other) == Card:
      return False
    return self.suit == other.suit and \
      self.value == other.value


CardList = List[Card]

class Deck:
  def __init__(self):
    root_dir = os.path.join( find_root_dir(), 'source')
    cards_file = f'{root_dir}{os.path.sep}playing_cards.txt'
    with open(cards_file, "r") as cards:
      cardBack = []
      for _ in range(6):
        line = cards.readline()
        cardBack.append(line.replace("\n",""))
      card = []
      level = 0
      for line in cards.readlines():
        if len(line) == 1:
          cardImages.append(card)
          level = 0
          card = []
          continue
        card.append(line.replace("\n",""))
        level += 1
      cardImages.append(card)
    
    deck = []
    index = 0
    for suit in suits:
      for value in values:
        deck.append(Card(suit, value, cardImages[index], cardBack))
        index += 1
    
    self.cards = deck
    self.size = len(deck)
    self.cardBack = cardBack
    self.discarded = []

  def __str__(self):
      return (cardImages)

  def shuffle(self):
    random.shuffle(self.cards)

  def getCard(self):
    card = self.cards.pop()
    self.size -= 1
    self.discarded.append(card)
    return card

class Player:
  def __init__(self, name, money: int = 0):
    self.name = name
    self.hand = []
    self.knownCards = []
    self.money = money

  def addMoney(self, amount: int):
    self.money += amount
    return self.money

  def makeBet(self, amount: int):
    if amount > self.money:
      print("%s does not have enough money to make this bet." % self.name)
      return self.money
    self.money -= amount
    return self.money

  def addCard(self, card: Card, isKnown: bool = True):
    self.hand.append(card)
    if isKnown:
      self.knownCards.append(True)
    else:
      self.knownCards.append(False)

  def clearHand(self):
    self.hand = []
    self.knownCards = []

  def showHand(self):
    print(self.hand)

PlayerList = List[Player]

class Dealer:
  def __init__(self):
    pass

  def printCards(self, cards: CardList, showFront: bool, printShort: bool = True):
    for idx in range(6):
      for i, card in enumerate(cards):
        if printShort and i < len(cards)-1:
          image = card.shortImage[idx] if showFront else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if showFront else card.cardBack[idx]
          print(image, end="")
      print()
    
  def printPlayerCards(self, player: Player, printShort: bool = False):
    for idx in range(6):
      for i, card in enumerate(player.hand):
        if printShort and i < len(player.hand)-1:
          image = card.shortImage[idx]  if player.knownCards[i] else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if player.knownCards[i] else card.cardBack[idx]
          print(image, end="")
      print()

  def dealCards(self, numCards: int, players: PlayerList, deck: Deck):
    if numCards * len(players) > deck.size:
      return False
    for player in players:
      for _ in range(numCards):
        player.addCard(deck.getCard())
    return True


  
# NEW CODE BELOW

  def printAllPlayerCards_test(self, players: PlayerList):
  #  TotalPlayers = []
    for i in players:
      self.printPlayerCards(i)


# COMMENTED OUT SETUP CODE      
"""
deck1 = Deck()
player1 = Player("john")
player2 = Player("jeff")
player3 = Player("george")
players2 = [player1, player2, player3]
dealer1 = Dealer()


dealer1.dealCards(2, [player1], deck1)
dealer1.dealCards(3, [player2], deck1)
dealer1.dealCards(4, [player3], deck1)
dealer1.printAllPlayerCards_test(players2)

"""
  


