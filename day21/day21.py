import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

initial_speed = 0.05
max_score = 5

# Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

# Paddle, Ball and Score object
scoreboard = Scoreboard()
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
ball_speed = initial_speed

# Commands
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Loop game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.y_dir *= -1
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50 or ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.x_dir *= -1
        ball_speed -= 0.001
    elif ball.xcor() > 420 and ball.distance(r_paddle) > 50:
        scoreboard.l_points += 1
        scoreboard.refresh_scoreboard()
        ball_speed = initial_speed
        ball.reset()
        if scoreboard.l_points >= max_score:
            scoreboard.game_over()
            game_is_on = False
    elif ball.xcor() < -420 and ball.distance(l_paddle) > 50:
        scoreboard.r_points += 1
        scoreboard.refresh_scoreboard()
        ball_speed = initial_speed
        ball.reset()
        if scoreboard.r_points >= max_score:
            scoreboard.game_over()
            game_is_on = False











screen.exitonclick()