from testing_base import *
from source.PokerPlayer4Functions import *
from source.PokerSetup import *

def test_preGame():

    player1 = Player('John')
    player2 = Player('Jacob')
    player3 = Player('Jonathan')
    player4 = Player('Andrew')
    player5 = Player('Joe')

    PlayerList = [player1, player2, player3, player4, player5]

    deck = Deck()

    PokerGameSetup.preGame(deck, PlayerList)

    print('')
    for player in PlayerList:
        print(player.name, '= $', player.money)

test_preGame()

def test_startRound():

    player1 = Player('John')
    player2 = Player('Jacob')
    player3 = Player('Jonathan')
    player4 = Player('Andrew')
    player5 = Player('Joe')

    PlayerList = [player1, player2, player3, player4, player5]

    deck = Deck()
    dealer = Dealer()
    PokerGameRounds.startRound(deck, PlayerList)

test_startRound()
