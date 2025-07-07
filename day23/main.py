import time
from turtle import Screen
from car_manager import CarManager
from player import Player, STARTING_POSITION
from scoreboard import Scoreboard

# Screen Config
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

# Objects
    # Cars
car = CarManager()
    # Player
player = Player()
    # Scoreboard
scoreboard = Scoreboard()

# Commands
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.spd_up, "w")
screen.onkey(player.spd_down, "r")

game_is_on = True
counter = 0

for i in range(3):
    car.generate_car()

while game_is_on:
    counter += 1
    if counter >= 10:
        car.generate_car()
        counter = 0
    car.move_car()
    screen.update()
    time.sleep(0.1)
    if player.ycor() >= 280:
        scoreboard.level_up()
        player.goto(STARTING_POSITION)
        car.car_speed += 2
    for each_car in car.cars:
        if -25 < each_car.xcor() - player.xcor() < 25:
            if -25 < each_car.ycor() - player.ycor() < 25:
                scoreboard.game_over()
                game_is_on = False



screen.exitonclick()