from turtle import Turtle, Screen
#requirement random color, from 3-sided shape to 10-sided shape, increase 100 each shape
from random import randint
screen = Screen()

screen.colormode(255)
Tommy = Turtle()
direction = [0, 90, 180, 270]
def change_color(Turtle):
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    Turtle.pencolor((r, g, b))
def change_thickness(Turtle, size):
    Turtle.width(size)
def random_direction(Turtle):
    Turtle.setheading(direction[randint(0, 3)])

change_thickness(Tommy, 10)
Tommy.speed(0)
for i in range(200):
    change_color(Tommy)
    random_direction(Tommy)
    Tommy.forward(50)






















Tommy.shape("turtle")
screen.exitonclick()