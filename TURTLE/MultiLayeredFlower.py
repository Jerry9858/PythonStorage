import turtle
import time


def fourPetals(t, radius, color):
	counter = 4
	t.pencolor(color)
	t.speed(5)
	t.pensize(5)

	while counter > 0:
		t.rt(300)
		t.circle(radius, 210)
		counter -= 1 


turtle.getscreen()
t = turtle.Turtle()

fourPetals(t, 40, "red")
def petalAlignment()
t.penup()
t.rt(300)
t.circle(40, 45)
t.rt(97)
t.fd(22)
t.rt(-90)
t.rt(50)
t.pendown()

turtle.getscreen()
t = turtle.Turtle()
petalAlignment()
fourPetals(t, 40, "blue")

# t.penup()
# t.goto(+100, +120)
# t.write("Flower", font = ("times new roman", 22))
time.sleep(5)
print("~ WINDOW WILL CLOSE AUTOMATICLY ~")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

time.sleep(10000)
