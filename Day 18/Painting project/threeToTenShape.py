from turtle import Turtle, Screen
#requirement random color, from 3-sided shape to 10-sided shape, increase 100 each shape
from random import randint
screen = Screen()

screen.colormode(255)
def change_color(Turtle):
    R = randint(0, 255)
    B = randint(0, 255)
    G = randint(0, 255)

    Turtle.pencolor(R, G, B)


Tommy = Turtle()
for i in range(3, 11): #from 3 to 10
    length = 100
    change_color(Tommy)
    for x in range(i):
        Tommy.right(360/i)
        Tommy.forward(length)
    length += 100





















Tommy.shape("turtle")
screen.exitonclick()