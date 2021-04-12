from turtle import Turtle
FONT = ("Courier", 15, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.penup()
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER !", align="center", font=("Arial", 30, "bold"))

