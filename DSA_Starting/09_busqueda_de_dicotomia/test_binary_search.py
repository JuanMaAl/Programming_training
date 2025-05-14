from array import array

def binary_search(arrays, search_value):
	length = len(arrays)
	low = 1
	high = length - 1
	mid = 0
	while low <= high:
		mid = (low + high) // 2
		if arrays[mid] == search_value:
			return mid
		elif arrays[mid] < search_value:
			low = mid + 1
		elif arrays[mid] > search_value:
			high = mid -1
	return -1

def print_result(scores, value):
	position = binary_search(scores, value)
	if position < 0:
		print(value,"not found")
	else:
		print(value,"position:",position)
	print("------------------------------")


def main():
	scores = array('i', [30, 40, 50, 70, 85, 90])
	print(scores)
	print()
	print_result(scores, 40)
	print_result(scores, 90)
	print_result(scores, 45)

if __name__ == "__main__":
	main()

