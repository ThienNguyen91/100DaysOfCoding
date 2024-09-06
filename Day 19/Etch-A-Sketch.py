from turtle import Turtle, Screen, colormode, onkey

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def reset():
    tim.reset()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(reset, "c")

screen.exitonclick()