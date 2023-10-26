
################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

#################### Number Guessing Game Objectives ####################
# Choosing a random number between 1 and 100.
# Make a function to set difficulty
# User guesses a number
# Function to check user's guess against actual answer
# Track the number of turns and reduce by 1 if answer is wrong
# Repeat the guessing functionality if answer is wrong

from random import randint
from art import logo
EASY = 10
HARD = 7

##### Whatever functions needed here! #####
def check(guess, number, turns):
  '''Checks answers. Returns the number of turns left.'''
  if guess > number:
    print("Too high!")
    return turns - 1
  elif guess < number:
    print("Too low!")
    return turns - 1
  else:
    print(f"You got it! The number is {number}.")

def difficulty():
  '''Sets the difficulty of the game.'''
  level = input("Choose the difficulty, type easy or hard: ").lower()
  if level == "easy":
    return EASY
  elif level == "hard":
    return HARD
  else: #BUG HERE! GOTTA CHECK IT LATER
    print("Invalid. Try again.")
    difficulty()
  
def game():
  '''Starts the game.'''
  print(logo)
  print("Welcome to Guess the Number.")
  print("Guess a number between 1 and 100.")
  number = randint(1, 100)
  print(f"The number is: {number}")
  
  turns = difficulty()
  guess = 0
  while guess != number:
    print(f"You have {turns} tries.")
    guess = int(input("Make a guess: "))
    turns = check(guess, number, turns)
    if turns == 0:
      print("Game over.")
      return
    elif guess != number:
      print("Guess again!")
game()






