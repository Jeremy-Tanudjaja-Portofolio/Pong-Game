from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

game_is_on = True


screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.tracer(0)

player_paddle = Paddle(x = -360)
enemy_paddle = Paddle(x = 360)
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(key = "Up", fun = player_paddle.move_up)
screen.onkeypress(key = "Down", fun = player_paddle.move_down)

# screen.onkey(key = "w", fun = enemy_paddle.move_up)
# screen.onkey(key = "s", fun = enemy_paddle.move_down)

while game_is_on:
    scoreboard.writeScore()
    time.sleep(0.1)
    ball.move()
    ball.detect_collision_wall()
    player_paddle.detect_collision_wall()
    enemy_paddle.enemy_paddle_auto_move(ball)
    if player_paddle.detect_collision_ball(ball) or enemy_paddle.detect_collision_ball(ball):
        ball.hit_paddle()
    if ball.out_of_bound() == 1:
        scoreboard.add_score()
        scoreboard.writeScore()
        ball.reset_position()
    elif ball.out_of_bound()== 0:
        scoreboard.add_opponent_score()
        scoreboard.writeScore()
        ball.reset_position()
    screen.update()





screen.exitonclick()
