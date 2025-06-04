# Number Guessing Game

This project is a simple terminal-based guessing game built with Python. It was created as part of my Cognizant externship to practice using loops, conditionals, and user input in a fun and interactive way.

## How It Works

- The program randomly selects a number between 1 and 100.
- The user has up to **10 chances** to guess the number.
- After each guess, feedback is provided:
  - “Too high! Try again.”
  - “Too low! Try again.”
  - “Congratulations! You guessed it!”

If the user doesn’t guess it within 10 attempts, the program ends and reveals the correct number.

## Features

- `while` loop for repeated input
- Input validation using `try`/`except`
- Tracks and limits the number of attempts
- Clean and readable logic for beginners

## File

- `main.py` — contains the full guessing game logic

## Running the Program

Make sure Python is installed, then run:
python3 main.py
