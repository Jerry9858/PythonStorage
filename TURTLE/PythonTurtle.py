import turtle
import time



def square(length):
	turtle.getscreen()
	turtle.clear()
	w = 0
	t = turtle.Turtle()
	while w < 4:
		print(type(length))
		t.fd(length)
		t.rt(90)
		w += 1

	time.sleep(5)


parameter = input("Enter the length of the square: \n")
distance = int(parameter)
print(distance)
square(distance)









