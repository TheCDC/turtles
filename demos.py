import turtle
import random, time
from shrinking_squares import boxes
from binary_tree import tree
from spirals import spiral

def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    turtle.setup(1920, 1000)
    t = turtle.Turtle()
    while True:
        # turtle.done()
        t.clear()
        t.speed(4)
        boxes(-490, 490, 8, t, size=900)
        time.sleep(3)
        t.clear()
        tree(0, 490, 8, t, size=1.85)
        time.sleep(3)
        t.clear()
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.speed(0)
        spiral(t,iters=400, length=400, sides=4, mult=1.1)

if __name__ == '__main__':
    main()