from turtle import Turtle

class Paddle:


    def __init__(self, x):
        self.paddle = []
        self.coorx = x
        self.coory = -20
        for i in range(0, 5):
            self.paddle.append(self.create_paddle())
            self.coory = self.coory + 20


    def create_paddle(self):
        paddle_section = Turtle()
        paddle_section.penup()
        paddle_section.shape("square")
        paddle_section.color("white")
        paddle_section.shapesize(1,1,1)
        paddle_section.goto(self.coorx, self.coory)
        paddle_section.setheading(90)
        return paddle_section

    def move_up(self):
        for paddle_section in self.paddle:
            paddle_section.forward(30)

    def move_down(self):
        for paddle_section in self.paddle:
            paddle_section.back(30)

    def detect_collision_wall(self):
        if self.paddle[4].ycor() > 295:
            self.move_down()
        if self.paddle[0].ycor() < -280:
            self.move_up()

    def detect_collision_ball(self, ball):
        for paddle_section  in self.paddle:
            if paddle_section.distance(ball.xcor(), ball.ycor()) < 20:
                return True

    def enemy_paddle_auto_move(self, ball):
        if self.paddle[4].ycor() < ball.ycor():
            self.move_up()
        elif self.paddle[0].ycor() > ball.ycor():
            self.move_down()


