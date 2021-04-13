from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.color('white')
        self.speed('fastest')

    def up(self):
        if self.ycor() < 240:
            self.forward(20)

    def down(self):
        if self.ycor() > -240:
            self.backward(20)