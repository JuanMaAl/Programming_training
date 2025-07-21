#Tablero de ajedrez 4x4 colocando 4 reinas sin ataques mutuos
# columnas de la 'a' a la 'd' y filas de la '1' a la '4'
# cada casilla tiene un nombre formado por la columna + la fila
# Ejemplo del tablero:
# a4 b4 c4 d4
# a3 b3 c3 d3
# a2 b2 c2 d2
# a1 b1 c1 d1

#Creando la clase para las casillas
class square:
	def __init__(self, name, file, rank, diagonal_one, diagonal_two):
		self.name = name
		self.file = file
		self.rank = rank
		self.diagonal_one = diagonal_one
		self.diagonal_two = diagonal_two

#funcion para comprobar que dos damas no se atacan
def two_ok(queen_a, queen_b):
	if queen_a.name == queen_b.name:
		return False
	if queen_a.file == queen_b.file:
		return False
	if queen_a.rank == queen_b.rank:
		return False
	if queen_a.diagonal_one == queen_b.diagonal_one:
		return False
	if queen_a.diagonal_two == queen_b.diagonal_two:
		return False
	return True

#funcion para comprobar que todas las damas no se atacan
def all_ok(q_one, q_two, q_three, q_four):
	if not two_ok(q_one, q_two):
		return False
	if not two_ok(q_one, q_three):
		return False
	if not two_ok(q_one, q_four):
		return False
	if not two_ok(q_two, q_three):
		return False
	if not two_ok(q_two, q_four):
		return False
	if not two_ok(q_three, q_four):
		return False
	return True
	
#Creando la lista de diagonales
one = [
"a1b2c3d4", #0
"b1c2d3", #1
"c1d2", #2
"d1", #3
"a2b3c4",#4 
"a3b4", #5
"a4" #6
]
two = [
"a1", #0
"b1a2", #1
"c1b2a3", #2
"d1c2b3a4", #3
"d2c3b4", #4
"d3c4", #5
"d4" #6
]

#Creando la lista
squares = []

squares.append(square("a1", "a", "1", one[0], two[0])) 
squares.append(square("b1", "b", "1", one[1], two[1])) 
squares.append(square("c1", "c", "1", one[2], two[2])) 
squares.append(square("d1", "d", "1", one[3], two[3])) 
squares.append(square("a2", "a", "2", one[4], two[1])) 
squares.append(square("b2", "b", "2", one[0], two[2])) 
squares.append(square("c2", "c", "2", one[1], two[3])) 
squares.append(square("d2", "d", "2", one[2], two[4])) 
squares.append(square("a3", "a", "3", one[5], two[2])) 
squares.append(square("b3", "b", "3", one[4], two[3])) 
squares.append(square("c3", "c", "3", one[0], two[4])) 
squares.append(square("d3", "d", "3", one[1], two[5])) 
squares.append(square("a4", "a", "4", one[6], two[3])) 
squares.append(square("b4", "b", "4", one[5], two[4])) 
squares.append(square("c4", "c", "4", one[4], two[5])) 
squares.append(square("d4", "d", "4", one[0], two[6]))

#Testeo
i = 0
j = i + 1
k = j + 1
l = k + 1
solutions = 0
while i < 16:
	while j < 16:
		while k < 16:
			while l < 16: 
				if all_ok(squares[i], squares[j], squares[k], squares[l]):
					solutions += 1
					print(squares[i].name, squares[j].name, squares[k].name, squares[l].name)
				l += 1

			k += 1
			l = k
		j += 1
		k = j
	i += 1
	j = i
print(solutions)
