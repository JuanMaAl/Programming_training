# 2. Check for Palindrome

def is_palindrome(source):
	reverse = source[::-1]
	is_pal = (source == reverse)
	return is_pal

print(is_palindrome("Hola mundo"))
print(is_palindrome("reconocer"))

# Palindrome que se lee igual del reverso que del derecho
# [inicio:fin:paso]
