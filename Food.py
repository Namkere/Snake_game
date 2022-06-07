import turtle
import random
from Snake import *
from Scoreboard import *
turtle.colormode(255)

TURTLE_SIZE = 20
WIDTH = 600
HEIGHT = 600

X_RANGE = (WIDTH - TURTLE_SIZE) / 2
Y_RANGE = (HEIGHT - TURTLE_SIZE) / 2

food = turtle.Turtle("circle")



# def get_color():
#     r = float(random.randint(1,255))
#     g = float(random.randint(1,255))
#     b = float(random.randint(1,255))
#     colours =  (r,g,b)
#     return colours

r = random.randint(1,255)
g = random.randint(1,255)
b = random.randint(1,255)

x = random.randint(int(-X_RANGE), int(X_RANGE))
y = random.randint(int(-Y_RANGE), int(Y_RANGE - 2 * TURTLE_SIZE))


def add_food():
    global r,g,b,x,y
    global food
    food.shapesize(stretch_len=0.5, stretch_wid=0.5)
    food.speed(0)
    food.penup()
    food.color(r,g,b)
    food.goto(x,y)


# function to eat the food

def eat_food():
    global food, x, y, r, g, b
    # check the distance between the head and the food
    if snakes[0].distance(food) < TURTLE_SIZE - 1:
        # move the food
        food.goto(x, y)
        # add a segment  to the snake
        add_segments()
        # change the food color
        food.color(r,g,b)
        # update score
        update_score(10)

