from CardGames import *

def highCard(player, river):
    cardList = player.hand + river.river
    card_value=[]
    for x in cardList:
        card_value.append(x.value)
    card_value.sort()
    High = card_value.pop()
    #print("High card is:", High)
    return True, High

def getPairs(player, river):
    cardList = player.hand + river.river
    duplicate = []
    x = 7
    card_value=[]
    for x in cardList:
        card_value.append(x.value)
    card_value.sort()

    a, b = 0, 1
    for z in range(6):
        if card_value[a] == card_value[b]:
            duplicate.append(card_value[a])
        a, b = a + 1, b + 1

    if len(duplicate) != 0:
        Pair = duplicate[len(duplicate) - 1]
        #print("Highest pair is:", Pair)
        return True, Pair

def get2Pairs(player, river):
    cardList = player.hand + river.river
    duplicateList = []
    pairList = []
    v = 7
    card_value=[]
    for w in cardList:
        card_value.append(w.value)
    card_value.sort()

    x = 0
    a, b = 0, 1
    for y in range(6):
        if card_value[a] == card_value[b]:
            duplicateList.append(card_value[a])
            x += 1
        a, b = a + 1, b + 1
    Duplicate = sorted(duplicateList)

    if x >= 2:
        c, d = 0, 1
        for z in range(x - 1):
            if Duplicate[c] != Duplicate[d]:
                pairList.append(Duplicate[c])
            c, d = c + 1, d + 1
        pairList.append(Duplicate[c])
        
    if len(pairList) == 2:
        Pair1 = pairList[len(pairList) - 1]
        Pair2 = pairList[len(pairList) - 2]
        #print("Highest 2 pairs is:", Pair1, Pair2)
        return True, Pair1, Pair2

def threeOfAKind(player, river):
    cardList = player.hand + river.river
    duplicateList = []
    pairList = []
    v = 0
    card_value=[]
    for w in cardList:
        card_value.append(w.value)
        v += 1
    card_value.sort()

    x = 0
    a, b = 0, 1
    for y in range(v - 1):
        if card_value[a] == card_value[b]:
            duplicateList.append(card_value[a])
            x += 1
        a, b = a + 1, b + 1
    Duplicate = sorted(duplicateList)

    if x >= 2:
        c, d = 0, 1
        for z in range(x - 1):
            if Duplicate[c] == Duplicate[d]:
                pairList.append(Duplicate[c])
            c, d = c + 1, d + 1
    threeOfAKind = sorted(pairList)

    length = len(threeOfAKind) - 1
    if length >= 0:
        threekind = threeOfAKind[0]
        #print("Highest 3 of a kind is:", 3kind)
        return True, threekind
    else:
        return False, 0
