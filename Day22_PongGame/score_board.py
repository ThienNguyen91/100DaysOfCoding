from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.l_score = 0
        self. r_score = 0

        self.write_score()
    def increase_r(self):
        self.r_score += 1
        self.write_score()
    def increase_l(self):
        self.l_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))