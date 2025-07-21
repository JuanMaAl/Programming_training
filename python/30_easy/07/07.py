# 7. Check if First and Last Elements Are the Same

def first_last_same(lst):
	are_the_same = (lst[0] == lst[-1])
	return are_the_same

print(first_last_same(['Adios', 'Hola', 'Filete']))
print(first_last_same(['Hola', 'tarde', 'Hola']))
