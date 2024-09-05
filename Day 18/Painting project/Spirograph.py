from random import randint
from turtle import Screen, Turtle, colormode
colormode(255)

def change_color(Turtle):
    R = randint(0, 255)
    B = randint(0, 255)
    G = randint(0, 255)

    Turtle.pencolor(R, G, B)
size_of_gap = int(input("How many gap?: "))
Tom = Turtle()
Tom.speed(0)
print("Circle running")
for x in range(int(360/size_of_gap)):
    change_color(Tom)
    Tom.circle(100)
    Tom.setheading(Tom.heading() +size_of_gap)










screen = Screen()
screen.exitonclick()













