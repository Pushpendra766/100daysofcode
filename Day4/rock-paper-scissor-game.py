import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps=[rock,paper,scissors]

choice=int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissor\n"))
if(choice<0 or choice>2):
  print("Invalid input. You lose!")
else:
  print(rps[choice])   

  c_choice= random.randint(0,2)
  print("Computer choose : "  )
  print(rps[c_choice])
    

  a = str(choice) + str(c_choice)

  if(a=='01' or a=='12' or a=='20'):
    print("You lose ")
  elif(a=='10' or a=='21' or a=='02'):
    print("You Won ")
  else:
    print("Same choice. Tie")    


