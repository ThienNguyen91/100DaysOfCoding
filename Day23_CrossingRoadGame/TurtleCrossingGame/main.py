import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_is_on = True
player = Player()
screen.onkeypress(player.go_up, "w")
screen.onkeypress(player.go_up, "Up")
car_list = []
player_score = Scoreboard()
spawn_delay = 0.6
last_spawn_time = time.time()

while game_is_on:
    #Player life
    if player.live == 0:
        player_score.game_over()
        game_is_on = False
        break
    #Car spawn time
    current_time = time.time()
    if float(current_time - last_spawn_time) > spawn_delay:
        car_list.append(CarManager())
        last_spawn_time = current_time
    #Move car
    for car in car_list:
        car.move(player_score.score)
        if player.distance(car) < 25.0:
            player.default_position()
            player.decrease_player_live()

    if player.ycor() > 280.0:
        player.default_position()
        # increase score
        player_score.increase_score()
        spawn_delay -= 0.3


    time.sleep(0.1)
    screen.update()


screen.exitonclick()