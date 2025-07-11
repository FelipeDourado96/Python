import pandas as pd
from turtle import Turtle, Screen

image = "brazil.gif"

screen = Screen()
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

states_name = Turtle()
states_name.hideturtle()
states_name.penup()

dataset = pd.read_csv("brazil_states.csv")

states = dataset["state"]
x_cor = dataset["x"]
y_cor = dataset["y"]
states_list = []

while len(states_list) < 26:
    user_answer = screen.textinput(title=f"{len(states_list)}/26 States Correct", prompt="What's another state's name?").title()
    if user_answer == "Exit":
        break
    for state in states:
        if user_answer == state and user_answer not in states_list:
            states_list.append(state)
            x = x_cor[states == state].item()
            y = y_cor[states == state].item()
            states_name.goto(x, y)
            states_name.write(state)

missing_states = [state for state in states if state not in states_list]

remaining_states = pd.DataFrame(missing_states)
remaining_states.to_csv("remaining states.csv")