from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'bold')
with open("high_score.txt", "r") as file:
    max_score = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = int(max_score)
        self.color("White")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.points}", align=ALIGNMENT, font=FONT)
        self.goto(0, 230)
        self.write(f"Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over. Final score: {self.points}", align=ALIGNMENT, font=FONT)
        if self.points > self.high_score:
            self.high_score = self.points
            with open("high_score.txt", "w") as high_score_file:
                high_score_file.write(str(self.high_score))
        self.points = 0
        self.goto(0, -50)
        self.write(f"Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)