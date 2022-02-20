from CardGames import *
def face_values(deck):
  for x in range(52):
    value=deck.cards[x].value
    if value in [2,3,4,5,6,7,8,9,10]: #If the card is 2, 3, 4, 5, 6, 7, 8, 9, 10, then the card value is it's current value.
      deck.cards[x].value=value
    elif value in [11,12,13]: #If the card is a King, Queen, or Jack, then the card value is switched from its current value to 10.
      deck.cards[x].value=10

def ace_value(Sum, card):
  if Sum < 11:
    card.value=11
  else:
    card.value=1
  return card.value
