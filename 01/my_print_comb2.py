from my_putchar import *

def put_digits(a, b, c, d):
	n = "0123456789"
	my_putchar(n[a])
	my_putchar(n[b])
	my_putchar(" ")
	my_putchar(n[c])
	my_putchar(n[d])
	if a == 9 and b == 8 and c == 9 and d == 9:
		my_putchar("\n")
		return 
	my_putchar(",")
	my_putchar(" ")

def two_loops(a, b):
	c, d = 0, 0
	while (c <= 9):
		while (d <= 9):
			if ((a * 10 + b) < (c * 10 + d)):
				put_digits(a, b, c, d)		
			d += 1
		d = 0
		c += 1

def my_print_comb2():
	a, b = 0, 0
	while (a <= 9):
		while (b <= 9):
			two_loops(a, b)
			b += 1
		b = 0
		a += 1

# my_print_comb2()
