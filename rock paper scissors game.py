# The `# rock paper scissors game` is a comment in Python code that serves as a brief description or
# title for the following code block. In this case, it indicates that the code below is implementing a
# rock-paper-scissors game in Python. Comments in code are ignored by the Python interpreter and are
# used to provide information or context about the code for developers reading the code.

import time
import os
import getpass

def print_intro():
    print("-- ROCK PAPER SCISSORS --".center(os.get_terminal_size().columns))
    print()
    time.sleep(1)

def get_player_names():
    player1 = input("Player 1's name: ")
    player2 = input("Player 2's name: ")
    print()
    return player1, player2

def get_objective():
    while True:
        try:
            objective = int(input("What's the winning score / objective? "))
            if objective > 0:
                return objective
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_move(player):
    while True:
        move = getpass.getpass(f"{player}'s turn (r/p/s): ").lower()
        if move in ['r', 'p', 's']:
            return move
        else:
            print("Invalid move. Please enter 'r' for rock, 'p' for paper, or 's' for scissors.")

def determine_winner(player1move, player2move):
    outcomes = {
        ('r', 'r'): 'tie',
        ('r', 'p'): 'player2',
        ('r', 's'): 'player1',
        ('p', 'r'): 'player1',
        ('p', 'p'): 'tie',
        ('p', 's'): 'player2',
        ('s', 'r'): 'player2',
        ('s', 'p'): 'player1',
        ('s', 's'): 'tie'
    }
    return outcomes[(player1move, player2move)]

def main():
    print_intro()
    player1, player2 = get_player_names()
    objective = get_objective()

    print("Type 'r' for rock, 'p' for paper and 's' for scissors")
    print("Your input won't be visible. So just input and press enter.")
    time.sleep(11)

    player1score = 0
    player2score = 0
    round_number = 0

    while player1score < objective and player2score < objective:
        round_number += 1
        os.system('cls' if os.name == 'nt' else 'clear')

        player1move = get_move(player1)
        player2move = get_move(player2)
        print()
        time.sleep(1)

        print(f"{player1}'s move: {player1move}")
        print(f"{player2}'s move: {player2move}")
        print()
        time.sleep(3)

        winner = determine_winner(player1move, player2move)

        if winner == 'tie':
            print("It's a tie")
        else:
            winner_name = player1 if winner == 'player1' else player2
            print(f"Winner of round {round_number} is: \033[92m{winner_name}\033[0m")
            if winner == 'player1':
                player1score += 1
            else:
                player2score += 1

        print(f"{player1}'s score: {player1score}")
        print(f"{player2}'s score: {player2score}")
        print()
        time.sleep(3)

    final_winner = player1 if player1score >= objective else player2
    print("The final winner of this game is...".center(os.get_terminal_size().columns))
    time.sleep(1)
    print("*drumroll*".center(os.get_terminal_size().columns))
    time.sleep(3)
    print(f"\033[92m{final_winner.center(os.get_terminal_size().columns)}\033[0m")

if __name__ == "__main__":
    main()
