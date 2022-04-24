from turtle import Turtle
import random
COLORS = ["yellow", "black", "blue", "red", "brown", "pink", "orange", "cyan"]
CONST_MOVE_INCREAMENT = 10


class RandomObjects:

    def __init__(self):
        self.objects = []

    def Factory(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            ob_1 = Turtle("square")
            ob_1.shapesize(stretch_wid=1, stretch_len=2)
            ob_1.penup()
            ob_1.color(random.choice(COLORS))
            random_y = random.randrange(-220, 240, 60)
            ob_1.goto(400, random_y)
            self.objects.append(ob_1)

    def Motion(self):
        for ob_1 in self.objects:
            ob_1.backward(CONST_MOVE_INCREAMENT)
