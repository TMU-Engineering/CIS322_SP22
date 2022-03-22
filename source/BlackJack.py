# This file is the game controller for BlackJack.
# It is where we will link all the components together
# and manage the game state.
import CardGames
import BlackJackDealer
import New_Values
import Player_input
import print_cards
import win_evaluation

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
        self.gameDealer.dealCards(2, self.gamePlayer, self.gameDeck)
        self.gameDealer.dealDealerCards(self.gameDeck)

    # This will run the game loop
    def runGameLoop(self):
        Player_input.Player_input(self.gamePlayer, self.gameDeck, self.gameDealer)
        self.gameDealer.Dealers_Moves(self.gameDeck)

    # This function will handle the game win/loose and display to the user who won
    def endGame(self):
        win_evaluation.evaluation(self.gamePlayer, self.gameDealer)

# This is where the instance of the blackjack game will be made
deck = CardGames.Deck()
player = CardGames.Player('Player1', 500)
dealer = BlackJackDealer.BlackJackDealer('Dealer', 1000)
myblackjack = BlackJack(deck, player, dealer, 0)

myblackjack.main()
myblackjack.runGameLoop()
myblackjack.endGame()