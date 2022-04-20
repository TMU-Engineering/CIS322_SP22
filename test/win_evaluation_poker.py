import CardGames
from Find_Flush import *
from FourOfAKind import *
from Find_FullHouse import *
from PokerPlayer4Functions import *
from Straight_Hand import *

class win_evaluation_poker:

    def __init__(self, playerlist, river, betting):
        player=Player("test", 10)
        player.hand_value=(10, 0)
        self.winner=player
        self.winnerList=[]
        self.players=playerlist
        self.river=river
        self.betting=betting

    def find_hand_values(self, playerlist, river):
        #for every player, check to see if they have
        for i in playerlist:
            
            high=highCard(i, river)
            pair=getPairs(i, river)
            two=get2Pairs(i, river)
            three=threeOfAKind(i, river)
            flush=find_flush(i, river)
            four=findFour(i, river)
            full_house=findFullHouse(i, river)
            Straight=straight(i, river)
            Straight_flush=straight_flush(i, river)
            # set the player hand_value to the highest type of hand
            if high[0] == True:
                i.hand_value=(9, high[1])
            elif pair[0] == True:
                i.hand_value=(8, pair[1])
            elif two[0] == True:
                i.hand_value=(7, two[1])
            elif three[0] == True:
                i.hand_vaule=(6, three[1])
            if Straight[0] == True:
                i.hand_value=(5, Straight[1])
            elif flush[0] == True:
                i.hand_value=(4, flush[1])
            elif full_house[0]:
                i.hand_value=(3, full_house[1])
            elif four[0] == True:
                i.hand_value=(2, four[1])
            elif Straight_flush[0] == True:
                i.hand_value=(1, Straight_flush[1])
    
        
    def find_winner(self, playerlist):
        #check every person hand_value to each other   
        for i in playerlist:
            if i.hand_value[0] < self.winner.hand_value[0]:
                self.winner=i
            elif i.hand_value[0] == self.winner.hand_value[0]:
                if i.hand_value[1] > self.winner.hand_value[1]:
                    self.winner.pop()
                    self.winner.append(i)
                else:
                    self.winner.append(i)
                    
    def end_game_actions(self):
        #give the money to the winner(s)
        if len(self.winnerList) == 0:
            money=self.betting.pot
            self.winner.money += money
            self.betting.pot = 0
        else:
            number = len(self.winnerList)
            money=self.betting.pot
            split_money=money/number
            for i in self.winnerList:
                i.money += split_money
            self.betting.pot = 0
            
            

    
                
            
