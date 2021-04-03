import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def compare( guess, number,attempts):
  """ Compares guess and number. """
  if guess > number:
    print("Too high.\nGuess again.")
    return attempts -1
  elif guess<number:
    print("Too low.\nGuess again.")
    return attempts -1
  elif guess == number:
    print(f"You got it! The answer is {guess} ")
    return attempts  

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1,100)
  difficulty = input("Choose a difficulty .Type 'easy' or 'hard' ")
  if difficulty == 'easy':
    attempts = EASY_LEVEL_TURNS
  elif difficulty == 'hard':
    attempts = HARD_LEVEL_TURNS  

  guess = 0 

  while guess != number and attempts > 0 :  
    print(f"You have {attempts} attempts to guess the number.")
    guess = int(input("Make a guess : "))
    
    attempts = compare(guess,number,attempts)

  if attempts < 1:
      print(f"You are out of attempts.You lose. The number was {number}")
game()    
