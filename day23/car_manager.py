from turtle import Turtle
from random import randint

CAR_COLORS = ["red", "pink", "yellow", "blue", "green", "orange", "grey"]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = 10

    def generate_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(CAR_COLORS[randint(0,6)])
        new_car.setposition(300, randint(-220, 230))
        self.cars.append(new_car)

    def move_car(self):
        for i in self.cars:
            i.backward(self.car_speed)