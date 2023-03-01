from turtle import Turtle

FONT = ("Lucida Handwriting", 15, "bold")


class Scoreboard(Turtle):

    score = 1

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """Updates the number of eggs user put inside the basket"""
        self.clear()
        self.setposition(0, 270)
        self.write(f"Thy Eggs: {self.score}", False, "center", FONT)

    def inc_score(self):
        """Increases the egg counter"""
        self.score += 1
        self.update_score()

    def dec_score(self):
        """Decreases the egg counter"""
        self.score -= 1
        self.update_score()
