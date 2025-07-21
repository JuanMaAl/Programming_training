from array import array

def sort(arrays):
	length = len(arrays)
	for i in range(0, length-1):
		isSwap = False
		for j in range(0, length-i-1):
			if arrays[j] > arrays[j+1]: # intercambiar
				arrays[j], arrays[j+1] = arrays[j+1], arrays[j]
				isSwap = True
		if isSwap == False: # Sin intercambio, asi que deja de ordenar
			break

def main():
	scores = array('i', [60, 50, 95, 80, 70])
	sort(scores)

	length = len(scores)

	for i in range(length):
		if i == 0:
			print(scores[i], end="")
			continue
		print(",", scores[i], end="")
	print()

if __name__ == "__main__":
	main()
