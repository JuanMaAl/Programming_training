from my_putchar import *
from my_put_nbr import *

def special_cases(n):
	if n < 1 or n > 10:
		i = 0
		message = "El valor de n tiene que estar entre 1 y 10 ya que el sistema decimal tiene 10 digitos diferentes 0123456789#"
		while (message[i] != "#"):
			my_putchar(message[i])
			i += 1
		my_putchar("\n")
		return True
	if n == 10:
		number = "0123456789"
		i = 0
		while (i < 10):
			my_putchar(number[i])
			i += 1
		return True
	return False

def limit(n):
	limit = 1
	while (n > 0):
		limit *= 10
		n -= 1
	return limit

def put_zeros(i, n):
	if n == 1 and i == 0:
		my_putchar("0")
		return 
	j = i
	k = 1
	while (j // 10 > 0):
		k += 1
		j //= 10
	n_zeros = n - k
	if n_zeros > 1:
		return -1
	if n_zeros > 0:
		my_putchar("0")
	
def nbr_is_printable(i, n):
	j = i
	while (j // 10 > 0):
		if (j % 100) // 10 >= j % 10:
			return False
		j //= 10
	if put_zeros(i, n) == -1:
		return False	
	return True

def my_print_combn(n):
	if special_cases(n):
		return 
	lim = limit(n)
	i = 0
	while (i < lim):
		if nbr_is_printable(i, n):
			my_put_nbr(i)
			my_putchar(" ")
		i += 1

my_print_combn(10)
