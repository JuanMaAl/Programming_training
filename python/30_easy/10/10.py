# 10. Remove First n Characters from a String

def remove_chars(source_str, number_chars):
	new_str = source_str[number_chars:]
	return new_str

print(remove_chars("Hola mundo!", 5))
