import random

# Constants for moves
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

# Mapping choices to emojis
emojis = {ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️'}
choices = tuple(emojis.keys())   # tuple to avoid modification

def get_user_choice():
    while True:
        user_choice = input("Choose (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice ❌")

def display_choice(user_choice, computer_choice):
    print(f'YOU CHOSE: {emojis[user_choice]}')
    print(f'COMPUTER CHOSE: {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a DRAW 🤝")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("You WIN 🎉✨")
    else:
        print("You LOSE 😢")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        
        display_choice(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        should_continue = input("Do you want to continue playing? (y/n): ").lower()
        if should_continue == "n":
            print("Thanks for playing! 👋")
            break

# Start the game
play_game()
