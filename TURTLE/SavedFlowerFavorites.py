import turtle
import time


turtle.getscreen()
t = turtle.Turtle()

counter = 9

t.pencolor("Blue")
t.speed(20)
t.pensize(5)
while counter > 0:
	t.rt(300)
	t.circle(20, 210)
	counter -= 1

t.penup()
t.goto(+100, +120)
t.write("Flower", font = ("times new roman", 22))
time.sleep(5)
print("~ WINDOW WILL CLOSE AUTOMATICLY ~")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

time.sleep(5)
