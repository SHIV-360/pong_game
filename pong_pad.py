from turtle import Turtle

class pong(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.setheading(90)
        self.shapesize(stretch_len=3, stretch_wid=0.25)
        self.penup()
        self.goto(position)
        
    def up(self):
        self.setheading(90)
        self.forward(40)

    def down(self):
        self.setheading(270)
        self.forward(40)


