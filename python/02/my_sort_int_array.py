def my_sort_int_array(array, size):
	i = 0
	j = 0
	while i < size - 1:
		while j < size -1:
			if array[j] > array[j + 1]:
				temp = array[j]
				array[j] = array[j + 1]
				array[j + 1] = temp
			j += 1
		j = 0
		i += 1

"""numbers = [4, 6, 9, 0, 1, 2, 5, 7, 3, 8]
print(numbers)
my_sort_int_array(numbers, 10)
print(numbers)
numbers2 = [-42, 656, -9, 0, 11, 223, 512, 27, 43, -8]
print(numbers2)
my_sort_int_array(numbers2, 10)
print(numbers2)"""
