import blackjack_functions as bjf
print("Welcome to Blackjack Offline Gambling")
x = bjf.set_difficulty()
amount = bjf.how_much_gamble()
winner_1 = bjf.blackjack_game(1,x)
winner_2 = bjf.blackjack_game(2,x)
winner_3 = bjf.blackjack_game(3,x)
bjf.final_winner_gambling(winner_1, winner_2, winner_3, x, amount)

