from my_putchar import *

def my_swap(int_list01, int_list02):
	temp = [0]
	temp[0] = int_list01[0]
	int_list01[0] = int_list02[0]
	int_list02[0] = temp[0]

"""number1 = [42]
number2 = [24]
print("Se espera 42: {}".format(number1[0]))
print("Se espera 24: {}".format(number2[0]))
my_swap(number1, number2)
print("Se espera 24: {}".format(number1[0]))
print("Se espera 42: {}".format(number2[0]))"""
