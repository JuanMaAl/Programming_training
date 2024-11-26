def my_compute_power_rec(nb, p):
	if p < 0:
		return 0
	if p == 0:
		return 1
	return nb * my_compute_power_rec(nb, p -1)

"""print (my_compute_power_rec(5, -1))
print (my_compute_power_rec(5, 0))
print (my_compute_power_rec(5, 1))
print (my_compute_power_rec(5, 2))
print (my_compute_power_rec(5, 3))
print (my_compute_power_rec(5, 4))
print (my_compute_power_rec(-5, -1))
print (my_compute_power_rec(-5, 0))
print (my_compute_power_rec(-5, 1))
print (my_compute_power_rec(-5, 2))
print (my_compute_power_rec(-5, 3))
print (my_compute_power_rec(-5, 4))"""
