import turtle
import time

turtle.getscreen()
t = turtle.Turtle()

counter = int(input("HOW MANY CURVES DO YOU WANT IN YOUR PATTTERN? \n"))

t.rt(-90)
while counter > 0:
	t.circle(20, 180)
	t.rt(180)
	counter -= 1

time.sleep(5)
print("~ WINDOW WILL CLOSE AUTOMATICLY ~")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

time.sleep(95)
