import turtle
import time
import random

delay = 0.1
score = 0

# Screen setup
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(600, 600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Movements
def go_up(): 
    if head.direction != "down": head.direction = "up"
def go_down(): 
    if head.direction != "up": head.direction = "down"
def go_left(): 
    if head.direction != "right": head.direction = "left"
def go_right(): 
    if head.direction != "left": head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Game loop
while True:
    wn.update()

    # Border collision
    if abs(head.xcor()) > 280 or abs(head.ycor()) > 280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for seg in segments: seg.hideturtle()
        segments.clear()

    # Food collision
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)

    # Move the body
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].position())
    if segments:
        segments[0].goto(head.position())

    move()

    # Self collision
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for seg in segments: seg.hideturtle()
            segments.clear()

    time.sleep(delay)
