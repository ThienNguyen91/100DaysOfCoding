from time import sleep
from turtle import Turtle
from defaultTurtle import setup
move_distance = 20
square_block_list = []
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.length = 3
        self.create_snake()
        self.head = square_block_list[0]
        self.speed = 0.1

    def create_snake(self):
        for i in range(0, 3):
            x = Turtle()
            self.fill_square_color(x)
            x.goto(square_block_list[i].xcor()-20 * i, square_block_list[i].ycor())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go(self, screen, food, score):
        while True:
            for i in range(len(square_block_list) - 1, 0, -1):
                new_x = square_block_list[i - 1].xcor()
                new_y = square_block_list[i - 1].ycor()
                square_block_list[i].goto(new_x, new_y)
            self.head.forward(move_distance)
            #Detect collision with food
            if self.head.distance(food) < 15:
                self.resize_snake_add_score(score)
                self.speed -= 0.005
                food.new_location()
            #Detect collision with wall
            if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
                score.game_over()
                break
            #Detect collision with tail
            game_over_flag = False
            for segment in square_block_list[1:]:
                if self.head.distance(segment) < 10:
                    game_over_flag = True
                    break
            if game_over_flag:
                score.game_over()
                break
            #update frame
            screen.update()
            sleep(self.speed)
    def resize_snake_add_score(self, score):
        score.increase_score()
        self.length += 1
        for i in range(0, 1):
            x = Turtle()
            self.fill_square_color(x)
            x.goto(square_block_list[-1].position())
    def fill_square_color(self, square_block):
        self.is_not_used()
        setup(square_block, "square", "white")
        square_block.fillcolor("white")
        square_block_list.append(square_block)
    def is_not_used(self):
        pass