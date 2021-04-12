import turtle
import time

def squareSpiral(turtle, edge = 2):
	while edge < 108:
		turtle.fd(edge)
		turtle.rt(90)
		edge += 3	

squareSpiral(turtle.Turtle(), 3)	



time.sleep(5)