from my_putchar import *

def my_putstr(string):
	i = 0
	string += "\0"
	while string[i] != '\0':
		my_putchar(string[i])
		i += 1
	my_putchar("\n")

#string = "Hello World!"
#my_putstr(string)
