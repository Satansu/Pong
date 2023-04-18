import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

game = True
while game:
    time.sleep(0.175)
    screen.update()
    ball.move()
    ball.bounce()
    ball.r_touch(r_paddle)
    ball.l_touch(l_paddle)
    ball.move()

    if ball.xcor() < -360:
        ball.reset()
        scoreboard.r_update()
    if ball.xcor() > 360:
        ball.reset()
        scoreboard.l_update()

screen.exitonclick()