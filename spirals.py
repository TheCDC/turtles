#!/usr/bin/env python3

import turtle # allows us to use the turtles library
import colorsys #for converting colors
import math
import time
import random	

def spiral(t,iters, length,sides,mult):
	ang = 360/sides
	for i in range(iters):
		# t.pencolor(colorsys.hsv_to_rgb((math.atan2(t.xcor(),t.ycor()) + math.pi)/math.pi,1,1))
		t.pencolor(colorsys.hsv_to_rgb(i/(iters/sides),1,1))
		# t.pencolor(colorsys.hsv_to_rgb(1 - i/iters,1,1))
		t.fd(length*i/iters)
		t.left((mult)*360/sides)

def main():
	wn = turtle.Screen()        # creates a graphics window
	wn.bgcolor("black")
	alex = turtle.Turtle()      # create a turtle named alex
	numSides = 5
	turnAngle = 360.0/numSides
	offsetMult = 1.2
	alex.speed(0)
	iterations = 400
	baseLength = 400
	alex.clear()
	spiral(alex,iters=400,
		length=400,
		sides=4,
		mult=1.1)
	alex.getscreen().getcanvas().postscript(file="out.eps")
	wn.exitonclick()

	# final y position?
if __name__ == '__main__':
	main()