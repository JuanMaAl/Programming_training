from my_strlen import *

def my_evil_str(string):
	last = my_strlen(string) - 1
	rev_str = ""
	while last >= 0:
		rev_str += string[last]
		last -= 1
	return rev_str

#print(my_evil_str("a"))	
#print(my_evil_str("ab"))	
#print(my_evil_str("abc"))	
#print(my_evil_str("abcd"))	
#print(my_evil_str("abcde"))	
#print(my_evil_str("abcdef"))	
