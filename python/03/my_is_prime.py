def my_is_prime(number):
	if number <= 1:
		return False
	i = 2
	while i < number:
		if number % i == 0:
			return False
		i += 1
	return True

"""print("False -1:", my_is_prime(-1))
print("False 0:", my_is_prime(0))
print("False 1:", my_is_prime(1))
print("True 2:", my_is_prime(2))
print("True 3:", my_is_prime(3))
print("False 4:", my_is_prime(4))
print("True 5:", my_is_prime(5))
print("False 6:", my_is_prime(6))
print("True 7:", my_is_prime(7))
print("False 8:", my_is_prime(8))
print("False 9:", my_is_prime(9))
print("True 2999:", my_is_prime(2999))
print("False 3000:", my_is_prime(3000))"""
