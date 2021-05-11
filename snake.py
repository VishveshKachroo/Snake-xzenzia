import turtle
import time
import random

delay= 0.1
#main window
window = turtle.Screen()
window.title("snake game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shapesize()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)

segments = []

#functions
def go_up():
    head.direction="up"
def go_down():
    head.direction="down"
def go_left():
    head.direction="left"
def go_right():
    head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")

#main game loop
while True:
    window.update()
    #window collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide segments
        for segment in segments:
            segment.goto(1000, 1000)
        #clear the segments list
        segments.clear()
    if head.distance(food)<20:
        #move food to random spot
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)

        #snake body
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to where head is
    if len(segments)> 0:
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)


    move()
    #body collisions
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
    time.sleep(delay)
window.mainloop()