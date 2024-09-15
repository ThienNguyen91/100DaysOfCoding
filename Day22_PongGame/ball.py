from time import sleep
from turtle import Turtle

class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(x_pos, y_pos)
        self.x_move = 3
        self.y_move = 2.7
    def start_moving(self, l_paddle, r_paddle, score_board):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        #detect wall
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()
        #detect paddle
        if self.xcor() > 330 and self.distance(r_paddle) < 50 or self.xcor() < -335 and self.distance(l_paddle) < 50:
            self.bounce_x()
        #detect when out of bounds
        if self.xcor() > 380:
            score_board.increase_l()
            self.reset_position(1)
        elif self.xcor() < -380:
            score_board.increase_r()
            self.reset_position(-1)


    def reset_position(self, multiply_num):
        self.goto(0, 0)
        self.x_move = 3 * multiply_num
        self.y_move = 2.7 * multiply_num
        self.bounce_y()
        self.bounce_x()
    def bounce_y(self):
        self.y_move *= -1.1
    def bounce_x(self):
        self.x_move *= -1.1
