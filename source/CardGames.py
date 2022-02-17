
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

  def findCard(self, val: int, suit: str, remove: bool=True):
    foundCard = None
    for idx, card in enumerate( self.cards ):
      if card.suit == suit and card.value == val:
        foundCard = self.cards.pop(idx) if remove else card
        break
    return foundCard

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

  def highCard(self):
    curr_high=self.hand[0]
    for i in range(len(self.hand)):
       if curr_high.value < self.hand[i].value:
           curr_high=self.hand[i]
    return curr_high.value

  def SumCards(self):
    Sum=0
    for i in self.hand:
      Sum=Sum + i.value
    return Sum

  def info(self):
    info=""
    name = "Player's name: " + self.name
    money = self.name+ "'s money: $"+str(self.money)
    hand = self.name + "'s hand: " + str(self.hand)
    knownHand = self.name + "'s known hand: " + str(self.knownCards)
    info=info + str(name) + "\n" + str(money) + "\n" + str(hand) + "\n" + str(knownHand)
    return info

  def getPairs(self):
    pairList = []
    for x in self.hand:
      for y in self.hand:
        if x.value == y.value:
          if x.__eq__(y)== False and ([y,x] in pairList) == False:
            pairList.append([x,y])


    return pairList

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

# Create a display output (prints) for multiple player's hands of cards.
# This should output the hands such that it is unambiguous whose cards are whose.
  def printAllPlayersCards(self, players: PlayerList, printShort: bool = False):

    # Loop Through Each Player in the List of Players
    for player in players:

      # Print the player's name
      print(player.name)

      # Prints Player's Cards
      for idx in range(6):
        for i, card in enumerate(player.hand):
          if printShort and i < len(player.hand)-1:
            image = card.shortImage[idx] if player.knownCards[i] else card.cardBack[idx]
            print(image, end="")
          else:
            image = card.image[idx] if player.knownCards[i] else card.cardBack[idx]
            print(image, end="")
        print()
      print("""
      ------------------------------
      """)

  def dealCards(self, numCards: int, players: PlayerList, deck: Deck):
    if numCards * len(players) > deck.size:
      return False
    for player in players:
      for _ in range(numCards):
        player.addCard(deck.getCard())
    return True

