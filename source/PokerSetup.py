#   Code still needs to incorporate a pot.

from source.CardGames import *
import sys

PlayersStillInGameList = PlayerList
BlindsList = PlayersStillInGameList
PlayersPlayingRoundList = PlayersStillInGameList
PlayersOutOfGameList = []

class PokerGameSetup:

    def __init__(self, name, money: int = 0):
        self.name = []
        self.hand = []
        self.money = money

    def preGame(self, players: PlayerList):
        #   Give each player their money.
        #
        #   Option to have each player start with the same amount of money,
        #   or with various amounts of money.
        try:
            Same = input('''Enter "Same" if each player starts with the same amount.
Enter "Different" if each player start with different amounts: ''')

            #   Each player starts with the same amount.
            if Same == "Same" or Same == "same" or Same == "SAME" or Same == "S" or Same == "s":
                Amount = int(input('No cents! Enter amount: $'))
                for player in PlayerList:
                    Player.addMoney(self, amount)

            #   Each player starts with different amounts.
            elif Same == "Different" or Same == "different" or Same == "DIFFERENT" or Same == "D" or Same == "d":
                for player in PlayerList:
                    Amount = int(input('No cents! Enter amount: $'))
                    Player.addMoney(self, amount)

            #   If a word other than "Same" or "Different" is entered.
            else:
                print('''YOU WERE SUPPOSE TO ENTER "Same" OR "Different"!!!
YOU WANT TO BE DIFFICULT?!?!
GO HOME!!!''')
                sys.exit()

            #   "Big Blind" amount.
            Big_Blind = int(input('''Enter Big Blind amount.
Must be an even number greater than 0: $'''))

            #   If "Big Blind" amount is not even, or
            #   is $0 then the question gets repeated.
            while Big_Blind%2 != "1" or Big_Blind == "0":
                Big_Blind = int(input('''Enter Big Blind amount.
Must be an EVEN number greater than 0: $'''))

        #   If an invalid value is entered (i.e. not a number).
        except ValueError:
            print(error)
            sys.exit()

        return Big_Blind

    def Blinds(self):
        #   Determines who is Big_Blind and who is Small_Blind.
        #   Made a BlindsList to keep track.
        #   BlindList will need to delete all players no longer playing.
        #   Made a PlayersOutOfGameList, just keep the BlindList updated every time by deleting from PlayersOutOfGameList.
        pass

class PokerGameRounds:

    def __init__(self, name, money: int = 0):
        self.name = name
        self.money = money
        river = []

    def startRound(self):

        #   Shuffle deck!
        Deck.shuffle(self)

        #   Cuts
        print('Cutting')
        Deck.shuffle(self)

        #   Deal cards!
        Dealer.dealCards(2, PlayerList, deck)

    def initialRiver(self):
        #   Deals and Displays Initial River!
        #   Made a river list.
        pass

    def blindBets(self):
        #   First round of betting incorporating Big_Blind and Small Blind.
        #   Made a BlindsList to keep track.
        pass

    def normalBets(self):
        #   Display player and their hand! Does not factor in Big_Blind and Small_Blind.

        #   Initial Amount is 0
        Amount = 0

        #   Loops through players
        for player in PlayersPlayingRoundList:
            print(player.name)
            print(player.money)
            Dealer.printPlayerCards(self)

            # Player's move!
            Move = input('''Enter "Check" to Pass.
Enter "Call" to Match.
Enter "Raise" to Raise.
Enter "All In" to Raise all in.
Enter "Fold" to Fold.''')

            #   Player Checks!
            if Move == "Check" or Move == "CHECK" or Move == "check":
                #   Call Check Function.
                PokerPlayer.Check()

            #   Player Calls!
            elif Move == "Call" or Move == "CALL" or Move == "call":
                #   Call Call Function.
                PokerPlayer.Call()

            #   Player Raises!
            elif Move == "Raise" or Move == "RAISE" or Move == "raise":
                #   Call Raise Function.
                PokerPlayer.Raise()

            #   Player is All In!
            if Move == "All In" or Move == "ALLIN" or Move == "ALL IN" or Move == "All in" or Move == "all In" or Move == "all in" or Move == "allin":
                #   Call Check Function.
                PokerPlayer.Check()

            #   Player Folds!
            elif Move == "Fold" or Move == "fold":
                #   Call Fold Function.
                PokerPlayer.Fold()

            #   If an invalid move was entered.
            else:
                print('''You did not corretly enter a valid move.
Automatic Fold!''')
                PokerPlayer.Fold()

    def Check(self):
        #   Checks and passes.
        pass

    def Call(self):
        #   Call and matches bidding amount.
        pass

    def Raises(self):
        #   Raises and increases bidding amount.
        #
        #   I think we are doing it where the raise has to be at least double the preious raise.
        #
        #   If raised, then another loop must be factored in for betting that round until it arrives at the last person to raise it.
        #
        #   How I have played Texas Hold Em is that the person who raised it in a round, cannot raise it again in the same round
        #   This will work because then we don't have to factor in the potential scenarior where it loops around more times than there are players playing.
        #   So loop through the bets, if someone Raises, begin a new loop until it ends at the person who is before the person who raised it.
        pass

    def allIn(self):
        #   Raises bidding amount with all the money the player has left.
        #
        #   Technically, when someone goes all in, those who are wealtheier can still outbid him.
        #   So the player who goes all in will have to leave PlayersPlayingRoundList.
        #   But if he wins, they get placed back in.
        #   They only win all the player's money that matches them.
        #   If there is more money in the pot, then all the extra money goes back to original owners.
        #   If they lose, they drop out of the game entirely.
        pass

    def Fold(self):
        #   Fold and leaves PlayersPlayingRoundList.
        pass

    def addCardToRiver(self):
        #   Adds a card to the River and Displays River!
        #   Made a river list.
        pass

    def playFirstRound(self):
        #   First Round of a Game.
        PokerGameSetup.Blinds(self)
        PokerGameRounds.startRound(self)
        PokerGameRounds.initialRiver(self)
        PokerGameRounds.blindBets(self)

    def playRound(self):
        #   A normal Round of a game.
        PokerGameRounds.addCardToRiver(self)
        PokerGameRounds.normalBets(self)

class PokerGameRoundsWinEvaluation:

    def __init__(self, name, value, money: int = 0):
        self.name = name
        self.hand = []
        self.knownCards = []
        self.value = []
        self.win = []
        self.money = money

    def highCard(self, value):
        #   Player's Best hand is a high card.
        cardList = []
        for x in self.hand:
            cardList.append(x.value)
        Sort = sorted(cardList) 
        print("High card is:", Sort[len(Sort) - 1])

    def getPairs(self, value):
        #   Player's Best hand is a pair.
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
        #   Player's Best hand is 2 pairs.
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
        #   Player's Best hand is a 3 of a kind.
        cardList = []
        duplicateList = []
        pairList = []
        self.winNumber = []
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

    def evaluatePlayerHand(self):
        for players in PlayersPlayingRoundList:
            PokerGameRoundsWinEvaluation.threeOfAKind(self, value)
            if yes == True:
                players = win.append(4)
                break
            PokerGameRoundsWinEvaluation.get2Pairs(self, value)
            if yes == True:
                players = win.append(3)
                break
            PokerGameRoundsWinEvaluation.getPairs(self, value)
            if yes == True:
                players = win.append(2)
                break
            PokerGameRoundsWinEvaluation.highCard(self, value)
            if yes == True:
                players = win.append(1)

    def winTie(self):
        #   Evaluates a winner if the winRoundEvaluation is a tie.
        #   If it is truly a tie, the highest players who tie split the pot.
        #   If there was a player who went all in and ties, they get half the amount the would have, other winner gets the rest.
        pass

    def winRoundEvaluation(self):
        #   Incorporates the 10 Functions made.
        #   Evaluates winner of the game round.
        pass

    def playGameRound(self):
        #   One Game
        PokerGameRounds.playFirstRound(self)

        for i in range(2):
            PokerGameRounds.playRound(self)

        evaluatePlayerHand(self)
        winRoundEvaluation(self)

    def playEntireGame(self):
        while len(PlayersStillInGameList) > 1:
            playGameRound(self)
