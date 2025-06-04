"""
Assignment: Number Guessing Game
For Cognizant Externship – Python Fundamentals
Description:
This script generates a random number between 1 and 100.
The user has 10 attempts to guess it correctly.
Feedback is given after each guess, and the number of attempts is tracked.

Jordan Wang
6/4/2025
"""

import random

# generating a random number between 1 and 100
number_to_guess = random.randint(1, 100)

guess_count = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print("Try to guess the number I'm thinking of between 1 and 100.")
print(f"You have {max_attempts} attempts. Good luck.\n")

# this is the guessing loop
while guess_count < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:  # This is so that it tells the user that the number is invalid instead of an error statement
        print("That's not a valid number. Try again.\n")
        continue

    guess_count += 1

    if guess < number_to_guess:
        print("Too low! Try again.\n")
    elif guess > number_to_guess:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You guessed it in {guess_count} attempt(s)!")
        break
else:
    print(f"Game over! The number was {number_to_guess}. Better luck next time!")
