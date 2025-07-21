# 6 Merge Two Sorted Lists

def merge_sorted_lists(lst1, lst2):
	big_list = lst1 + lst2
	sorted_list = sorted(big_list)
	return sorted_list

lst1 = ['manzana', 'pera', 'mandarina', 'zanahoria']
lst2 = ['coche', 'autocar', 'camion', 'bicicleta']
print(merge_sorted_lists(lst1, lst2))
