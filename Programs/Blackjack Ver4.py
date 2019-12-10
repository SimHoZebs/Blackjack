# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:46:09 2019

@author: Zebs
"""

from random import choice
from time import sleep
import ipdb

###################################

class CharBase:
    def __init__(self, money):
        self.money_in_CharBase = money
        self.hand = []
        self.decision = 0
        self.hand_size_in_CharBase = len(self.hand)
        self.score1_in_CharBase = 0     #SCORE VALUE FOR WHEN ACE == 11
        self.score2_in_CharBase = 0     #SCORE VALUE FOR WHEN ACE == 1

        global playingChar_main

    def draw(self, amount=1):
        cycle = 0

        while cycle != amount:
            drawn_card = choice(board.deck_Board)
            board.deck_Board.remove(drawn_card)
            self.hand.append(drawn_card)

            if self.name == "Dealer" and len(self.hand) <= 2:
                print("Dealer draws a card.")

            else:
                print(f"{self.name} draws {drawn_card}.")

            cycle += 1
            sleep(1.4)

    #Score resets before each calc. Need to change it.

###################################

class Dealer(CharBase):
    def __init__(self, money):
        super().__init__(money)
        self.name = 'Dealer'
        self.socre1_hidden_in_Dealer = 0
        self.score2_in_hidden_in_Dealer = 0
        self.revealed = False

    def hide(self):
        self.hidden_card = choice(self.hand)
        self.hand.remove(self.hidden_card)
        self.hand.append("HIDDEN CARD")

        if card_value[self.hand[0]] == 'special':
            self.socre1_hidden_in_Dealer = 11
            self.score2_in_hidden_in_Dealer = 1

        else:
            self.socre1_hidden_in_Dealer = self.score2_in_hidden_in_Dealer = card_value[self.hand[0]]

        self.score1_in_CharBase = f"{self.socre1_hidden_in_Dealer} + x"
        self.score2_in_CharBase = f"{self.score2_in_hidden_in_Dealer} + x"

    def reveal(self):   #Swaps the hidden card with the actual card, revealing it.
        print("Revealing HIDDEN CARD...")
        sleep(1.4)

        self.hand.append(self.hidden_card)
        self.hand.remove("HIDDEN CARD")

        print(f"The HIDDEN CARD was a {self.hidden_card}!")
        sleep(1.4)
        self.calc_score()   #THIS IS TO CHANGE SCORE VALUE TO TRUE SCORE
        board.display()

    def play(self):
        if self.revealed == False:
            self.revealed = True
            self.reveal()

        if self.score1_in_CharBase >= 17:
            self.decision = 3
        else:
            self.decision = 1

#        self.play_result()

###################################

class Player(CharBase):
    def __init__(self, money):
        super().__init__(money)
        self.name = 'Player' 
        self.total_bet_in_Player = 0
        self.betted_in_Player = False
        self.decided = False

    def bet(self, bet_amount_in_Player = 0):
        #Charbase.play() calls this method.

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
                if self.decision == 2:  #This is when bet() is called from Charbase.play()
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

#        self.check_loss()
        sleep(1.4)
#        self.play_result()

###################################

class Board:

    def __init__(self):
        self.loser_Board = ""
        self.deck_Board = []

    def create_deck_Board(self):
        global card_value
        card_value = {}
        
        for shapes in ("Cloves ", "Hearts ", "Spades ", "Diamonds "):
            #Deck creation with pure numbers
            for nums in range(1, 14):
                self.deck_Board.append(shapes+str(nums))

                if nums == 1:
                    card_value[shapes+str(nums)] = 'special'
                elif nums > 10:
                    card_value[shapes+str(nums)] = 10
                else:
                    card_value[shapes+str(nums)] = nums

        #CONVERTING CARDS TO JACK, QUEEN, KING, ACE
        for cards in self.deck_Board:
            index = self.deck_Board.index(cards)
            oldCard = cards
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
                    self.deck_Board.insert(index, new)
                    self.deck_Board.remove(oldCard)
                    del new
            except UnboundLocalError:
                pass

    def display(self):
        print("------------------------------------- \n"
              f"Dealer's hand: {dealer.hand} \n"
              f"Dealer's score: {dealer.score1_in_CharBase} or {dealer.score2_in_CharBase} \n"
              f"Dealer's bank: ${dealer.money_in_CharBase}"
              "\n \n \n \n \n"
              f"Player's hand: {player.hand} \n"
              f"Player score: {player.score1_in_CharBase} or {player.score2_in_CharBase} \n"
              f"Player's bet: ${player.total_bet_in_Player} \n"
              f"Player's bank: ${player.money_in_CharBase}"
              "\n-------------------------------------")
        sleep(3)

    def pause(self):
        a = input("Press anything to continue \n")

    def reset(self):

        print(f"You have ${player.money_in_CharBase}! \n"
              f"The dealer has ${dealer.money_in_CharBase}. \n")

        self.check_game_over()

        if GAME == True:
            self.create_deck_Board()
            self.loser_Board = "Noone"

            #ipdb.set_trace()
            player.hand = []
            player.decision = 0
            player.total_bet_in_Player = 0
            player.betted_in_Player = False
            try:
                del bet_amount_in_Player
            except UnboundLocalError:   #bet_amount_in_Player does not exist
                pass

            dealer.hand = []
            dealer.revealed = False

            print("\n \n \n \n \n")

        else:
            pass

    def check_game_over(self):
        for names in {player, dealer}:
            if names.money_in_CharBase == 0:
                print(f"{names.name} is broke. {names.name} loses!")
                global GAME
                GAME = False
                break

    def play_result():
    global playingChar_main

    def check_loss():

        if self.score1_in_CharBase > 21:   #WHEN NAME IS PLAYER
           print(f"{self.name}'s score is over 21. {self.name} loses!")
           board.loser_Board = self.name
           sleep(1.4)

        elif playingChar_main == dealer:
            if playingChar_main.score1_in_CharBase >= 17:
                if playingChar_main.score1_in_CharBase > player.score1_in_CharBase:
                    print("Dealer has a higher score. Dealer wins!")
                    board.loser_Board = 'Player'
                elif playingChar_main.score1_in_CharBase < player.score1_in_CharBase:
                    print("Dealer has a lower score. Player wins!")
                    board.loser_Board = self.name
                elif playingChar_main.score1_in_CharBase == player.score1_in_CharBase:
                    print("A draw! Player gets their money back.")
                    board.loser_Board == 'everyone'

                sleep(1.4)

            elif self.score1_in_CharBase < 17:
                pass

        if board.loser_Board == 'Dealer':
            dealer.money_in_CharBase -= player.total_bet_in_Player
            print(f"Dealer loses ${player.total_bet_in_Player}."
                  f"(Total: ${dealer.money_in_CharBase})")
            sleep(1.4)
            player.money_in_CharBase += player.total_bet_in_Player*2
            print(f"Player wins double the bet, ${player.total_bet_in_Player*2}."
                  f"(Total: ${player.money_in_CharBase})")
            sleep(1.4)
            board.pause()

        elif board.loser_Board == "Player":
            print(f"Player loses ${player.total_bet_in_Player}."
                  f"(Total: ${player. money})")
            sleep(1.4)
            dealer.money_in_CharBase += player.total_bet_in_Player
            print(f"Dealer wins ${player.total_bet_in_Player}."
                  f"(Total: ${dealer.money_in_CharBase})")
            sleep(1.4)
            board.pause()

        elif board.loser_Board == "everyone":
            player.money_in_CharBase += player.total_bet_in_Player
            sleep(1.4)
            board.pause()

    def calc_score(self):
        score1_in_calc_score = self.score1_in_CharBase
        score2_in_calc_score = self.score2_in_CharBase

        score1_in_calc_score = 0
        score2_in_calc_score = 0
        hasAce = 0

        for cards in self.hand:
            try:
                score1_in_calc_score += card_value[cards]
                score2_in_calc_score = score1_in_calc_score
            except TypeError:
                """ This occurs when the card in hand is an ACE."""
                score2_in_calc_score += 1
                hasAce += 1

        if hasAce == 1:
            if score1_in_calc_score >= 11:
                score1_in_calc_score += 1
            elif score1_in_calc_score < 11:
                score1_in_calc_score += 11

        elif hasAce > 1:
            score1_in_calc_score += hasAce

        self.score1_in_CharBase = score1_in_calc_score
        self.score2_in_CharBase = score2_in_calc_score

###################################

playingChar_main = 'Noone'

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

        #CARD DRAW PHASE
        playingChar_main = player
        playingChar_main.bet()
        playingChar_main.draw(2)
        board.calc_score()

        playingChar_main = dealer
        playingChar_main.draw(2)
        playingChar_main.hide()
        board.calc_score()
        #End of CARD DRAW PHASE

        #show BOARD
        board.display()

        playingChar_main = player
###              
        playingChar_main.play()

        if playingChar_main.decision == 1:
            playingChar_main.draw()
            board.display()
            playingChar_main.check_loss()

        if board.loser_Board == "Noone":
            playingChar_main.decided = False
            playingChar_main.play()

        elif playingChar_main.decision == 2:
            playingChar_main.betted_in_Player = False

            playingChar_main.bet(playingChar_main.total_bet_in_Player)
            playingChar_main.draw()
            board.display()
            playingChar_main.check_loss()

        elif playingChar_main.decision == 3:
            pass

        playingChar_main.calc_score()

        board.display()

        board.check_loss()

        if board.loser_Board != "Noone":
            continue
        else:
            playingChar_main = dealer
            playingChar_main.play()
            play_result()
###