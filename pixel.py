from turtle import Turtle
from random import uniform

SPEED = 5


class Pixel(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.setposition(0, -280)
        self.x_go = uniform(0.1, 0.9)
        self.y_go = uniform(0.1, 0.9)
        self.new_speed = 1
        self.speed(self.new_speed)

    def reset_state(self):
        self.goto(0, -280)
        self.new_speed = 1

    def move(self):
        x = self.xcor() + SPEED * self.x_go
        y = self.ycor() + SPEED * self.y_go
        self.goto(x, y)

    def y_bounce(self):
        self.y_go *= -1
        self.new_speed *= 0.09

    def x_bounce(self):
        self.x_go *= -1
        self.new_speed *= 0.09
