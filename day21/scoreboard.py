from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_points = 0
        self.l_points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_points, align="center", font=('Courier', 50, 'normal'))
        self.goto(100, 200)
        self.write(self.r_points, align="center", font=('Courier', 50, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Final Score:", align="center", font=('Courier', 50, 'normal'))
        self.goto(0, 130)
        self.write(f"{self.l_points}x{self.r_points}", align="center", font=('Courier', 50, 'normal'))