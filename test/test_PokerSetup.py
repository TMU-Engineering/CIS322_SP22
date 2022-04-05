from testing_base import *
from source.PokerPlayer4Functions import *
from source.PokerSetup import *

def test_Functions():

    player1 = Player('John')
    player2 = Player('Jacob')
    player3 = Player('Jonathan')
    player4 = Player('Andrew')
    player5 = Player('Joe')

    PlayerList = [player1, player2, player3, player4, player5]

    deck = Deck()
    dealer = Dealer()

    #PokerGameSetup.preGame(deck, PlayerList)
    PokerGameSetup.Blinds(deck)
    #PokerGameRounds.startRound(deck)
    PokerGameRounds.initialRiver(deck)
    PokerGameRounds.blindBets(deck)
    #PokerGameRounds.normalBets(deck)
    PokerGameRounds.Check(deck)
    PokerGameRounds.Call(deck)
    PokerGameRounds.Raises(deck)
    PokerGameRounds.allIn(deck)
    PokerGameRounds.Fold(deck)
    PokerGameRounds.addCardToRiver(deck)
    #PokerGameRounds.playFirstRound(deck)
    #PokerGameRounds.playRound(deck)
    #PokerGameRoundsWinEvaluation.evaluatePlayerHand(deck)
    #PokerGameRoundsWinEvaluation.winTie(deck)
    #PokerGameRoundsWinEvaluation.winRoundEvaluation(deck)
    #PokerGameRoundsWinEvaluation.playGameRound(deck)
    #PokerGameRoundsWinEvaluation.playEntiregame(deck)

test_Functions()

def test_4_Functions():
    deck=Deck()
    deck.shuffle()
    player=Player("player", 200)
    player2=PokerPlayer("player2", 200)
    dealer=Dealer()
    dealer.dealCards(7, [player, player2], deck)
    dealer.printPlayerCards(player2)
    player2.highCard(deck)
    player2.getPairs(deck)
    player2.get2Pairs(deck)
    player2.threeOfAKind(deck)

test_4_Functions()
