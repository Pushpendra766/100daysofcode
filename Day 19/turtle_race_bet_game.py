from turtle import Turtle, Screen
from random import randint


def create_turtle(colour, position):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=pos)
    return new_turtle


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colours = ['red', 'orange', 'blue', 'green', 'purple', 'yellow']
turtles = []
pos = -100

for i in range(6):
    turtles.append(create_turtle(colours[i], pos))
    pos += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle finishes first.")
            else:
                print(f"You've lost. The {winning_color} turtle finishes first.")

        distance = randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
