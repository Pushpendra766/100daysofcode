from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.level = 1
        self.write(f"Level : {self.level}", align='left', font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align='center', font=("Courier", 30, "bold"))

