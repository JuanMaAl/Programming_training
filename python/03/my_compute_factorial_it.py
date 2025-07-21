def my_compute_factorial_it(number):
	if number < 0:
		return 0
	factorial = 1
	if number == 0:
		return factorial
	while number > 0:
		factorial *= number
		number -= 1
	return factorial

#print(my_compute_factorial_it(-24))
#print(my_compute_factorial_it(0))
#print(my_compute_factorial_it(6))
