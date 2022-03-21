from CardGames import *
from River_Class import *

def find_flush(player, river):
    ### Need to have separate variables to keep track of how many cards are of each suit"
    num_spades = 0
    num_clubs = 0
    num_hearts = 0
    num_diamonds = 0
    ### Need to have separate variables to keep track of the highest suit card
    high_spade = Card("test", 0, [], [])
    high_club = Card("test", 0, [], [])
    high_heart = Card("test", 0, [], [])
    high_diamond = Card("test", 0, [], [])
    ### Add both Player's hand and the river
    Cards= player.hand + river.hand
    ### For every card, check to find the suit, then add 1 to the count
    ### for that specific suit and see if that's the highest card in the suit
    for i in Cards:
        if i.suit == "Spades":
            num_spades = num_spades + 1
            if i.value > high_spade.value:
                high_spade= i
        elif i.suit == "Clubs":
            num_clubs = num_clubs + 1
            if i.value > high_club.value:
                high_club= i
        elif i.suit == "Hearts":
            num_hearts = num_hearts + 1
            if i.value > high_heart.value:
                high_heart= i
        else:
            num_diamonds = num_diamonds + 1
            if i.value > high_diamond.value:
                high_diamond= i
    ### See if there is a set of 5 cards with the same suit.
    ### This function returns a tuple with the first being if there is a flush
    ### The second being the highest card in that suit
    ### The thrid being the name of the suit
    if num_spades >=5:
        return (True, high_spade.value, high_spade.suit)
    elif num_clubs >=5:
        return (True, high_club.value, high_club.suit)
    elif num_hearts >=5:
        return (True, high_heart.value, high_heart.suit)
    elif num_diamonds >=5:
        return (True, high_diamond.value, high_diamond.suit)
    else:
        return (False, 0)
    

deck=Deck()
Jacob=Player("Jaocb", 200)
Dealer=Dealer()
River = River(deck)
Jacob.addCard(deck.getCard())
Jacob.addCard(deck.getCard())
Dealer.printCards(Jacob.hand, True)
River.roundOne(deck)
River.roundTwo(deck)
River.roundThree(deck)
River.printHand(River.hand, True)
flush=find_flush(Jacob, River)
print(flush)
