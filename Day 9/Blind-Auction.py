from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

bids = {}
answer = 'yes'
while answer == 'yes': 
  print(logo)
  print("Welcome to Blind Auction")
  name = input("What's your name ? : ")
  bid = input("What's your bid ? : $")
  bids[name] = bid
  answer = input("Do you want more bids ? Type 'yes' or 'no'\n")
  if(answer == 'yes'):
    clear()
max_bid = 0    
for people in bids:
  if int(bids[people]) > max_bid:
    max_bid = int(bids[people])
    max_bidder = people
print(f" Winner is {max_bidder} with {max_bid} ")  
