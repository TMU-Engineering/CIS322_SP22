import CardGames



def findFullHouse(player, river):
    tempHand = []
    tempHand = player.hand + river.hand
    handValues = []
    twoHandValues = []
    hasThree = False
    threeValue = 0
    for x in tempHand:
        counter = 1
        for y in tempHand:
            if y != x and y.value == x.value:
                counter+=1
        if counter == 3 or counter == 4:
            hasThree = True
            for card in tempHand:
                if card.value == x.value:
                    tempHand.remove(card)
            threeValue = x.value
            
            break
        


    for value in tempHand:
        handValues.append(value.value)


    hasTwo = False
    twoValue = 0
    for a in tempHand:
        twoCounter = 1
        for b in tempHand:
            if b != a and b.value == a.value:
                twoCounter+=1
        if twoCounter == 2 or twoCounter == 3:
            hasTwo = True
            for card in tempHand:
                if card.value == a.value:
                    tempHand.remove(card)
            twoValue = a.value

            break
        

    if hasThree == True and hasTwo == True:
        return True
    
    for value in tempHand:
        twoHandValues.append(value.value)

#    print(f"hasThree: {hasThree}")
#    print(f"threeValue: {threeValue}")
#    print(f"tempHand: {handValues}")
#    print(f"hasTwo: {hasTwo}")
#    print(f"twoValue: {twoValue}")
#    print(f"2ndtempHand: {twoHandValues}")
    return False#hasThree, threeValue, hasTwo, twoValue)

        