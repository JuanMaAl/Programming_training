# 8.Display Numbers Divisible by Five

def divisible_by_five(lst):
	divisibles_by_five = []
	for number in lst:
		if number % 5 == 0:
			divisibles_by_five.append(number)
	return divisibles_by_five

numbers_lst = []
for number in range(1, 101):
	numbers_lst.append(number)
print(numbers_lst)
print()
print(divisible_by_five(numbers_lst))
