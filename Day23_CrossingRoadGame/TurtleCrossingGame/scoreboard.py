from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.pendown()
        self.write(f"Level:{self.score}", True, "left", FONT)
    def increase_score(self):
        self.clear()
        self.goto(-280, 250)
        self.score += 1
        self.write(f"Level:{self.score}", True, "left", FONT)
    def game_over(self):
        self.penup()
        self.goto(-80, 0)
        self.write(f"Game Over.", True, "left", FONT)
