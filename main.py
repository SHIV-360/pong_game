from turtle import Screen 
from turtle import Turtle
from Ball import ball
from pong_pad import pong
import time
from scoreboard import scorebod
import time

screen = Screen()
screen.setup(width=850, height=500)
screen.bgcolor("LIGHTGREEN")
screen.title("PONG PAD GAME")
screen.tracer(0)
line = Turtle()
line.penup()
line.goto(0,250)
line.width(10)
line.setheading(270)
for _ in range(0, 11):
        line.pendown()
        line.forward(25)
        line.penup()
        line.forward(25)


pong1 = pong((-400, 0))
pong2 = pong((400, 0))
ball = ball()
scoreboard = scorebod()

screen.listen()
screen.onkey(pong1.up, "w")
screen.onkey(pong1.down, "s")
screen.onkey(pong2.up, "Up")
screen.onkey(pong2.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() >= 240 or ball.ycor() <= -240:
        ball.bounce_wall()
    if ball.xcor() >= 425:
        ball.refresh()
        scoreboard.score1()
        scoreboard.update_score()
    if ball.xcor() <= -425:
        ball.refresh()
        scoreboard.score2()
        scoreboard.update_score()

    if ball.distance(pong1) <= 50 and ball.xcor() <= -378:
        ball.bounce_pad()
    if ball.distance(pong2) <= 50 and ball.xcor() >= 378:
        ball.bounce_pad()

    if scoreboard.p1 == 10 or scoreboard.p2 == 10:
        scoreboard.winner()
        game_is_on = False


screen.exitonclick()
