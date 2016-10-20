#!/usr/bin/env python3
import turtle
import random
import colorsys
from turtils import line

def randcolor():
    # turtle color values are between 0 and 1, not 0 and 255
    return tuple([random.randint(0, 255) / 255 for i in range(3)])



def tree(x, y, n, t=None, size=10) -> None:
    if n == 0:
        return
    if not t:
        t = turtle.Turtle()
    fact = 2**n
    p1 = (x + fact * size, y - fact * size)
    p2 = (x - fact * size, y - fact * size)
    tree(*p2, n - 1, t, size=size)
    tree(p1[0], p1[1], n - 1, t, size=size)
    t.pencolor(
        colorsys.hsv_to_rgb(random.random(), 1, 1 )
    )
    t.penup()
    t.setpos(x,y)
    t.dot(fact)
    line(t,(x,y),p1)
    line(t,(x,y),p2)


def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    turtle.setup(1920, 1000)
    t = turtle.Turtle()
    t.speed(4)
    tree(0, 490, 8, t, size=1)
    # for i in range(1,9):
    #     tree(0,490,i,t,size=1)
    # tree(0,400,6,t,size=1)
    # tree(0,400,8,t,size=1)
    turtle.done()
if __name__ == '__main__':
    main()
