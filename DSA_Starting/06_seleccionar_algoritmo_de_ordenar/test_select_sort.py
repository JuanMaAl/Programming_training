from array import array

def sort(arrays):
	length = len(arrays) - 1
	min_index = 0 # el indice del minimo seleccionado

	for i in range(0, length):
		min_index = i
		min_value = arrays[min_index]
		for j in range(i, length):
			if min_value > arrays[j + 1]:
				min_value = arrays[j + 1]
				min_index = j + 1
		# los minimos arrays[i] se intercambian con los arrays[minIndex]
		if i != min_index:
			arrays[i], arrays[min_index] = arrays[min_index], arrays[i]

def main():
	scores = array('i',[60,50,95,80,70])
	sort(scores)
	for score in scores:
		print(score,",",end="")
	print()

if __name__ == "__main__":
	main()
	
			
