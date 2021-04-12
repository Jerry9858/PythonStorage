def sum1(start = 1, end = 91, step = 5):
	num = list(range(start, end, step))
	print(num)
	sum = 0
	for x in num:
		sum += x

	print(sum)
