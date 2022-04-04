from CardGames import *

class betting:
    def __init__(self, playerList):
        self.pot=0
        self.bet=0

    def square(self, playerList):
        square=True
        for i in playerList:
            if i.bet == self.bet:
                square=True
            else:
                square=False
        return square
    
    def make_bet(self, amount: int):
        if amount == self.bet:
            self.bet=amount
        elif amount > (self.bet*2):
            self.bet=amount
        else:
            print("A raise must be twice the size of the original bet")
            
        
    
