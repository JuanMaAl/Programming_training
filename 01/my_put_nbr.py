from my_putchar import *

def one_digit_to_char (digit):
	digits = "0123456789"
	return digits[digit]

def my_put_nbr(nb):
	if nb < 0:
		nb *= -1
		my_putchar("-")
	if nb // 10 > 0:
		my_put_nbr(nb // 10)
	my_putchar(one_digit_to_char(nb % 10))

#my_put_nbr(24)
#my_putchar("\n")
#my_put_nbr(24242424)
#my_putchar("\n")
#my_put_nbr(-24)
#my_putchar("\n")
