from time import sleep
import ipdb

def delay(duration=1.4):
    duration = 0
    sleep(duration)

class Board:

    deck = []
    CARD_VALUE = {}

    def create_deck(self):
        """
        Creates cards then appends each in to deck.
        """
        for shape in ("Cloves ", "Hearts ", "Spades ", "Diamonds "):
            #Deck creation with pure numbers
            for num in range(1, 14):

                if num == 1:
                    self.deck.append(shape+"Ace")
                elif num == 11:
                    self.deck.append(shape+"Jack")
                elif num == 12:
                    self.deck.append(shape+"Queen")
                elif num == 13:
                    self.deck.append(shape+"King")
                else:
                    self.deck.append(shape+str(num))

    def generate_CARD_VALUE(self):
        """
        Keys are added to CARD_VALUE, where key = cards and their value = items.
        """
        for card in self.deck:

            try:
                if int(card[-1]) == 0:
                    self.CARD_VALUE[card] = 10
                else:
                    self.CARD_VALUE[card] = int(card[-1])

            except ValueError:  #card[-1] == string
                if "Ace" in card:
                    self.CARD_VALUE[card] = "SPECIAL"
                else:
                    self.CARD_VALUE[card] = 10