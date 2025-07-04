import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

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
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)






















screen.exitonclick()