import turtle
import time


turtle.getscreen()
t = turtle.Turtle()

counter = int(input("ENTER THE NUMBER OF RINGS YOU WANT ON YOUR TARGET DRAWING: \n"))
raidus = 5
distance = 5
while counter > 0:
	raidus += distance
	t.speed(10)
	t.circle(raidus)
	t.penup()
	t.rt(90)
	t.fd(distance * 2)
	t.lt(90)
	t.pendown()
	counter -= 1

time.sleep(5)
print("~ WINDOW WILL CLOSE AUTOMATICLY ~")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

time.sleep(5)
