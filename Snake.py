from turtle import Turtle
TURTLE_SIZE = 20
snakes = []
head = None
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def create_head(is_initial = True):
    global head, snakes
    head = Turtle("triangle")
    head.color("magenta")
    head.speed(0)
    head.penup()
    if is_initial:
        head.goto(0, 200)
    snakes.append(head)



def go_up():
    global snakes

    if snakes[0].heading() != DOWN:
        snakes[0].setheading(UP)


def go_down():
    global snakes

    if snakes[0].heading() != UP:
        snakes[0].setheading(DOWN)


def go_right():
    global snakes

    if snakes[0].heading() != LEFT:
        snakes[0].setheading(RIGHT)


def go_left():
    global snakes

    if snakes[0].heading() != RIGHT:
        snakes[0].setheading(LEFT)
def add_segments():
    global snakes
    x, y = get_last_segment_position()
    segment = Turtle("square")
    segment.color("magenta")
    segment.speed(0)
    segment.penup()
    segment.goto(x, y)
    snakes.append(segment)

def get_last_segment_position():
    global snakes
    last_segment = snakes[-1]

    x_position = last_segment.xcor()
    y_position = last_segment.ycor()

    if snakes[0].heading() == UP:
         y_position -= TURTLE_SIZE

    # if direction is up -> same x, y is TURTLE_SIZE more
    elif snakes[0].heading() == DOWN:
        y_position += TURTLE_SIZE

    # if direction is right -> same y, x is TURTLE_SIZE less
    elif snakes[0].heading() == RIGHT:
        x_position -= TURTLE_SIZE

    # if direction is left -> same y, x is TURTLE_SIZE more
    elif snakes[0].heading() == LEFT:
        x_position += TURTLE_SIZE

    return (x_position, y_position)


def move():
    for i in range(len(snakes) - 1, 0, -1):
        x = snakes[i - 1].xcor()
        y = snakes[i - 1].ycor()
        snakes[i].goto(x, y)
    snakes[0].forward(TURTLE_SIZE)


