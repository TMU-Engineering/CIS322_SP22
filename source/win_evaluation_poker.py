import CardGames

class win_evaluation_poker:

    def __init__(self, playerlist, river, betting):
        self.winner=[]
        self.players=playerlist
        self.river=river
        self.betting=betting

    def find_hand_values(self, playerlist, river):
        #for every player, check to see if they have
        for i in playerlist:
            
            high=highCard(i, river)
            pair=getpair(i, river)
            two=get2pair(i, river)
            three=threeofAKind(i, river)
            flush=find_flush(i, river)
            four=findFour(i, river)
            full_house=findFullHouse(i, river)
            straight=straight(i, river)
            straight_flush=straight_flush(i, river)

            # set the player hand_value to the highest type of hand
            if high[0] == True:
                i.hand_value=(9, high[1])
            elif pair[0] == True:
                i.hand_value=(8, pair[1])
            elif two[0] == True:
                i.hand_value=(7, two[1])
            elif three[0] == True:
                i.hand_vaule=(6, three[1])
            elif straight[0] == True:
                i.hand_value=(5, straight[1])
            else if flush[0] == True:
                i.hand_value=(4, flush[1])
            elif full_house[0] == True:
                i.hand_value=(3, full_house[1]
            elif four[0] == True:
                i.hand_value=(2, four[1])
            elif straight_flush[0] == True:
                i.hand_value=(1, straight_flush[1])
    
        
    def find_winner(self, playerlist):
        #check every person hand_value to each other
        self.winner.append(playerlist[0])   
        for i in playerlist[1:]:
            if i.hand_value[0] < self.winner[0].hand_value[0]:
                self.winner.pop()
                self.winner.append(i)
            elif i.hand_value[0] == self.winner.hand_value[0]:
                if i.hand_value[1] > self.winner[0].hand_value[1]:
                    self.winner.pop()
                    self.winner.append(i)
                else:
                    self.winner.append(i)

    def end_game_actions(self):
        #give the money to the winner(s)
        if len(self.winner) == 0:
            money=self.betting.pot
            self.winner[0].money += money
            self.betting.pot = 0
        else:
            number = len(self.winner)
            money=self.betting.pot
            split_money=money/number
            for i in self.winner:
                i.money += split_money
            self.betting.pot = 0
            
            

    
                
            
