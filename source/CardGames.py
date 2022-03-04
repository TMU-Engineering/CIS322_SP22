
from functools import total_ordering
from logging import root
from operator import attrgetter
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

  def setValue(self):
    if self.value > 10:
      self.value = 10
    return self.value

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

  def __str__(self):
    return "Player's name is % s, known cards are % s, and money is % d." % (self.name, self.knownCards, self.money)
    
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

  def printHandValue(self):
    totalPoints = 0
    aces = 0

    for i in self.hand:
      if int(i.value) > 10:
        totalPoints += 10
      elif int(i.value) > 1:
        totalPoints += int(i.value)
      
      if int(i.value) == 1:
        aces += 1
    
    while aces != 0:
      if totalPoints > 10:
        totalPoints += 1
        aces -= 1
      elif totalPoints <= 10:
        totalPoints += 11
        aces -= 1
    return totalPoints  
    

  def HasPair(self):
    FoundPair = False
    for i in range(len(self.hand)):
      for j in range(i+1, len(self.hand)):
          x = self.hand[i].value 
          y = self.hand[j].value 
          if x == y:
            FoundPair = True
    
    return FoundPair

  def sumOfCards(self):
    total = self.hand[0].value
    for i in range(1,len(self.hand)):
        total = total + self.hand[i].value
    return total

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
      
  def winEvaluation(self, players: PlayerList):
    winner_list = []  
    loser_list = []
    winner_list.append(dealer_total)
    for u in players:
      if player_total == dealer_total:
        winner_list.append(u)
      if player_total > dealer_total:
        winner_list.append(u)
        winner_list.remove(dealer_total)
      if player_total < dealer_total:
        loser_list.append(u) 
      print("All players with the total value of " + max(winner_list) + "win the round.")

  def printAllPlayerCards_test(self, players: PlayerList):
    for i in players:
      print( i.name )
      self.printPlayerCards(i)
      print( '--------------------------')
  

def findHighCard(CardList):
    return max(CardList, key=attrgetter('value'))

    #If needed, the below function acccounts for suits in Clubs, Diamonds, Hearts, Spades (lowest -> highest) order
    #It sorts using max because this common suit order is in alphabetical order

    #return max(CardList, key=attrgetter('value', 'suit'))
