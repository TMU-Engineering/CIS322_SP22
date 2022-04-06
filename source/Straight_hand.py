from CardGames import *
from Find_Flush import *


def straight(player, river):
    
    options = []
    
    # In these loops I am adding the values of cards all into one list
    # I was struggling to do it any other way and this seems to work fine
    
    for cards in player.hand:
        options.append(cards.value)
    for stuff in river.hand:
        options.append(stuff.value)

    #Here I am going through all of the values starting at 14
    #If the rank is in the list it counts 1 and continues
    #If it hits a value that is not there and we have not hit 5, it resets the count
    #If iterated through completely with no breaks, it returns false

    count = 0
    for rank in reversed(range(2, 15)):
        if rank in options:
            count += 1
            if count == 5:
                return True, rank+4
                break
        else:
            count = 0
    else:
        return False
   
def straight_flush(player, river):
    if find_flush(player, river) != False and straight(player, river) != False:
        return straight(player, river)
    else:
        return False

