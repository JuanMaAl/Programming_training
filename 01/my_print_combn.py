from my_putchar import *

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
	
my_print_comb(1)		
my_print_comb(3)		
my_print_comb(7)		
my_print_comb(9)		
my_print_comb(10)		
