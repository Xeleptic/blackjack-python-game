import random



"""Part 1: Initial Game Setup Creation"""
def create_deck ():
    deck = []
    for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
        for card in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
            deck.append((card, suit))
    return deck

def shuffle_deck (deck):
    random.shuffle(deck)
    return deck

def deal_card (deck, hand):
    hand.append(deck[0])
    deck.pop(0)
    return hand

def game_setup ():
    deck = create_deck()
    deck = shuffle_deck(deck)
    player_hand = []
    dealer_hand = []
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    if dealer_hand[0] == "Ace":
        print(f'The dealer\'s up card is an {dealer_hand[0][0]} of {dealer_hand[0][1]}.')
    else:
        print(f'The dealer\'s up card is a {dealer_hand[0][0]} of {dealer_hand[0][1]}.')
    return player_hand, dealer_hand, deck



"""Part 2: Point Calculation"""
def calculate_points (hand):
    hand_points = sorted(hand)
    points = 0
    # adds points for all face cards (Jack, Queen, King)
    for n,card in enumerate(hand_points):
        if card[0] in ["Jack", "Queen", "King"]:
            points += 10
            hand_points.pop(n)
            hand_points.insert(n, ("0", "Place Holder"))
    # adds points for all normal cards
    for card in hand_points:
        if card[0] != "Ace":
            points += int(card[0])
    ace_count = 0
    # adds points for all aces
    for card in hand_points:
        if card[0] == "Ace":
            ace_count += 1
            points += 11
    # fixes value of previous aces if it's too high
    for ace in range(ace_count):
        if points > 21:
            points -= 10
            ace_count -= 1
    return points



"""Part 3: Displaying Player/Dealer Information"""
def display_player_info (player_hand):
    print(f'\nYou have the following cards:')
    for cards in player_hand:
        print(f'    {cards[0]} of {cards[1]}')
    player_points = calculate_points(player_hand)
    print(f'You currently have {player_points} points')

def display_player_final_info (player_hand):
    print(f'\nYour final hand is the following:')
    for cards in player_hand:
        print(f'    {cards[0]} of {cards[1]}')
    player_points = calculate_points(player_hand)
    print(f'Your ended with {player_points} points')

def display_dealer_info (dealer_hand):
    print(f'\nThe dealer\'s final hand is the following:')
    for cards in dealer_hand:
        print(f'    {cards[0]} of {cards[1]}')
    dealer_points = calculate_points(dealer_hand)
    print(f'The dealer ended with {dealer_points} points')
    if dealer_points > 21:
        print(f'The dealer has busted!')



"""Part 4: Player/Dealer Turn"""
# note: these turns are based not on the instructions, but on how you actually play Blackjack when alone against the dealer, as approved by you in class.
def player_turn (player_hand, deck):
    choice = "hit"
    while choice == "hit":
        player_points = calculate_points(player_hand)
        if player_points > 21:
            display_player_final_info(player_hand)
            print("You have busted!")
            return player_hand, deck
        choice = input("Do you want to hit or keep [hit/keep]?\n"
                   "Enter answer here: ")
        if choice == "hit":
            player_hand = deal_card(deck,player_hand)
            display_player_info(player_hand)
        elif choice == "keep":
            player_hand = player_hand
            display_player_final_info(player_hand)
        else:
            print("That is not a valid choice. Try again.")
            choice = "hit"
    return player_hand, deck

def dealer_turn (deck, dealer_hand, x):
    choice = "hit"
    while choice == "hit":
        dealer_points = calculate_points(dealer_hand)
        if dealer_points > 21:
            choice = "keep"
        elif dealer_points < x*21:
            deal_card(deck, dealer_hand)
            choice = "hit"
        else:
            choice = "keep"
    display_dealer_info(dealer_hand)
    return dealer_hand, deck



"""Part 5: Crowning a Winner"""
def decide_winner (player_hand, dealer_hand):
    player_points = calculate_points(player_hand)
    dealer_points = calculate_points(dealer_hand)
    if dealer_points > 21 and player_points <= 21:
        winner = "Player"
    elif player_points > 21 and dealer_points <= 21:
        winner = "Dealer"
    else:
        dealer_gap = abs(21 - dealer_points)
        player_gap = abs(21 - player_points)
        if player_gap > dealer_gap:
            winner = "Dealer"
        elif player_gap < dealer_gap:
            winner = "Player"
        else:
            winner = "None"
    return winner

def display_winner (winner):
    if winner == "Dealer":
        print(f'\nThe dealer has won!')
    elif winner == "Player":
        print(f'\nYou have won!')
    elif winner == "None":
        print(f'\nThis game was a draw.')

def final_winner (winner_1, winner_2, winner_3):
    player_wins = 0
    dealer_wins = 0
    for winner in [winner_1, winner_2, winner_3]:
        if winner == "Player":
            player_wins += 1
        elif winner == "Dealer":
            dealer_wins += 1
    print(f'\n\n\nThe final score ratio is:'
          f'\n{player_wins} player wins:{dealer_wins} dealer wins')
    if player_wins > dealer_wins:
        print(f"You won!")
    elif player_wins < dealer_wins:
        print(f"You lost!")
    else:
        print(f"This series was a draw!")
    return



"""Part 6: Additional Stuff I Added For No Good Reason"""
def set_difficulty ():
    difficulty = input(f"Please select a difficulty [easy, medium, hard]:"
                       f"\n*Note: Higher difficulties mean more dabloons if you win!"
                       f"\nEnter choice: ")
    # x values were decided by taking the ideal x value, 0.81 (17/21 rounded up), then removing 20 every time the difficulty level decreases
    x = 0.61
    if difficulty == "easy":
        x = 0.41
    elif difficulty == "medium":
        x = 0.61
    elif difficulty == "hard":
        x = 0.81
    elif difficulty == "Mommy I want free wins":
        x = 1.05
    else:
        print("Invalid difficulty. Difficulty will be set to medium by default.")
    return x

def how_much_gamble ():
    amount = "Invalid"
    while amount == "Invalid":
        amount = input(f"\nPlease enter how many dabloons you want to gamble:"
                   f"\n*Note: Mimimum amount: 10 dabloons"
                   f"\n       Maximum amount: 10 000 dabloons"
                   f"\nEnter amount only (no units): ")
        try:
            amount_int = int(amount)
            if int(amount) not in range(10, 10001):
                amount = "Invalid"
                print("Invalid amount. Please enter a number within the allowed range.")
            else:
                amount = amount_int
        except ValueError:
            amount = "Invalid"
            print("Invalid input. Please enter a number within the allowed range.")
    return amount

def final_winner_gambling (winner_1, winner_2, winner_3, x, amount):
    player_wins = 0
    dealer_wins = 0
    for winner in [winner_1, winner_2, winner_3]:
        if winner == "Player":
            player_wins += 1
        elif winner == "Dealer":
            dealer_wins += 1
    print(f'\n\n\nThe final score ratio is:'
          f'\n{player_wins} player wins:{dealer_wins} dealer wins')
    if x == 0.41:
        mode = "easy difficulty"
    elif x == 0.61:
        mode = "medium difficulty"
    elif x == 0.81:
        mode = "hard difficulty"
    else:
        mode = "a difficulty that makes the game literally almost impossible to lose"
    if player_wins > dealer_wins:
        print(f"You won on {mode}!"
              f"\nYou won {int(amount + amount*x)} dabloons! "
              f"\nGood job kiddo, I see your potential. Keep at it bucko.")
    elif player_wins < dealer_wins:
        print(f"You lost on {mode}."
              f"\nYou lost {amount} dabloons. "
              f"\nCome on kiddo, one more game. You're due for a win at this point.")
    else:
        print(f"This series, played on {mode}, was a draw!"
              f"\nYour dabloons have been returned to your bank account."
              f"\nCome on kiddo, one more game. You're due for a win at this point.")
    return



"""Part 7: Final Product"""
def blackjack_game (round_number, x):
    print (f'\n\nRound {round_number}')
    player_hand, dealer_hand, deck = game_setup()
    display_player_info(player_hand)
    player_hand, deck = player_turn(player_hand, deck)
    dealer_hand, deck = dealer_turn(deck, dealer_hand, x)
    winner = decide_winner(player_hand, dealer_hand)
    display_winner(winner)

    return winner

