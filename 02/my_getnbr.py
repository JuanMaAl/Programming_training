from my_putchar import *
from my_strlen import *

def digit_to_nbr(digit):
	digits = "0123456789"
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	i = 0
	while digits[i] != digit:
		i += 1
	return numbers[i]

def my_getnbr(string):
	number = 0
	i = 0
	sign = 1
	last = my_strlen(string)
	while string[i] == '+' or string[i] == '-' or string[i] == " ":
		if string[i] == "-":
			sign *= -1
		i += 1
	while i < last and string[i] >= '0' and string[i] <= '9':
		number = (number * 10) + digit_to_nbr(string[i])
		if number * sign > 2147483647 or number * sign < -2147483648:
			return 0
		i += 1
	return number * sign

#print(my_getnbr("---+--++---+---+---+-42"))
#print(my_getnbr("42a43"))
#print(my_getnbr("11000000000000000000000042"))
#print(my_getnbr("-1000000000000000000000042"))
