import turtle
import time


s = turtle.getscreen()
t = turtle.Turtle()

counter = input("ENTER THE NUMBER OF RINGS YOU WANT ON YOUR TARGET DRAWING: \n")
counter = int(counter)
raidus = 5
distance = 9
while counter > 0:
	t.speed(10)
	t.circle(raidus)
	t.penup()
	t.rt(90)
	t.fd(distance)
	t.lt(90)
	t.pendown()
	raidus += distance
	counter -= 1

time.sleep(5)
print("~ WINDOW WILL CLOSE AUTOMATICLY ~")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

time.sleep(5)
