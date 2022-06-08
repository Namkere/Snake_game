import turtle
import random
from Snake import *
from Scoreboard import *


TURTLE_SIZE = 20
WIDTH = 600
HEIGHT = 600
colours =["blue", "red", "cyan", "magenta", "white", "pink", "brown", "green"]
colour = random.choice(colours)

X_RANGE = (WIDTH - TURTLE_SIZE) / 2
Y_RANGE = (HEIGHT - TURTLE_SIZE) / 2

food = turtle.Turtle("circle")



x = random.randint(int(-X_RANGE+TURTLE_SIZE), int(X_RANGE-TURTLE_SIZE))
y = random.randint(int(-Y_RANGE + TURTLE_SIZE), int(Y_RANGE - 2 * TURTLE_SIZE))


def add_food():
    global colour, x, y
    global food
    food.shapesize(stretch_len=0.5, stretch_wid=0.5)
    food.speed(0)
    food.penup()
    food.color(colour)
    food.goto(x,y)




