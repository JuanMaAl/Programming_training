def my_compute_power_it(nb, p):
	if p < 0:
		return 0
	if p == 0:
		return 1
	x = nb
	while p > 1:
		nb *= x
		p -= 1
	return nb

"""print (my_compute_power_it(5, -1))
print (my_compute_power_it(5, 0))
print (my_compute_power_it(5, 1))
print (my_compute_power_it(5, 2))
print (my_compute_power_it(5, 3))
print (my_compute_power_it(5, 4))
print (my_compute_power_it(-5, -1))
print (my_compute_power_it(-5, 0))
print (my_compute_power_it(-5, 1))
print (my_compute_power_it(-5, 2))
print (my_compute_power_it(-5, 3))
print (my_compute_power_it(-5, 4))"""
