from turtle import Turtle
from Snake import *

TURTLE_SIZE = 20
WIDTH = 600
HEIGHT = 600
scoreboard = Turtle()
score = 0
with open("high_score.txt") as file:
    high_score = int(file.read())

FONT = ('Arial', 16, 'normal')

X_RANGE = (WIDTH - TURTLE_SIZE) / 2
Y_RANGE = (HEIGHT - TURTLE_SIZE) / 2

def create_scoreboard():
    global scoreboard
    scoreboard.color("cyan")
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.goto(-5, Y_RANGE -2*TURTLE_SIZE)
    update_score(0)


def update_score(score_increment, is_reset=False):
    global score, high_score, scoreboard

    if is_reset:
        score = 0
    else:
        score += score_increment

    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as file:
            file.write(f"{high_score}")

    scoreboard.clear()

    scoreboard.write(f"Score : {score}  |  High Score :{high_score}", align= 'center', font = FONT)

def reset():
    # hide the segments of snake

    for t in snakes:
        t.goto(40000, 4000)

    # clear the snake
    snakes.clear()

    # create a new head
    create_head(is_initial=False)

    # reset the score
    update_score(0, is_reset=True)






