from random import randint
from turtle import Turtle
from defaultTurtle import setup
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        setup(self, "circle", "blue")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.fillcolor("blue")
        self.new_location()
    def new_location(self):
        x_cor = randint(-280, 280)
        y_cor = randint(-280, 280)
        self.goto(x_cor, y_cor)