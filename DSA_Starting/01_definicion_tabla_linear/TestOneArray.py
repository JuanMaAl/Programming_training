from array import array

def main():
	# Crea una matriz de tipo int
	print(arrays)
	length = len(arrays)

	for i in range(0, length):
		if i == 0:
			print(arrays[i], end="")
			continue
		print(",", arrays[i], end="")
	print()

if __name__ == "__main__":
	main()

