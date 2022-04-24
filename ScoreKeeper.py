from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-345, 275)
        self.write(f"Level: {self.score}", align="center", font=("Courier", 15, "bold"))

    def point_score(self):
        self.score += 1
        self.update_score()

    def Game_Over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("arial", 50, "bold"))

    def Won(self):
        self.goto(0, 0)
        self.write("You Won!\nCongratulations!😊", align="center", font=("arial", 50, "bold"))
