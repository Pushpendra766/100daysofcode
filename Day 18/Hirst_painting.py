from turtle import Turtle, Screen
from random import choice
tim = Turtle()
screen = Screen()
colour_list = [(144, 76, 51), (189, 165, 119), (166, 152, 36), (46, 110, 135), (14, 46, 85), (146, 56, 82), (149, 171, 177), (60, 120, 100), (141, 186, 176), (64, 152, 169), (84, 36, 31), (219, 210, 96), (109, 36, 30), (165, 99, 131), (100, 145, 110), (90, 122, 172), (163, 139, 159), (177, 104, 83), (55, 52, 85), (206, 182, 195), (64, 44, 58), (69, 52, 73), (171, 202, 195), (170, 201, 204), (213, 183, 177), (183, 190, 204), (36, 73, 82), (43, 52, 51), (7, 120, 118)]
tim.hideturtle()
tim.penup()
tim.goto(-370, -300)
tim.showturtle()
tim.pendown()
screen.colormode(255)
tim.speed('fastest')
tim.hideturtle()
for i in range(10):
    for _ in range(10):
        # tim.pencolor(choice(colour_list))
        tim.pendown()
        tim.dot(20, choice(colour_list))
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.backward(500)


screen.exitonclick()
