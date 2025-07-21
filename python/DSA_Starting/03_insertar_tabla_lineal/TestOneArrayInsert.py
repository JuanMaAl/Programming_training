from array import array

def insert(arrays, value, insertIndex):
	length = len(arrays)
	# Cree un tempArray mas grande que el arreglo
	tempArray = array('i',[0 for element in range(length + 1)])
	# print(tempArray)

	for i in range(0, length):
		if i < insertIndex:
			tempArray[i] = arrays[i] # Copie el valor que antes de i = insertIndex a tempArray
		else:
			tempArray[i + 1] = arrays[i] # Copie los elementos restantes en tempArray
	tempArray[insertIndex] = value # Inserte valor en tempArray
	return tempArray

# print(insert([20, 5, 6, 7, 8], 777, 2))

def main():
	# Crea una matriz de tipo int
	arrays = array('i',[90, 70, 50, 80, 60, 85])

	arrays = insert(arrays, 75, 2) #Inserte 75 en la matriz en i = 2
	length = len(arrays)
	for i in range(0, length):
		if i == 0:
			print(arrays[i], end="")
			continue
		print(",", arrays[i], end="")
	print()

if __name__ == "__main__":
	main()
