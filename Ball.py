from turtle import Turtle
import random

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_dir = 10
        self.y_dir = 10

    def move(self):
        new_x = self.xcor() + self.x_dir
        new_y = self.ycor() + self.y_dir
        self.goto(new_x, new_y)

    def refresh(self):
        self.goto(0,0)
        self.x_dir = random.choice([10, -10]) 
        self.y_dir = random.choice([10, -10])

    def bounce_wall(self):
        self.y_dir *= -1

    def bounce_pad(self):
        self.x_dir *= -1.15

