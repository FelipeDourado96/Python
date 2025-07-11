import pandas as pd
from turtle import Turtle, Screen

image = "brazil.gif"

screen = Screen()
screen.onscreenclick(print)
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)


screen.mainloop()