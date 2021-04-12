#no1 - no2 - no3 - no4 - no5
def subtract(numbers):
	length = len(numbers)
	difference = 0
	idx = 1
	while idx < length:
		difference = difference - numbers[idx]
		idx += 1

	difference = difference + numbers[0]
	return difference	

print(subtract([1, 2, 3, 9, 7]))
