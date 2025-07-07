from turtle import Turtle
STARTING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.spd = 15

    def move_up(self):
        new_position = self.ycor() + self.spd
        self.goto(0, new_position)

    def move_down(self):
        new_position = self.ycor() - self.spd
        self.goto(0, new_position)

    def spd_up(self):
        self.spd += 5
    def spd_down(self):
        self.spd -= 5