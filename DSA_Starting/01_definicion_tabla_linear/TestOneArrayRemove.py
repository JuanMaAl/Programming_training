from array import array

def remove(arrays, index):
	length = len(arrays)
	# Crear una matriz temporal, length = length -1
	tempArray = array('i', [0 for element in range(length - 1)])

	for i in range(0, length):
		if(i < index): # Copie los datos que antes de i = index a tempArray
			tempArray[i] = arrays[i]
		if(i > index): # Copie la matriz despues de i = index al final de tempArray
			tempArray[i - 1] = arrays[i]
	return tempArray

def main():
	arrays = array('i', [90, 70, 50, 80, 60, 85]) # Crea una matriz de tipo int
	arrays = remove(arrays, 2) # Eliminar el valor de la matriz en el indice = 2
	length = len(arrays)
	for i in range(0, length):
		if i == 0:
			print(arrays[i], end="")
			continue
		print(",", arrays[i], end="")
	print()

if __name__ == "__main__":
	main()
