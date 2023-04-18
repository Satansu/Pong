from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.ymove *= -1

    def r_touch(self, paddle):
        if 340 < self.xcor() < 360 and self.distance(paddle) < 50:
            self.xmove *= -1

    def l_touch(self, paddle):
        if -340 > self.xcor() > -360 and self.distance(paddle) < 50:
            self.xmove *= -1

    def reset(self):
        self.goto(0, 0)
        self.xmove *= -1
        self.ymove *= -1
