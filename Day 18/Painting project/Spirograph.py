from random import randint
from turtle import Screen, Turtle



def change_color(Turtle):
    R = randint(0, 255)
    B = randint(0, 255)
    G = randint(0, 255)

    Turtle.pencolor(R, G, B)
angle = 0
Tom = Turtle()
Tom.speed(0)
print("Circle running")
while angle != 360:
    angle += 5
    change_color(Tom)
    Tom.circle(100)
    Tom.left(angle)











screen.colormode(255)
screen.exitonclick()













