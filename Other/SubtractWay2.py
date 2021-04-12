def subtract():

numbers = [1, 2, 3, 9, 7]
length = len(numbers)
difference = 0
idx = 0
numbers = [1, 2, 3, 9, 7]	

while idx < length:
	difference = difference - numbers[idx]
	idx = idx + 1

difference = difference + numbers[0] * 2

print("\n", "Result: ", str(difference))

subtract()