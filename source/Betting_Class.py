class betting:
    def __init__(self, playerList):
        self.pot=0
        self.bet=0
        self.list=playerList

    def square(self):
        square=True
        for i in self.list:
            if i.bet == self.bet:
                square=True
            else:
                square=False
        return square
    
    def make_bet(self, amount: int):
        valid=False
        if amount == self.bet:
            self.bet=amount
            valid=True 
        elif amount >= (self.bet*2):
            self.bet=amount
            valid=True
        else:
            print("A raise must be twice the size of the original bet")
        return valid
        
    
