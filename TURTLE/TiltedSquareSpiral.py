from turtle import Screen
import turtle
import time
def squareSpiral(turtle, edge = 2):
	print("speed20")
	turtle.speed(20)
	size = 3
	for x in range(400):
		print(x)
		turtle.forward(x)
		turtle.rt(50)
		turtle.pensize(size)
		size += 1


print("black")
# turtle.bgcolor("black")
screen = Screen()
screen.colormode(255)
turtle.pencolor((164, 235, 52))
print("white")
t = turtle.Turtle()
print(t)
squareSpiral(t, 3)	


# time.sleep(5)


