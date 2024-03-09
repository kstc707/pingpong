from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, X1, Y1):
        self.X1 = X1
        self.Y1 = Y1
        super().__init__()
        self.tut = Turtle()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(X1, Y1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
