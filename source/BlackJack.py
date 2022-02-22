# This file is the game controller for BlackJack.
# It is where we will link all the components together
# and manage the game state.
from ast import Return
from msilib.schema import Class
import CardGames

#from source.CardGames import *


class BlackJack():
    # This is where the games objects and variables will be instantiated
    def __init__(self, gameDeck, gamePlayer, gameDealer, gamePot):
        print('placeholder0')
        self.gameDeck = gameDeck
        self.gamePlayer = gamePlayer
        self.gameDealer = gameDealer
        self.gamePot = gamePot
    
    def __str__(self):
        return str(self.gameDeck) + str(self.gamePlayer) + str(self.gameDealer) + str(self.gamePot)

    # This is where all the game functions including 'runGameLoop()' will be called
    def main(self):
        print('placeholder1')
        
    # This will run the game loop
    def runGameLoop(self):
        print('placeholder2')
        print(self)

    # This function will handle the game win/loose and display to the user who won
    def endGame(self):
        print('placeholder3')

# This is where the instance of the blackjack game will be made
deck = CardGames.Deck()
player = CardGames.Player('Player1', 500)
dealer = 'placeholder'
myblackjack = BlackJack(deck, player, dealer, 1000)

myblackjack.main()
myblackjack.runGameLoop()
myblackjack.endGame()