from Board import Board,delay

from CharBase import CharBase
###
import ipdb

class Player(CharBase):

    def __init__(self, money):
        super().__init__(money)
        self.name = 'Player' 
        self.total_bet_in_Player = 0
        self.betted_in_Player = False
        self.decided = False

    def bet(self, bet_amount_in_Player = 0):
        """
        betting a set amount of money.
        
        """
        while not self.betted_in_Player:

            if bet_amount_in_Player == 0 or self.decided == False:
                bet_amount_in_Player = input(f"How much will you bet? (Min: $1, Max: ${self.money_in_CharBase}) \n"
                                    "$")

            try:
                bet_amount_in_Player = int(bet_amount_in_Player)
            except ValueError:
                print("Bet again.")
                bet_amount_in_Player = 0
                continue

            if bet_amount_in_Player > self.money_in_CharBase:
                print("You can't bet more than your balance.")
                if self.decision == 2:  #This is when bet() is called from CharBase.ask_decision()
                    delay(1.4)
                    print("Betting all instead.")
                    bet_amount_in_Player = self.money_in_CharBase
                else:
                    bet_amount_in_Player = 0
                    continue

            elif bet_amount_in_Player < 1:
                print("Can't bet less than $1.")
                continue

            else:   #bet_amount_in_Player <= self.money_in_CharBase
                print(f"Betting ${bet_amount_in_Player}.")
                self.money_in_CharBase -= bet_amount_in_Player
                self.total_bet_in_Player += bet_amount_in_Player
                self.betted_in_Player = True
                
            delay(1.4)
    
    def make_decision(self):
        """
        decide a value for self.decision. Use in main script.
        """
        while not self.decided:
            try:
                self.decision = int(input("1. Draw \n"
                                         "2. Draw final card and double bet \n"
                                         "3. End turn \n"))
            except ValueError:
                print("Wrong input")
                continue

            self.decided = True

        delay(1.4)