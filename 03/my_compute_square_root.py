def my_compute_square_root(number):
	if number <= 0:
		return 0
	i = 1
	while i * i <= number:
		if i * i == number:
			return i
		i += 1
	return 0

"""print(my_compute_square_root(-4))
print(my_compute_square_root(0))
print(my_compute_square_root(1))
print(my_compute_square_root(25))
print(my_compute_square_root(4096))
print(my_compute_square_root(26))
print(my_compute_square_root(4097))"""
