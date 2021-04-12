import turtle
import time

turtle.getscreen()
t = turtle.Turtle()

# counter = int(input("HOW MANY CURVES DO YOU WANT IN YOUR PATTTERN? \n"))
counter = 5

t.rt(90)
while counter > 0:
	t.circle(20, -180)
	t.circle(-20, -180)
	counter -= 1

time.sleep(5)
print("~ WINDOW WILL CLOSE AUTOMATICLY ~")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

time.sleep(5)
