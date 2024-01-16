from turtle import Turtle 

class scorebod(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.p1 = 0
        self.p2 = 0
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.p1, align= "center", font= ("Courier", 50, "normal"))
        self.goto(100, 150)
        self.write(self.p2, align= "center", font= ("Courier", 50, "normal"))

    def score1(self):
        self.p1 += 1

    def score2(self):
        self.p2 += 1

    def winner(self):
        if self.p1 == 10:
            self.goto(-200, 50)
            self.write("P1 WINS", align= "center", font= ("Courier", 50, "normal"))
        if self.p2 == 10:
            self.goto(200, 50)
            self.write("P2 WINS", align= "center", font= ("Courier", 50, "normal"))