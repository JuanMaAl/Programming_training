from my_putchar import *
from my_put_nbr import *

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
	while (n_zeros > 0):
		my_putchar("0")
		n_zeros -= 1


def my_print_combn(n):
	lim = limit(n)
	i = 0
	while (i < lim):
		put_zeros(i, n)
		my_put_nbr(i)
		my_putchar(" ")
		i += 1

my_print_combn(9)
