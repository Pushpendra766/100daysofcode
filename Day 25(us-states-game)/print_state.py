from turtle import Turtle
FONT = ("Courier", 8, "normal")
ALIGNMENT = "center"


class PrintState(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def print_state_name(self, x_cor, y_cor, state_name):
        self.goto(x_cor, y_cor)
        self.write(state_name, align=ALIGNMENT, font=FONT)
