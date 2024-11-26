def my_find_prim_sup(number):
	if number <= 2:
		return 2
	i = 2
	while number:
		while number % i != 0:
			i += 1
			if i == number:
				return number
		number += 1
		i = 2

"""print("2:", my_find_prim_sup(-1))
print("2:", my_find_prim_sup(0))
print("2:", my_find_prim_sup(1))
print("2:", my_find_prim_sup(2))
print("3:", my_find_prim_sup(3))
print("5:", my_find_prim_sup(4))
print("5:", my_find_prim_sup(5))
print("7:", my_find_prim_sup(6))
print("7:", my_find_prim_sup(7))
print("11:", my_find_prim_sup(8))
print("11:", my_find_prim_sup(9))
print("3001:", my_find_prim_sup(3000))"""
