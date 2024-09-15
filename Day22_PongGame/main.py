from time import sleep
from turtle import Screen, textinput
from paddle import Paddle
from ball import Ball
from score_board import Score



#screen setup
my_screen = Screen()
my_screen.title("Pong Game")
my_screen.setup(width=800, height=600)
my_screen.bgcolor("Black")
my_screen.tracer(0)

#Gameplay setup
game_mode = textinput("GameMode", "Player Or Computer")
move_type = textinput("Movement", "Button Or Mouse")
paddle1 = Paddle(my_screen, -350, 0)
paddle2 = Paddle(my_screen, 350, 0)
my_ball = Ball(0, 0)
game_score = Score()

def player_mode():
    if paddle1.status == "btn":
        while True:
            paddle1.move()
            paddle2.move()
            my_ball.start_moving(paddle1, paddle2, game_score)
            frame_update(my_screen, 80)
    else:
        while True:
            paddle2.move()
            my_ball.start_moving(paddle1, paddle2, game_score)
            frame_update(my_screen, 80)
def computer_mode():
    if paddle1.status == "btn":
        while True:
            paddle1.move()
            paddle2.auto_moving(my_ball)
            my_ball.start_moving(paddle1, paddle2, game_score)
            frame_update(my_screen, 80)
    else:
        while True:
            paddle2.auto_moving(my_ball)
            my_ball.start_moving(paddle1, paddle2, game_score)
            frame_update(my_screen, 80)
def frame_update(screen, speed):
    screen.update()
    sleep(1/speed)

#r_paddle setup
if game_mode == "player":
    paddle2.setup_key("Up", "Down", "btn")
#l_paddle setup
if move_type.lower() == "button":
    paddle1.setup_key("w", "s", "btn")
else:
    paddle1.setup_key(None, None, "mouse")

#Game_Mode choose
if game_mode == "player":
    player_mode()
else:
    computer_mode()







