import time
from turtle import Screen
from player import Player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_is_on = True
player = Player()
player.shape("square")
player.shapesize(stretch_wid=3, stretch_len=2, outline=1)

while game_is_on:
    time.sleep(0.1)
    screen.update()
