from turtle import Turtle
from defaultTurtle import setup
class Score(Turtle):
    def __init__(self, score):
        super().__init__()
        self.goto(0,250)
        setup(self, "classic", "white")
        self.hideturtle()
        self.score = score
        self.write_score()
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.write_score()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=("Arial", 20, "normal"))