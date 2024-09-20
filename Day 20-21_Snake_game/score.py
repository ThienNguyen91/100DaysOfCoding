from turtle import Turtle
from defaultTurtle import setup




class Score(Turtle):
    def __init__(self, score):
        super().__init__()
        self.goto(0,250)
        setup(self, "classic", "white")
        self.hideturtle()
        self.score = score
        with open("highest_score.txt", "r") as file:
            self.highest_score = int(file.read())
        self.write_score()
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.write_score()
    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.write_score()
