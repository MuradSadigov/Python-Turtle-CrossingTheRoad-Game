from turtle import Screen
from TurtleObject import *
from RandomObjects import *
from ScoreKeeper import *
import time

# -----------Screen_Setup---------
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Cross the Road")
screen.tracer(0)

# ----------Player-------
player = TurtleObject()

# ----------Barrier------
Rand_Objects = RandomObjects()
# ----------Score--------
points = Score()

# ----------Key----------
screen.listen()
screen.onkey(player.move_straight, "Up")

# ------------------------------MAIN---------------------------
game_is_On = True

while game_is_On:
    time.sleep(0.01)
    screen.update()

    Rand_Objects.Factory()
    Rand_Objects.Motion()

    for car in Rand_Objects.objects:
        if car.distance(player) < 25:
            game_is_On = False
            screen.clear()
            points.Game_Over()

    if player.isFinished():
        points.point_score()
        player.reset_position()

    if points.score == 5:
        screen.clear()
        points.Won()
        game_is_On = False

screen.exitonclick()
