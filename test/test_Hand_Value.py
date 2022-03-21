from CardGames import *

def Hand_Value(player):
  hand=player.hand
  hand_value=0
  for card in hand:
    value=card.value
    if value in [2,3,4,5,6,7,8,9,10]: #If the card is 2, 3, 4, 5, 6, 7, 8, 9, 10, then the card value is it's current value.
      hand_value=hand_value + value
    elif value in [11,12,13]: #If the card is a King, Queen, or Jack, then the card value is switched from its current value to 10.
      hand_value=hand_value + 10
    else:
      if hand_value < 11:
        hand_value=hand_value+11
      else:
        hand_value=hand_value+1
  return hand_value

def testing():
    deck=Deck()
    dealer=Dealer()
    player1=Player("Player1", 200)
    player2=Player("Player2", 200)
    player3=Player("Player3", 200)
    player4=Player("Player4", 200)
    PlayerList.append(player1)
    PlayerList.append(player2)
    PlayerList.append(player3)
    PlayerList.append(player4)
    dealer.dealCards(4, PlayerList, deck)
    dealer.printPlayerCards(player1)
    player1_Hand_Value=Hand_Value(player1)
    dealer.printPlayerCards(player2)
    player2_Hand_Value=Hand_Value(player2)
    dealer.printPlayerCards(player3)
    player3_Hand_Value=Hand_Value(player3)
    dealer.printPlayerCards(player4)
    player4_Hand_Value=Hand_Value(player4)
    return [player1_Hand_Value,player2_Hand_Value,player3_Hand_Value,player4_Hand_Value]

x=testing())

def test_Hand_Value():
    assert 34=x[0] and 18=x[1] and 33=x[2] and 37=x[3] 

