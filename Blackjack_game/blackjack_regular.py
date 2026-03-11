import blackjack_functions as bjf
print("Welcome to Blackjack. The game will start soon, enjoy.")
x = 0.61
winner_1 = bjf.blackjack_game(1,x)
winner_2 = bjf.blackjack_game(2,x)
winner_3 = bjf.blackjack_game(3,x)
bjf.final_winner(winner_1, winner_2, winner_3)
