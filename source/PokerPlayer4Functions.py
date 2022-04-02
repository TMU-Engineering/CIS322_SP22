from source.CardGames import *

class PokerPlayer:

    def __init__(self, name, value, money: int = 0):
        self.hand = []
        self.knownCards = []
        self.value = []

    def printPlayerCards(self, printShort: bool = False):
        for idx in range(6):
            for i, card in enumerate(self.hand):
                if printShort and i < len(self.hand)-1:
                    image = card.shortImage[idx]  if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
            print()

    def addCard(self, card: Card, isKnown: bool = True):
        self.hand.append(card)
        if isKnown:
            self.knownCards.append(True)
        else:
            self.knownCards.append(False)

    def highCard(self, value):
        cardList = []
        for x in self.hand:
            cardList.append(x.value)
        Sort = sorted(cardList)
        print("High card is:", Sort[len(Sort) - 1])

    def getPairs(self, value):
        cardList = []
        duplicate = []
        x = 0
        for y in self.hand:
            cardList.append(y.value)
            x += 1
        Sort = sorted(cardList)

        a, b = 0, 1
        for z in range(x - 1):
            if Sort[a] == Sort[b]:
                duplicate.append(Sort[a])
            a, b = a + 1, b + 1

        if len(duplicate) != 0:
            print("Highest pair is:", duplicate[len(duplicate) - 1])

    def get2Pairs(self, value):
        cardList = []
        duplicateList = []
        pairList = []
        v = 0
        for w in self.hand:
            cardList.append(w.value)
            v += 1
        Sort = sorted(cardList)

        x = 0
        a, b = 0, 1
        for y in range(v - 1):
            if Sort[a] == Sort[b]:
                duplicateList.append(Sort[a])
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
            print("Highest 2 pairs is:", pairList[len(pairList) - 1],
                  "and", pairList[len(pairList) - 2])

    def threeOfAKind(self, value):
        cardList = []
        duplicateList = []
        pairList = []
        v = 0
        for w in self.hand:
            cardList.append(w.value)
            v += 1
        Sort = sorted(cardList)

        x = 0
        a, b = 0, 1
        for y in range(v - 1):
            if Sort[a] == Sort[b]:
                duplicateList.append(Sort[a])
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
            print("Highest 3 of a kind is:", threeOfAKind[length])
