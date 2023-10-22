from turtle import Turtle
from speed import Speed
s = Speed()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.goto(0, 0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move = s.level()

    def change_position(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move = s.level()
