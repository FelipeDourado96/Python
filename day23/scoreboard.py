from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=("Courier", 40, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Final Score {self.level}", align="center", font=("Courier", 40, "bold"))
