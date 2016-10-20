#!/usr/bin/env python3
import turtle
import random
import colorsys
from turtils import line

def randcolor():
    # turtle color values are between 0 and 1, not 0 and 255
    return tuple([random.randint(0, 255) / 255 for i in range(3)])


def boxes(x, y, n, t=None, size=10) -> None:
    if n == 0:
        return
    fact = 1/(2**(1/2))
    t.pencolor(
        colorsys.hsv_to_rgb(random.random(), (random.random() + 1)/2, 1 )
    )
    t.penup()
    t.setpos(x,y)
    t.pendown()
    # t.seth(0)
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.forward(size/2)
    t.right(45)
    for i in range(4):
        t.forward(size*fact)
        t.right(90)
    t.forward(size*fact/2)
    t.right(45)
    boxes(t.xcor(),t.ycor(),n-1,t,size*(fact**2))


def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    turtle.setup(1920, 1000)
    t = turtle.Turtle()
    t.speed(4)
    boxes(-490, 490, 15, t, size=900)
    turtle.done()
if __name__ == '__main__':
    main()
