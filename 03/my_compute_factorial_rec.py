def my_compute_factorial_rec(number):
	if number < 0:
		return 0
	if number == 0:
		return 1
	return number * my_compute_factorial_rec(number -1)

#print (my_compute_factorial_rec(-24))
#print (my_compute_factorial_rec(0))
#print (my_compute_factorial_rec(6))
