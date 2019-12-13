def check_loss_old(self):

    if self.score1_in_CharBase > 21:   #WHEN NAME IS PLAYER
       print(f"{self.name}'s score is over 21. {self.name} loses!")
       main.loser = self.name
       delay()

    elif playing_char == dealer:
        if playing_char.score1_in_CharBase >= 17:
            if playing_char.score1_in_CharBase > player.score1_in_CharBase:
                print("Dealer has a higher score. Dealer wins!")
                main.loser = 'Player'
            elif playing_char.score1_in_CharBase < player.score1_in_CharBase:
                print("Dealer has a lower score. Player wins!")
                main.loser = self.name
            elif playing_char.score1_in_CharBase == player.score1_in_CharBase:
                print("A draw! Player gets their money back.")
                main.loser == 'everyone'

            delay()

        elif self.score1_in_CharBase < 17:
            pass

    if main.loser == 'Dealer':
        dealer.money_in_CharBase -= player.total_bet_in_Player
        print(f"Dealer loses ${player.total_bet_in_Player}."
              f"(Total: ${dealer.money_in_CharBase})")
        delay()
        player.money_in_CharBase += player.total_bet_in_Player*2
        print(f"Player wins double the bet, ${player.total_bet_in_Player*2}."
              f"(Total: ${player.money_in_CharBase})")
        delay()
        board.pause()

    elif main.loser == "Player":
        print(f"Player loses ${player.total_bet_in_Player}."
              f"(Total: ${player. money})")
        delay()
        dealer.money_in_CharBase += player.total_bet_in_Player
        print(f"Dealer wins ${player.total_bet_in_Player}."
              f"(Total: ${dealer.money_in_CharBase})")
        delay()
        board.pause()

    elif main.loser == "everyone":
        player.money_in_CharBase += player.total_bet_in_Player
        delay()
        board.pause()