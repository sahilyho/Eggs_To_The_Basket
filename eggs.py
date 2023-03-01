from turtle import Turtle
from random import randint, choice

color_choice = ["white", "yellow", "red"]
FONT = ("Lucida Sans", 15, "bold")


class Eggs(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=1.5)
        self.setposition(randint(-100, 100), randint(-200, 200))
        self.setheading(90)
        self.new_color = [choice(color_choice)]
        self.color(self.new_color)
        self.drag_egg(self.xcor(), self.ycor())

    def drag_egg(self, x, y):
        """Input the xcor() and ycor() value of SELF. Ex. x= turtle.xcor(), y=turtle.ycor()"""
        self.ondrag(None)
        self.goto(x, y)
        self.ondrag(self.drag_egg)

    def change_on_collision(self, distance_object):
        """Input the object that will collide with SELF. Each collision will change the color of SELF."""
        if self.distance(distance_object) < 5:
            if "white" in self.new_color:
                self.new_color.remove("white")
                self.new_color.append("yellow")
            elif "yellow" in self.new_color:
                self.new_color.remove("yellow")
                self.new_color.append("red")
                # the dots give user clues about the state of its eggs.
                # Ex. if dot is red and egg is yellow, the next collision will result in game over.
                self.write(".", False, "left", FONT)
            elif "red" in self.new_color:
                self.new_color.remove("red")
                self.new_color.append("white")
                self.write(".", False, "left", FONT)
            self.color(self.new_color)
