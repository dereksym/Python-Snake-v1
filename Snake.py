import turtle
import time
import random

delay = 0.1
high_score = 0
score = 0

# Set up screen
wn = turtle.Screen()
wn.title("Snake Game by @Dereksym")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # This turns off the screen update

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.shape('square')
food.color('black')
food.penup()
food.goto(0,100)

# Add Food to Snake Body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("High Score:{}     Score:{}".format(high_score,score), align="center", font=("Courier", 24, "normal"))

# Direction Function
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# Move Function
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_left,'a')
wn.onkeypress(go_right,'d')

# Main Game Loop
while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        food.goto(random.randrange(-280,280,20), random.randrange(-280,280,20))

        score = 0
        pen.clear()
        pen.write("High Score:{}     Score:{}".format(high_score, score), align="center",font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color('black')
        new_segment.penup()
        segments.append(new_segment)

        # Shorten Delay
        delay -= 0.001

        score += 10
        if score >= high_score:
            high_score = score
        pen.clear()
        pen.write("High Score:{}     Score:{}".format(high_score, score), align="center",font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Head Collision with Body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            food.goto(random.randrange(-280,280,20), random.randrange(-280,280,20))

            score = 0
            pen.clear()
            pen.write("High Score:{}     Score:{}".format(high_score, score), align="center",font=("Courier", 24, "normal"))


    time.sleep(delay)

wn.mainloop()