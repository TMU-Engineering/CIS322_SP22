from CardGames import *
from win_evaluation_poker import *
from Betting_Class import *
from River_Class import *


def testing():
    deck="test"
    #function=functions()
    jacob=Player("Jacob", 200)
    dana=Player("Dana", 200)
    john=Player("John", 200)
    kati=Player("Kati", 200)
    ace = Card("Spade", 14, [],[])
    king = Card("Spade", 13, [],[])
    queen = Card("Clubs", 12, [],[])
    jack = Card("Clubs", 11, [],[])
    ten = Card("Spade", 10, [],[])
    six_2 = Card("Hearts",6 , [],[])
    eight = Card("Spade", 8, [],[])
    six_3 = Card("Clubs", 6, [],[])
    six = Card("Clubs", 6, [],[])
    five_spade = Card("Spade", 5, [],[])
    five_clubs = Card("Clubs", 5, [],[])
    three = Card("Spade", 3, [],[])
    two = Card("Spade", 2, [],[])
    river=River(deck)
    river.river=[ace, queen, ten, eight, six]
    jacob.hand=[king, jack] # straight
    dana.hand=[two, three] #flush
    #kati.hand=[five_spade, five_clubs] #pair
    #john.hand=[six_2, six_3] #three
    playerList=[jacob,dana]
    Betting=betting(playerList)
    for i in playerList:
        i.makeBet(20, Betting)
    judge=win_evaluation_poker(playerList, river, Betting)
    judge.find_hand_values(playerList, river)
    judge.find_winner(playerList)
    judge.end_game_actions()
    return judge.winner.name, judge.winner.money
    

x=testing()

def test_win_evaluation_poker():
    assert x[0] == "Dana" and x[1] == 220
