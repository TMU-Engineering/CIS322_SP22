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

