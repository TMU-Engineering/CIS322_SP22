import CardGames



def findFullHouse(player, river):
    tempHand = player.hand + river.hand
    handValues = []

    #/////////ThreeOfAKind////////
    three = (False, 0)
    for i in tempHand:
        #print(f"i-Value: {i.value}")
        cardCount = 0
        handValues.append(i.value)
        for x in tempHand:
            if x != i:
                if x.value == i.value:
                    cardCount += 1
        print(f"cardCount(forThree): {cardCount}, for card: {i.value}")
        if cardCount == 2 or cardCount == 3:
            three = (True, x.value-1)


    #/////////TwoOfAKind//////////
    two = (False, 0)
    for y in tempHand:
        #print(f"y-Value: {y.value}")
        twoCardCount = 0
        if y.value-1 != three[1]:
            
            for x in tempHand:
                if x != y:
                 if x.value == y.value:
                    twoCardCount += 1
        print(f"cardCount(forThree): {cardCount}, for card: {y.value}")
        if twoCardCount == 1 or twoCardCount == 2:
            two = (True, x.value-1)
    
    if two == True and three == True:
        return(True, three[1], two[1])
    


    print(f"Hand:{handValues}")
    return (False, 0, 0)