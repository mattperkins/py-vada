import turtle
import os

# setup screen
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("SpaceVada")

# draw border
border_pen = turtle.Turtle()
bp = border_pen
bp.speed(0)
bp.color("white")
bp.penup()
bp.setposition(-280,-270)
bp.pendown()
bp.pensize(3)
for side in range(4):
    bp.fd(550)
    bp.lt(90)
bp.hideturtle()

# create player
player = turtle.Turtle()
p = player
p.color("blue")
p.shape("triangle")
p.penup()
p.speed(0)
p.setposition(0, -250)
p.setheading(90)

# move player with left right arrows on keyboard
playerspeed = 15
ps = playerspeed
t = turtle

def move_left():
    x = p.xcor()
    x -= ps
    p.setx(x)
def move_right():
    x = p.xcor()
    x += ps
    p.setx(x)
def move_up():
    y = p.ycor()
    y += ps
    p.sety(y)
def move_down():
    y = p.ycor()
    y -= ps
    p.sety(y)

t.listen()
t.onkey(move_left, "Left")
t.onkey(move_right, "Right")
t.onkey(move_up, "Up")
t.onkey(move_down, "Down")





delay = input("Press enter to quit")







