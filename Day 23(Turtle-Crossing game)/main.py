import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
game_is_on = True
screen.listen()
screen.onkeypress(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_forward()

    # detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) <= 25:
            game_is_on = False
            scoreboard.game_over()
    # turtle reached the other side
    if player.ycor() >= 280:
        scoreboard.update_score()
        player.level_up()
        car_manager.level_up()

screen.exitonclick()

