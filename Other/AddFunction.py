def add(numbers):
	sum = 0
	for x in numbers:
		sum +=  x
	return sum
 	
 
def string2char(string):
	for x in string:
		print(x + ",")


def addfloat(numbers):
	floatNo = 0
	for x in listOfFloat:
		floatNo +=  x
	return floatNo

	def main_entry() :
	strOfFloat = input("Enter an array of floats (decimals eg: 1.1) \n")
	listOfFloat = strOfFloat.split(",")
	listOfFloat = [float(m) for m in listOfFloat]

#word = input("Enter a word(s) \n") 
#print(add([1.1, 2.2, 3]))
#string2char(word)

#This is for add()
# number = input("Enter an array of numbers \n")
# m = 0
# listOfNumbers = number.split(",")
# listOfNumbers = [int(m) for m in listOfNumbers]


# This is for addfloat()
strOfFloat = input("Enter an array of floats (decimals eg: 1.1) \n")
	listOfFloat = strOfFloat.split(",")
	listOfFloat = [float(m) for m in listOfFloat]


# print(add(int(number)))
# print(add("banana"))

# print(add(listOfNumbers))
print(addfloat(listOfFloat))




