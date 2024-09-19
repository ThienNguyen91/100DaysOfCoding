from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.my_turtle = Turtle()
        self.live = 4
        self.decrease_player_live()
        self.shape("turtle")
        self.penup()
        self.default_position()
        self.setheading(90)
    def go_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
    def default_position(self):
        self.goto(STARTING_POSITION)
    def decrease_player_live(self):
        self.my_turtle.clear()
        self.my_turtle.hideturtle()
        self.my_turtle.penup()
        self.my_turtle.goto(180, 250)
        self.my_turtle.pendown()
        self.live -= 1
        self.my_turtle.write(f"LIFE:{self.live}", True, "left", FONT)