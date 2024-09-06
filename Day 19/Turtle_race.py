from turtle import Turtle, Screen, colormode, onkey, textinput
from random import randint
screen = Screen()
screen.setup(500, 400)
player_turtle = textinput("Make your bet", "Who will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

def setup(name_color, x, y):
    name = Turtle(shape = "turtle")
    name.pencolor(name_color)
    name.penup()
    name.goto(x, y)
    turtle_list.append(name)

x_default = -230
y_default = -100
count = 0
for color in colors:
    setup(color, x_default, y_default + 40*count)
    count += 1

#Start racing
def start(player_bet):
    if player_bet:
        while True:
            for eachTurtle in turtle_list:
                eachTurtle.forward(randint(0, 10))
                if eachTurtle.xcor() > 250:
                    return eachTurtle

winner = start(player_turtle)
if player_turtle.lower() == winner.pencolor():
    print(f"You've won! The {player_turtle} turtle is the winner!")
else:
    print(f"You've lost! The {winner.pencolor()} turtle is the winner!")






screen.exitonclick()
