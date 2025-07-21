# 4. Remove Duplicates from a list

def remove_duplicates(source):
	new_list = set(source)
	return new_list

marcas_coches = ['Mercedes', 'Audi', 'Ferrari', 'Renault', 'Fiat', 'Seat', 'Mercedes', 'Fiat']

print(remove_duplicates(marcas_coches))

# set coleccion no ordenada y sin duplicados

