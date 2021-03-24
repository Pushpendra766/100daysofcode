#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("  Tip Calculator ")
bill = float(input("What is the total bill ? \n₹"))
tip = int(input("What percentage do you want to give tip ?"))
num_of_people = int(input("How many are you ? "))
bill_with_tip = bill + (bill*tip/100)
to_pay = bill_with_tip/num_of_people
print(f"Each of you should pay {to_pay:.2f}")
