from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.opponent_score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(-20, 270)

    def writeScore(self):
        self.clear()
        self.write(f"{self.score} | {self.opponent_score}", font=("Verdana", 15, "normal"))

    def add_opponent_score(self):
        self.opponent_score = self.opponent_score + 1

    def add_score(self):
        self.score = self.score + 1
