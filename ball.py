from turtle import Turtle
import random as rand

class Ball(Turtle):

    collision = 1
    collision_paddle = 1
    move_speed = 1
    move_rate = 10

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        new_x = self.xcor() - (self.move_rate*self.collision_paddle)
        new_y = self.ycor() + (self.move_rate*self.collision)
        self.speed(self.move_speed)
        self.goto(new_x, new_y)

    def detect_collision_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.collision = self.collision * -1

    def hit_paddle(self):
        self.collision_paddle = self.collision_paddle * -1
        self.move_speed = self.move_speed + 1
        self.move_rate = self.move_rate + 2


    def reset_position(self):
        self.goto(0,0)

    def out_of_bound(self):
        if self.xcor()>400:
            self.collision_paddle = self.collision_paddle * -1
            return 1
        elif self.xcor()<-400:
            self.collision_paddle = self.collision_paddle * -1
            return 0
