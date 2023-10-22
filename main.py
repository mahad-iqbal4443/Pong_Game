from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time as t
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(370)
l_paddle = Paddle(-380)
ball = Ball()
score = Score()
game_is_on = True


def screen_fun():
    screen.update()
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")


while game_is_on:
    t.sleep(ball.move)
    screen_fun()
    ball.change_position()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
    if ball.distance(r_paddle) > 50 and ball.xcor() > 400:
        score.increase_l_score()
        ball.reset_position()
    if ball.distance(l_paddle) > 50 and ball.xcor() < -400:
        score.increase_r_score()
        ball.reset_position()


screen.exitonclick()
