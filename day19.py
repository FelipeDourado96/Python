from turtle import Turtle, Screen
from random import randint

screen = Screen()

############################# Turtle colors#################################################
turtle_colors = ["green", "purple", "red", "yellow", "blue", "black", "pink"]
all_turtles = []
winner_turtle = ""
y_position = [-300, -200, -100, 0, 100, 200, 300]
for color in range(0, 7):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[color])
    new_turtle.setposition(-450, y_position[color])
    all_turtles.append(new_turtle)
##################################################################################################

end_race = False

def bet():
    user_bet = screen.textinput("Turtle Race", "Which Turtle is going to win the race?")
    return user_bet
user_bet = bet()

while not end_race:
    for turtle in all_turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 450:
            end_race = True
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print("You've won!")
            else:
                print(f"You lost, the winner was {winner_turtle}")

screen.listen()
screen.exitonclick()