def my_strlen(string):
	string += "\0"
	i = 0
	while string[i] != '\0':
		i += 1
	return i

#string = "Hola mundo"
#print("my_strlen:", my_strlen(string))
#print("python len:", len(string))
