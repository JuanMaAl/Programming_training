from array import array

def add(arrays, value):
	length = len(arrays)
	# Cree un tempArret mas grande que el arreglo
	tempArray = array('i',[0 for x in range(length + 1)])
	for i in range(0, length):
		tempArray[i] = arrays[i] # Copiar el valor de la matriz a tempArray
	tempArray[length] = value # Insertar el valor en el ultimo indice
	return tempArray

def main():
	# Crea una matriz de tipo int
	arrays = array('i',[90,70,50,80,60,85])
	arrays = add(arrays, 75)
	length = len(arrays)
	for i in range(0, length):
		if i == 0:
			print(arrays[i], end="")
			continue
		print(",", arrays[i], end="")
	print()

if __name__ == "__main__":
	main()
