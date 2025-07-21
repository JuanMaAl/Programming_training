from my_putchar import *

def my_print_comb():
	n = "0123456789"
	i, j, k = 0, 1, 2
	c, d, e = n[i], n[j], n[k]
	while (i < 10):
		while (j < 10):
			while (k < 10):
				if i < j and j < k:
					my_putchar(n[i])
					my_putchar(n[j])
					my_putchar(n[k])
					if n[i] == '7' and n[j] == '8' and n[k] == '9':
						my_putchar('\n')
						return
					my_putchar(',')
					my_putchar(' ')	
				k += 1
			k = 0
			j += 1
		j = 0
		i += 1

my_print_comb()
