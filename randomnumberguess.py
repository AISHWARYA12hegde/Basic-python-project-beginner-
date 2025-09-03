#randomnumber guess game
#ask user to make a guess and checck
import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number: "))
        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print("Congrats!!!! You guessed it right champ!")
            break   # exit loop once guessed correctly
    except ValueError:
        print("Please enter a valid number")
