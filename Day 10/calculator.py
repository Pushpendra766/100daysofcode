#Calculator
from replit import clear
from art import logo
#addition
def add(a,b):
  return a+b

#subtraction
def subtract(a,b):
  return a-b

#multiply
def multiply(a,b):
  return a*b

#divide
def divide(a,b):
  return a/b

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
} 
def calculator(): 
  clear()
  print(logo)
  num1=float(input("What is the first number? : "))
  choice = True

  for operation in operations:
    print(operation)

  while choice:  
    operation_symbol = input("Pick an operation :")
    num2=float(input("What is another number ? : ")) 
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol}  {num2} = {answer}") 
    
    if input (f"Type 'y' to continue calculating with {answer} or 'n' to start new : ") == 'y':
      num1 = answer
    else:
      choice = False
      calculator()

calculator()      
