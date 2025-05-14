from array import array

def search(arrays, value):
	length = len(arrays)
	for i in range(0, length):
		if(arrays[i] == value):
			return i
	return - 1

def main():
	# Crea una matriz de tipo int
	arrays = array('i', [90, 70, 50, 60, 85])
	value = 60
	index = search(arrays, value) # Busca 70 y luego regresa el indice

	if(index > 0):
		print("Found value:", value, "the index is:", index)
	else:
		print("The value was not found:",value)

if __name__=="__main__":
	main()
