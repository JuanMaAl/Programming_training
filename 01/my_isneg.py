from my_putchar import *

def my_isneg(number):
	if number < 0:
		my_putchar('N')
		my_putchar('\n')
	else:
		my_putchar('P')
		my_putchar('\n')

# my_isneg(-24)
# my_isneg(0)
# my_isneg(24)
