import time
from turtle import Turtle, Screen
from snake import Snake()

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()

segments = []
xcoor = 0

for turtle in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    segments.append(new_segment)
    new_segment.penup()
    new_segment.setposition(xcoor, 0)
    xcoor -= 20

screen.tracer(0)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)

    snake.move()





















screen.exitonclick()