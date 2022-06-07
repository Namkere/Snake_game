import time
import turtle
from turtle import Screen
from Food import *
from Snake import*
from Scoreboard import *

X_RANGE = (WIDTH - TURTLE_SIZE) / 2
Y_RANGE = (HEIGHT - TURTLE_SIZE) / 2
r = random.randint(1,255)
g = random.randint(1,255)
b = random.randint(1,255)

x = random.randint(int(-X_RANGE + 2*TURTLE_SIZE), int(X_RANGE- 2*TURTLE_SIZE))
y = random.randint(int(-Y_RANGE + 2*TURTLE_SIZE), int(Y_RANGE - 2 * TURTLE_SIZE))

TURTLE_SIZE = 20
WIDTH = 600
HEIGHT = 600
duration = 0.1


window = Screen()
window.title('Hands-On Snake')
window.bgcolor('black')
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)


create_head(is_initial = True)
create_scoreboard()
add_food()

window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')

game_is_on = True
while game_is_on:


    window.update()
    time.sleep(duration)
    x = random.randint(int(-X_RANGE + 2 * TURTLE_SIZE), int(X_RANGE - 2 * TURTLE_SIZE))
    y = random.randint(int(-Y_RANGE + 2 * TURTLE_SIZE), int(Y_RANGE - 2 * TURTLE_SIZE))
    move()

    if snakes[0].distance(food) < TURTLE_SIZE - 4:
        food.goto(x, y)
        add_segments()
        food.color(r, g, b)
        update_score(10)

    #to check if the game is over:


    # check border collision

    if snakes[0].xcor() <= -X_RANGE or snakes[0].xcor() >= X_RANGE or snakes[0].ycor() <= -Y_RANGE or snakes[0].ycor() \
            >= Y_RANGE:

        # reset screen after 1 second
        time.sleep(1)
        reset()
    # Check collision with other parts of the snake
    for t in snakes[1:]:
        if snakes[0].distance(t) < TURTLE_SIZE - 5:
            time.sleep(1)
            reset()

# window.exitonclick()

turtle.mainloop()
