def my_strcpy(dest, src):
	# dest[0] = src, iteraremos caracter a caracter como en C para que haya ejercicio
	temp = ""
	src += "\0"
	i = 0
	while (src[i] != '\0'):
		temp += src[i]
		i += 1
	dest[0] = temp

"""# Una string es un objeto inmutable en python. En python la funcion strcpy no tiene 
# tanto sentido como en C
src = "Hola mundo"
dest = ["Adios mundo"]
print(dest)
my_strcpy(dest, src)
print(dest)
src2 = ""
my_strcpy(dest, src2)
print(dest)"""
