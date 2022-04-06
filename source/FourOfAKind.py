#import River_Class
import CardGames


def findFour(player, river):
    tempHand = player.hand + river.hand
    handValues = []
    for i in tempHand:
        cardCount = 0
        handValues.append(i.value)
        for x in tempHand:
            if x != i:
                if x.value == i.value:
                    cardCount += 1
        if cardCount == 3:
            return (True, x.value-1)
        #print(f"FourResults: \n CardNum:{i.value}, Count:{cardCount}")
    #print(f"Hand:{handValues}")
    return (False, 0)



