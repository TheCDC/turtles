#!/usr/bin/env python3
# the previous line is called a shebang. Don't worry about it.
# it allows you to run your code with just "./programname.py"
# on UNIX systems.


# import libraries we will be using
import turtle
import random

# initialize the display window
turtle.setup(1920,1080)
wn = turtle.Screen()
wn.bgcolor("black")


# define a helper function
def randcolor():
    # turtle color values are between 0 and 1, not 0 and 255
    return tuple([random.randint(0,255)/255 for i in range(3)])

# we want between 3 and 10 turtles
for i in range(random.randint(3,15)):
    # for each of those, initialize them
    t = turtle.Turtle()
    t.speed(0)
    # also start them with a random color and direction
    t.pencolor(randcolor())
    t.left(random.random()*360)
    # make them move randomly
    precision = 10
    for j in range(random.randint(3*precision,30*precision)):
        # give the turtle random forward movement and random turning
        t.fd(random.randint(0,100/precision))
        t.left((random.random()*180 - 90)/(precision**(1/2)))

# make it only close when you click it
wn.exitonclick()