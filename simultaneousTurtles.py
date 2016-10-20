#!/usr/bin/env python3
# import libraries we will be using
import turtle
import random

def randcolor():
	# turtle color values are between 0 and 1, not 0 and 255
	return tuple([random.randint(0,255)/255 for i in range(3)])


# initialize the display window
wn = turtle.Screen()
wn.bgcolor("black")
turtles = []
for i in range(10):
	turtles.append(turtle.Turtle())

for t in turtles:
	t.pencolor(randcolor())
	t.speed(0)

for i in range(300):
# while True:
	for t in turtles:
		t.left(random.random()*180 - 90)
		t.fd(random.random()*20)

wn.exitonclick()