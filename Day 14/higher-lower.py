#This game is guessing game where you have to guess which celebrity or brand have more Insta followers
from art import logo,vs
from game_data import data
import random
from replit import clear

#pick a account from top 50 listed
def pick_accounts():
  return random.choice(data)

#compare followers with user choice
def compare(choice_A,choice_B,choice):
  if choice_A >= choice_B and choice == 'A':
    return True
  elif choice_A <= choice_B and choice == 'B':
    return True
   
#Shows the current score
def update_score(ans,score):
  if ans == True:
    print(logo)
    print(f"You're right! Current score: {score}")
    return False
  else:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    return True

score = 0
end_of_game = False 
print(logo)
choice_A = pick_accounts()

while not end_of_game :
  
  choice_B = pick_accounts()

  while choice_A == choice_B:
     choice_B = pick_accounts()
  print(f"Compare A : {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}.")
  print(vs)
  print(f"Against B : {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}.")
  choice = (input("Who has more followers? Type 'A' or 'B': ")).upper()
  ans = compare(choice_A['follower_count'],choice_B['follower_count'],choice)
  if(ans == True):
    score += 1
    choice_A = choice_B
  clear()
  end_of_game = update_score(ans,score)
