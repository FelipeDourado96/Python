from turtle import Turtle, Screen
from random import randint, choice

t = Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()
x_pos = -250
y_pos = -200
t.setposition(x_pos, y_pos)
screen = Screen()
screen.colormode(255)
color = [(206, 162, 130), (239, 206, 171), (102, 93, 83), (28, 23, 20), (147, 154, 166), (14, 15, 21), (102, 110, 125), (207, 213, 234), (227, 188, 151), (20, 16, 17), (165, 114, 99), (172, 186, 225), (218, 210, 214), (71, 65, 53), (120, 124, 143)]

def hirst_painting():
    current_floor = 0
    for floors in range(10):
        dots = 1
        for dot in range(10):
            # i = randint(0, len(color) - 1)
            # random_color = color[i]
            t.dot(30, choice(color))
            dots += 1
            if dots <= 10:
                t.forward(50)
        current_floor += 1
        t.teleport(x_pos, y_pos + current_floor*50)

hirst_painting()


screen.exitonclick()