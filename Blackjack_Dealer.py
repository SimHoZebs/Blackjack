from Blackjack_CharBase import CharBase
from Blackjack_Board import Board,delay

from random import choice

class Dealer(CharBase):
    def __init__(self, money):
        super().__init__(money)
        self.name = 'Dealer'
        self.revealed = False

    def hide_card(self):
        self.hidden_card = choice(self.hand)
        self.hand.remove(self.hidden_card)
        self.hand.append("HIDDEN CARD")

        if Board.CARD_VALUE[self.hand[0]] == 'SPECIAL':
            score1_hidden = 11
            score2_hidden = 1

        else:
            score1_hidden = score2_hidden = Board.CARD_VALUE[self.hand[0]]

        self.score1_in_CharBase = f"{score1_hidden} + x"
        self.score2_in_CharBase = f"{score2_hidden} + x"

    def reveal_card(self):   #Swaps the hidden card with the actual card, revealing it.
        print("Revealing HIDDEN CARD...")
        delay(1.4)

        self.hand.append(self.hidden_card)
        self.hand.remove("HIDDEN CARD")

        print(f"The HIDDEN CARD was a {self.hidden_card}!")
        delay(1.4)

    def play(self):
        if self.revealed == False:
            self.revealed = True
            self.reveal()

        if self.score1_in_CharBase >= 17:
            self.decision = 3
        else:
            self.decision = 1