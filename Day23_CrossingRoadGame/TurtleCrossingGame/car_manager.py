from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2, outline=1)
        self.pencolor(choice(COLORS))
        new_y = randint(-250, 280)
        new_x = randint(300, 310)
        self.goto(new_x, new_y)
    def move(self, score):
        speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * score
        self.setx(self.xcor() - speed)
        if self.ycor() <-300:
            self.clear()


