import turtle
import time

def squareSpiral(turtle, edge = 2):
	turtle.speed(20)
	while edge < 1000:
		turtle.circle(edge)
		turtle.rt(180)
		edge += 1	

squareSpiral(turtle.Turtle(), 3)	


time.sleep(5)


