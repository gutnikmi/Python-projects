from random import randint, choice
from turtle import Turtle, Screen

screen = Screen()

width, height = screen.window_width(), screen.window_height()

turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.penup()


def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


def rnd():
    r = randint(1, 3)
    rtx = 0
    rty = 0
    if r == 1:
        rtx = 0
        rty = 200
    elif r == 2:
        rtx = -200
        rty = -200
    elif r == 3:
        rtx = 200
        rty = -200
    return rtx, rty





turtle.setposition(-200, -200)
turtle.dot(5, 'black')
turtle.setposition(200, -200)
turtle.dot(5, 'black')
turtle.setposition(0, 200)
turtle.dot(5, 'black')

x, y = 0, 0
xt, yt = 0, 200

for _ in range(10000):
    xr, xy = rnd()
    x, y = get_middle_point(xt, yt, xr, xy)
    turtle.setposition(x, y)
    turtle.dot(5, 'black')
    xt, yt = x, y

screen.exitonclick()
