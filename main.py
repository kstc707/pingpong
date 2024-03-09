from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800,600)

r_pad=Paddle(350,0)
l_pad=Paddle(X1=-350,Y1=0)

screen.listen()
screen.onkey(r_pad.go_up,"Up")
screen.onkey(r_pad.go_down,"Down")
screen.onkey(l_pad.go_up,"w")
screen.onkey(l_pad.go_down,"s")

pong=Ball()
score_board=Scoreboard()


not_over=True
while not_over:
    time.sleep(pong.sp)
    screen.update()
    pong.move()
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()
    if pong.distance(r_pad) < 50 and pong.xcor() > 320 or pong.distance(l_pad) < 50 and pong.xcor() < -320 :
        pong.bounce_x()
        pong.speed(pong.sp+5)
    if pong.xcor() > 380:
        pong.reset_position()
        score_board.l_point()
    if pong.xcor() < -380:
        pong.reset_position()
        score_board.r_point()

screen.exitonclick()

