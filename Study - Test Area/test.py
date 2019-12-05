import ipdb

class CharBase:
    def __init__(self, money):
        self.money = money

class Player(CharBase):
    def __init__(self, money):
        super().__init__(money)
        self.name = 'Player' 
        self.total_bet = 0
        self.decision = 0

    def bet(self, bet_amount = 0):

        if bet_amount == 0:
            bet_amount = input(f"How much will you bet? (Min: $1, Max: ${self.money}) \n"
                           "$")
        
        try:
            bet_amount = int(bet_amount)
        except ValueError:
            print("Bet again.")
            self.bet()

        print(type(bet_amount)) #Unrelated to program, just to debug

player = Player(100)
player.bet()