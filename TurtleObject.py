from turtle import Turtle


class TurtleObject(Turtle):
    def __init__(self):
        super().__init__()
        self.left(90)
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setposition(x=0, y=-250)
        self.new_y = 0

    def move_straight(self):
        if self.ycor() < 250:
            self.new_y = self.ycor() + 30
            self.goto(self.xcor(), self.new_y)

    def isFinished(self):
        return self.ycor() >= 260

    def reset_position(self):
        return self.goto(0, -250)
