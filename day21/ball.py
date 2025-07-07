from turtle import Turtle
CONSTANT = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.setposition(0, 0)
        self.color("white")
        self.x_dir = 1
        self.y_dir = 1
        self.reverse = 1

    def move(self):
        new_x = self.xcor() + CONSTANT * self.x_dir * self.reverse
        new_y = self.ycor() + CONSTANT * self.y_dir * self.reverse
        self.setposition(new_x, new_y)

    def reset(self):
        self.goto(0,0)
        self.reverse *= -1