from Blackjack_CharBase import CharBase

from time import sleep

class Player(CharBase):
    def __init__(self, money):
        super().__init__(money)
        self.name = 'Player' 
        self.total_bet_in_Player = 0
        self.betted_in_Player = False
        self.decided = False

    def bet(self, bet_amount_in_Player = 0):
        #CharBase.play() calls this method.

        while not self.betted_in_Player:

            if bet_amount_in_Player not in locals():
                bet_amount_in_Player = input(f"How much will you bet? (Min: $1, Max: ${self.money_in_CharBase}) \n"
                               "$")

            try:
                bet_amount_in_Player = int(bet_amount_in_Player)
            except ValueError:
                print("Bet again.")
                del bet_amount_in_Player
                continue

            if bet_amount_in_Player > self.money_in_CharBase:
                print("You can't bet more than your balance.")
                if self.decision == 2:  #This is when bet() is called from CharBase.play()
                    sleep(1.4)
                    print("Betting all instead.")
                    bet_amount_in_Player = self.money_in_CharBase
                else:
                    del bet_amount_in_Player
                    continue

            elif bet_amount_in_Player < 1:
                print("Can't bet less than $1.")
                del bet_amount_in_Player
                continue

            if bet_amount_in_Player <= self.money_in_CharBase:
                print(f"Betting ${bet_amount_in_Player}.")
                self.money_in_CharBase -= bet_amount_in_Player
                self.total_bet_in_Player += bet_amount_in_Player
                self.betted_in_Player = True
                
            sleep(1.4)
    
    def play(self):

        while not self.decided:
            try:
                self.decision = int(input("1. Draw \n"
                                         "2. Draw final card and double bet \n"
                                         "3. End turn \n"))
            except ValueError:
                print("Wrong input")
                continue

            self.decided = True

        sleep(1.4)