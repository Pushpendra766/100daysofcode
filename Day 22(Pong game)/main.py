from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

scoreboard = ScoreBoard()
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong game')
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
ball = Ball()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    screen.delay(100)
    ball.move_ball()

    # collision with walls
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # collision with paddle
    if (ball.xcor() >= 340 or ball.xcor() <= -340) and (ball.distance(l_paddle) < 50.99 or ball.distance(r_paddle) < 50.99):
        ball.bounce_x()

    # l paddle misses
    if ball.xcor() < -340:
        ball.reset()
        scoreboard.r_point()
        scoreboard.display_score()

    # r paddle misses
    if ball.xcor() > 340:
        ball.reset()
        scoreboard.l_point()
        scoreboard.display_score()


screen.exitonclick()

