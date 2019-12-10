from Blackjack_Dealer import Dealer
from Blackjack_Player import Player

from time import sleep

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