# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:46:09 2019

@author: Zebs
"""

from random import choice
from msvcrt import getch
from Zebsential import Debug, DoDebug

DoDebug(1)

KEY_PRESS = getch
GAME = True

"""
To do:
    - Auto add number up


"""

class CharBase:

    def __init__(self, money):
        self.money = money
        self.hand = []
        self.score1 = 0
        self.score2 = 0
        #score2 is an optional display for when player has an Ace but
        #does not add up to 21.

        #score is total of card value of cards in hand.
        self.hand_size = len(self.hand)

    def draw(self, amount=1):

        Debug(f"{self.name} drawing card")
        cycle = 0
        while cycle != amount:
            Debug(f"cycle is {cycle}. Drawing till it equals {amount}.\n"
                  f"{self.name} has {self.hand} in hand.")
            drawn_card = choice(deck)
            Debug(f"{self.name} drew {drawn_card}.")
            deck.remove(drawn_card)
            Debug(f"Removing {drawn_card} from deck.\n"
                  f"Cards left in deck are {deck}", 0)
            self.hand.append(drawn_card)
            cycle += 1
            if cycle == amount:
                Debug(f"cycle equals to {cycle}. Stopping draw. "
                      f"{self.name} now has {self.hand}")
        self.calc_score()

    #Score resets before each calc. Need to change it.
    def calc_score(self):
        Debug("Calculating hand score...")
        self.score1 = 0
        self.score2 = 0

        for cards in self.hand:
            Debug(f"Found {cards} in {self.name} hand.")
            try:
                Debug(f"Value of {cards} is {card_value[cards]}.")
                self.score1 += card_value[cards]
                Debug(f"score of {self.name} is {self.score1}")
                self.score2 = self.score1
                Debug(f"Alternate score is {self.score2}")
            except TypeError:
                Debug(f"{cards} is {card_value[cards]}.")
                self.score2 += 1
                Debug(f"{cards} has value or either 1 or 11. \n"
                      f"Alternate score will show {self.score2}")
                if self.score1 > 11:
                    Debug(f"It seems that {self.name}'s score is {self.score1} \n"
                          "which is too large to add 11.")
                    self.score1 += 1
                else:
                    Debug(f"Score is {self.score1}, which is low enough \n"
                          f"to add 11 to.")
                    self.score1 += 11
            except KeyError:
                Debug(f"Revealing {cards}. It's actually {self.hidden_card}.")
                Debug(f"{self.hidden_card} has value {card_value[self.hidden_card]}.")
                self.score1 += card_value[self.hidden_card]
                Debug(f"Main score displaying as {self.score1}.")
                self.score2 = self.score1
                Debug(f"Alternate score is {self.score2}")

        self.eval_loss()

    def eval_loss(self):
        if self.name == "Dealer" and self.score1 > 21:
            print(f"Score is over 21. {self.name} loses!")
            player.money += player.bet_amount*2
            Board.loser = "Dealer"
        elif self.name == "Player" and self.score1 > 21:
            print(f"Score is over 21. {self.name} loses!")
            Board.loser = "Player"
        pass


class Dealer(CharBase):
    name = 'Dealer'

    def hide(self):
        self.hidden_card = choice(self.hand)

        Debug(f"hiding card {self.hidden_card}")
        self.hand.remove(self.hidden_card)
        self.hand.append("HIDDEN CARD")

        try:
            self.score1 -= card_value[self.hidden_card]
            self.score2 = self.score1
        except TypeError:
            self.score2 -= 1
            if self.score1 > 11:
                self.score1 -= 1
            else:
                self.score1 -= 11

    def play(self):
        self.calc_score()
        while self.score1 < 17 or self.score2 < 17:
            Debug("Score is less than 17; Drawing again.")
            self.draw()

        Debug(f"Score is {self.score1}. Ending draw.")
        #draw until 17 or higher or bust

class Player(CharBase):
    name = 'Player'
    state = ""
    bet_amount = 0
    decision = 0

    def bet(self):
        bet_amount = input(f"How much will you bet? (Min: $1, Max: ${self.money}) \n"
                           "$")
        self.bet_amount = int(bet_amount)

        if self.bet_amount > self.money:
            print("You cant' bet more than you have.")
            if self.decision == 2:
                print("Betting all instead.")
                self.bet_amount += self.money

            self.bet()
        if self.bet_amount < 1:
            print("Can't bet less than $1.")
            self.bet()
        else:
            print(f"Betting ${bet_amount}.")
            self.money -= self.bet_amount
#--------------------------------------------------------
    def play(self):

        Board.display()

        decision = int(input("1. Draw \n"
                         "2. Draw final card and double bet \n"
                         "3. End turn \n"))
        Debug(f"input received: {decision}")

        if decision == 1:
            self.draw()
            if not bool(Board.loser):
                self.play()
                Board.display()

        elif decision == 2:
            self.bet(self.bet_amount)
            self.draw()
            self.end_turn()
            Board.display()
        elif decision == 3:
            self.end_turn()
#--------------------------------------------------------
    def end_turn(self):
        print("Ending turn.")
        dealer.play()
        pass


class Board:
    loser = ""

    def reset(self):
        self.create_deck()

        player.hand = []
        player.decision = 0
        player.bet_amount = 0

        dealer.hand = []

    def create_deck():

        global deck
        deck = []
        global card_value
        card_value = {}
        for shapes in ("Cloves ", "Hearts ", "Spades ", "Diamonds "):
            #Deck creation with pure numbers
            for nums in range(1, 14):
                Debug(f"Creating card {shapes + str(nums)}")
                deck.append(shapes+str(nums))

                if nums == 1:
                    card_value[shapes+str(nums)] = 'special'
                elif nums > 10:
                    card_value[shapes+str(nums)] = 10
                else:
                    card_value[shapes+str(nums)] = nums

        for cards in deck:
            #Refining card names to human readable ones
            Debug(f"Checking {cards} for refining.")
            index = deck.index(cards)
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
                    Debug(f"{cards} was refined to {new}!")
                    card_value[new] = card_value[cards]
                    card_value.pop(cards)
                    deck.insert(index, new)
                    deck.remove(old_card)
                    del new
            except UnboundLocalError:
                Debug(f"{cards} doesn't require refinining.")

    def display():
        print("------------------------------------- \n"
                f"Dealer's hand: {dealer.hand} \n"
                f"Dealer's score: {dealer.score1} + x or {dealer.score2} + x"
              "\n \n \n \n \n"
              f"Player's hand: {player.hand} \n"
              f"Player score: {player.score1} or {player.score2} \n"
              f"Player's bet: ${player.bet_amount}"
              "\n-------------------------------------")


if __name__ == '__main__':

    #Game set up
    player = Player(100)
    dealer = Dealer(100)

    while GAME == True:

        Board.reset()

        #Player turn
        print(f"You have ${player.money}!")

        player.bet()
        player.draw(2)
        #End of player turn

        #dealer turn
        dealer.draw(2)
        dealer.hide()
        #End of dealer turn

        player.play()
        if bool(Board.loser):
            continue