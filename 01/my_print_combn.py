from my_putchar import *

def print_one_digit(n = -1):
	digit = "0123456789"
	i = 0
	while i < 10:
		if (n >= 0):
			my_putchar(digit[n])
		my_putchar(digit[i])
		i += 1

def print_two_digits(n = -1):
	digit = "0123456789"
	i = 0
	while i < 10:
		if (n >= 0):
			my_putchar(digit[n])
		print_one_digit(i)
		i += 1

def my_print_comb(n):
	if n > 10:
		n = 10
	if n < 0:
		n = 0
	digit = "0123456789"
	digit_arr = [] 
	i = n
	j = 0
	while i > 0:
		digit_arr.append(j)
		j += 1
		i -= 1
	i = 0
	while i < n:
		my_putchar(digit[digit_arr[i]])
		i += 1
	my_putchar("\n")
	
print_two_digits()		
