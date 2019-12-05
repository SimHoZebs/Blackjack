# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:46:09 2019

@author: Zebs
"""

from random import choice
from time import sleep

###################################

class CharBase:
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.decision = 0
        self.hand_size = len(self.hand)
        self.score1 = 0     #SCORE VALUE FOR WHEN ACE == 11
        self.score2 = 0     #SCORE VALUE FOR WHEN ACE == 1

    def draw(self, amount=1):
        cycle = 0

        while cycle != amount:
            drawn_card = choice(board.deck)
            board.deck.remove(drawn_card)
            self.hand.append(drawn_card)

            if self.name == "Dealer" and len(self.hand) <= 2:
                print("Dealer draws a card.")

            else:
                print(f"{self.name} draws {drawn_card}.")

            cycle += 1
            sleep(1.4)

        self.calc_score()

    #Score resets before each calc. Need to change it.
    def calc_score(self):
        self.score1 = 0
        self.score2 = 0
        has_ace = 0

        for cards in self.hand:
            try:
                self.score1 += card_value[cards]
                self.score2 = self.score1

            except TypeError:
                """ This occurs when the card in hand is an ACE."""
                self.score2 += 1
                has_ace += 1

        if has_ace == 1:
            if self.score1 >= 11:
                self.score1 += 1
            elif self.score1 < 11:
                self.score1 += 11

        elif has_ace > 1:
            self.score1 += has_ace

    def eval_loss(self):

        if self.score1 > 21:   #WHEN NAME IS PLAYER
           print(f"{self.name}'s score is over 21. {self.name} loses!")
           board.loser = self.name
           sleep(1.4)

        elif self.name == "Dealer":
            if self.score1 >= 17:
                if self.score1 > player.score1:
                    print("Dealer has a higher score. Dealer wins!")
                    board.loser = 'Player'
                elif self.score1 < player.score1:
                    print("Dealer has a lower score. Player wins!")
                    board.loser = self.name
                elif self.score1 == player.score1:
                    print("A draw! Player gets their money back.")
                    board.loser == 'everyone'

                sleep(1.4)

            elif self.score1 < 17:
                pass

        if board.loser == 'Dealer':
            dealer.money -= player.total_bet
            print(f"Dealer loses ${player.total_bet}."
                  f"(Total: ${dealer.money})")
            sleep(1.4)
            player.money += player.total_bet*2
            print(f"Player wins double the bet, ${player.total_bet*2}."
                  f"(Total: ${player.money})")
            sleep(1.4)
            board.pause()

        elif board.loser == "Player":
            print(f"Player loses ${player.total_bet}."
                  f"(Total: ${player. money})")
            sleep(1.4)
            dealer.money += player.total_bet
            print(f"Dealer wins ${player.total_bet}."
                  f"(Total: ${dealer.money})")
            sleep(1.4)
            board.pause()

        elif board.loser == "everyone":
            player.money += player.total_bet
            sleep(1.4)
            board.pause()

    def play(self):

        if self.name == "Player":
            self.decision = int(input("1. Draw \n"
                                 "2. Draw final card and double bet \n"
                                 "3. End turn \n"))

        elif self.name == 'Dealer':
            if self.revealed == False:
                self.revealed = True
                self.reveal()

            if self.score1 >= 17:
                self.decision = 3
            else:
                self.decision = 1

        self.eval_loss()
        sleep(1.4)

        if self.decision == 1:
            self.draw()
            board.display()
            self.eval_loss()
            if board.loser == "Noone":
                self.play()

        elif self.decision == 2:
            self.bet(self.total_bet)
            self.draw()
            board.display()
            self.eval_loss()
            self.end_turn()

        elif self.decision == 3:
            self.end_turn()


    def end_turn(self):
        pass

###################################

class Board:

    def __init__(self):
        self.loser = ""
        self.deck = []

    def create_deck(self):

        global card_value
        card_value = {}
        for shapes in ("Cloves ", "Hearts ", "Spades ", "Diamonds "):
            #Deck creation with pure numbers
            for nums in range(1, 14):
                self.deck.append(shapes+str(nums))

                if nums == 1:
                    card_value[shapes+str(nums)] = 'special'
                elif nums > 10:
                    card_value[shapes+str(nums)] = 10
                else:
                    card_value[shapes+str(nums)] = nums

        #CONVERTING CARDS TO JACK, QUEEN, KING, ACE
        for cards in self.deck:
            index = self.deck.index(cards)
            old_card = cards
            if '11' in cards:
                new = cards.replace('11', 'Jack')
            elif '12' in cards:
                new = cards.replace('12', 'Queen')
            elif '13' in cards:
                new = cards.replace('13', 'King')
            elif '1' in cards and '10' not in cards:
                new = cards.replace('1', 'Ace')
            try:
                if bool(new):
                    #If a card was replaced
                    card_value[new] = card_value[cards]
                    card_value.pop(cards)
                    self.deck.insert(index, new)
                    self.deck.remove(old_card)
                    del new
            except UnboundLocalError:
                pass

    def display(self):
        print("------------------------------------- \n"
              f"Dealer's hand: {dealer.hand} \n"
              f"Dealer's score: {dealer.score1} or {dealer.score2} \n"
              f"Dealer's bank: ${dealer.money}"
              "\n \n \n \n \n"
              f"Player's hand: {player.hand} \n"
              f"Player score: {player.score1} or {player.score2} \n"
              f"Player's bet: ${player.total_bet} \n"
              f"Player's bank: ${player.money}"
              "\n-------------------------------------")
        sleep(3)

    def pause(self):
        a = input("Press anything to continue \n")

    def reset(self):

        print(f"You have ${player.money}! \n"
              f"The dealer has ${dealer.money}. \n")

        self.check_game_over()

        if GAME == True:
            self.create_deck()
            self.loser = "Noone"

            player.hand = []
            player.decision = 0
            player.total_bet = 0

            dealer.hand = []
            dealer.revealed = False

            print("\n \n \n \n \n")

        else:
            pass

    def check_game_over(self):
        for names in {player, dealer}:
            if names.money == 0:
                print(f"{names.name} is broke. {names.name} loses!")
                global GAME
                GAME = False
                break

###################################

class Dealer(CharBase):
    def __init__(self, money):
        super().__init__(money)
        self.name = 'Dealer'
        self.score_hidden1 = 0
        self.score_hidden2 = 0
        self.revealed = False

    def hide(self):
        self.hidden_card = choice(self.hand)
        self.hand.remove(self.hidden_card)
        self.hand.append("HIDDEN CARD")

        if card_value[self.hand[0]] == 'special':
            self.score_hidden1 = 11
            self.score_hidden2 = 1

        else:
            self.score_hidden1 = self.score_hidden2 = card_value[self.hand[0]]

        self.score1 = f"{self.score_hidden1} + x"
        self.score2 = f"{self.score_hidden2} + x"

    def reveal(self):   #Swaps the hidden card with the actual card, revealing it.
        print("Revealing HIDDEN CARD...")
        sleep(1.4)

        self.hand.append(self.hidden_card)
        self.hand.remove("HIDDEN CARD")

        print(f"The HIDDEN CARD was a {self.hidden_card}!")
        sleep(1.4)
        self.calc_score()   #THIS IS TO CHANGE SCORE VALUE TO TRUE SCORE
        board.display()

###################################

class Player(CharBase):
    def __init__(self, money):
        super().__init__(money)
        self.name = 'Player'
        self.total_bet = 0
        self.decision = 0
        self.betted = False

    def bet(self, bet_amount = 0):
        #Charbase.play() calls this method.

        if bet_amount == 0:
            bet_amount = input(f"How much will you bet? (Min: $1, Max: ${self.money}) \n"
                           "$")

        while not self.betted:

            try:
                bet_amount = int(bet_amount)
            except ValueError:
                print("Bet again.")
                self.bet()
                continue

            if bet_amount > self.money:
                print("You can't bet more than your balance.")
                if self.decision == 2:  #This is when bet() is called from Charbase.play()
                    sleep(1.4)
                    print("Betting all instead.")
                    bet_amount = self.money
                else:
                    self.bet()
                    continue

            elif bet_amount < 1:
                print("Can't bet less than $1.")
                self.bet()
                continue

            if bet_amount <= self.money:
                print(f"Betting ${bet_amount}.")
                self.money -= bet_amount
                self.total_bet += bet_amount
                self.betted = True
                
            sleep(1.4)
        

###################################

if __name__ == '__main__':

    #Game set up
    GAME = True
    board = Board()
    player = Player(100)
    dealer = Dealer(100)

    while GAME == True:

        board.reset()
        if GAME == False:
            break
        else:
            pass

        #PLAYER TURN
        player.bet()
        player.draw(2)
        #END OF PLAYER TURN

        #DEALER TURN
        dealer.draw(2)
        dealer.hide()
        #End OF DEALER TURN

        board.display()

        player.play()

        if board.loser != "Noone":
            continue
        else:
            dealer.play()
