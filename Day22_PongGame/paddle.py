from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, screen, x_pos, y_pos):
        super().__init__()
        self.status = None
        self.screen = screen
        self.screen.listen()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.setpos(x_pos, y_pos)
        self.up = False
        self.down = False

    def change_up(self):
        self.up = True

    def change_down(self):
        self.down = True

    def stop_moving_up(self):
        self.up = False

    def stop_moving_down(self):
        self.down = False

    def setup_key(self, up_key, down_key, move_type):
        self.status = move_type
        if move_type.lower() == "btn":
            self.screen.onkeypress(self.change_up, up_key)
            self.screen.onkeypress(self.change_down, down_key)
            self.screen.onkeyrelease(self.stop_moving_up, up_key)
            self.screen.onkeyrelease(self.stop_moving_down, down_key)
        else:
            self.screen.cv.bind("<Motion>", self.mouse_mode)

    def move(self):
        #Paddle exceeded height
        if self.ycor() >= 255:
            self.up = None
        elif self.ycor() <= -255:
            self.down = None
        if self.up:
            y = self.ycor() + 10
            self.goto(self.xcor(), y)
        if self.down:
            y = self.ycor() - 10
            self.goto(self.xcor(), y)
    def auto_moving(self, target):
        y = self.ycor()
        diff = target.ycor() - y
        if target.xcor() > -280:
            if diff > 30:
                self.sety(y + 5)
            if diff < -30:
                self.sety(y - 5)
            if diff > 200:
                self.sety(y + 40)
            if diff < -200:
                self.sety(y - 40)
    def mouse_mode(self, event):
        y = self.screen.window_height() // 2 - event.y  # Adjust coordinates
        self.sety(y)
