

	
	length = len(numbers)
	difference = 0
	x = 1
	numbers = [1, 2, 3, 9, 7]
	while x < length:
	#print("diff - numbers[x] ==> " + str(difference) + "-" + str(numbers[x]))
	# Lines 8, 9, 11, 12, 15, Are ONLY for veiwing coding log, and may deleted on Subtract.py
		difference = numbers[x] - difference
	#print("x=" + str(x) + ", numbers[x]=" + str(numbers[x]) + ", diff=" + str(difference))
	#print("\n")
		
		x += 1

	print("\n", "Result: ", str(difference))

#This is just notes for Subtract.py
#May be Deleted







