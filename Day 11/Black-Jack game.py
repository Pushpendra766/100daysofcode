## Rules :-
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from replit import clear
from art import logo

def deal_card():
  """ Returns a random card from the deck."""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21:
      return 0 
  if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
  if computer_score == user_score:
    return "Draw 🤨"
  if computer_score == 0:
   return "Lose , Opponent has BlackJack 😵"
  elif user_score == 0:
    return "Win with a BlackJack 😎"
  elif  user_score>21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over.You win 😁 "
  elif user_score > computer_score:
    return "You win 🤓"
  else:
    return "You lose 😩"        

def play_game():
  print(logo)
  user_cards  = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    print(f"Your cards {user_cards}, your score {user_score} ")
    print(f"Dealer first card {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or  user_score>21:
      is_game_over  = True
    else:
      ans = input("Type 'y' to get another card, type 'n' to pass:")
      if ans=='y':
        user_cards.append(deal_card())
      else:
        is_game_over = True  
        

  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand {user_cards}, final score {user_score}")
  print(f"Dealer's final hand {computer_cards}, final score {computer_score}")
  print(compare(user_score,computer_score))  

while input("Do you want to play game of BlackJack ? \nType 'y' or 'n' : ") == 'y':
  clear()
  play_game()

