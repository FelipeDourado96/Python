from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.turtlesize(5, 1)
        self.setposition(position)

    # Commands
    def up(self):
        self.setposition(self.xcor(), self.ycor() + 70)
    def down(self):
        self.setposition(self.xcor(), self.ycor() - 70)
