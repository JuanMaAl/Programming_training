#Tablero de ajedrez 8x8 colocando 8 reinas sin ataques mutuos
# columnas de la 'a' a la 'h' y filas de la '1' a la '8'
# cada casilla tiene un nombre formado por la columna + la fila
# Ejemplo del tablero:
# a8 b8 c8 d8 e8 f8 g8 h8
# a7 b7 c7 d7 e7 f7 g7 h7
# a6 b6 c6 d6 e6 f6 g6 h6
# a5 b5 c5 d5 e5 f5 g5 h5
# a4 b4 c4 d4 e4 f4 g4 h4
# a3 b3 c3 d3 e3 f3 g3 h3
# a2 b2 c2 d2 e2 f2 g2 h2
# a1 b1 c1 d1 e1 f1 g1 h1

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
def all_ok(q_one, q_two, q_three, q_four, q_five, q_six, q_seven, q_eight):
	if not two_ok(q_one, q_two):
		return False
	if not two_ok(q_one, q_three):
		return False
	if not two_ok(q_one, q_four):
		return False
	if not two_ok(q_one, q_five):
		return False
	if not two_ok(q_one, q_six):
		return False
	if not two_ok(q_one, q_seven):
		return False
	if not two_ok(q_one, q_eight):
		return False

	if not two_ok(q_two, q_three):
		return False
	if not two_ok(q_two, q_four):
		return False
	if not two_ok(q_two, q_five):
		return False
	if not two_ok(q_two, q_six):
		return False
	if not two_ok(q_two, q_seven):
		return False
	if not two_ok(q_two, q_eight):
		return False

	if not two_ok(q_three, q_four):
		return False
	if not two_ok(q_three, q_five):
		return False
	if not two_ok(q_three, q_six):
		return False
	if not two_ok(q_three, q_seven):
		return False
	if not two_ok(q_three, q_eight):
		return False

	if not two_ok(q_four, q_five):
		return False
	if not two_ok(q_four, q_six):
		return False
	if not two_ok(q_four, q_seven):
		return False
	if not two_ok(q_four, q_eight):
		return False
	
	if not two_ok(q_five, q_six):
		return False
	if not two_ok(q_five, q_seven):
		return False
	if not two_ok(q_five, q_eight):
		return False

	if not two_ok(q_six, q_seven):
		return False
	if not two_ok(q_six, q_eight):
		return False

	if not two_ok(q_seven, q_eight):
		return False

	return True
	
#Creando la lista de diagonales
one = [
"a1b2c3d4e5f6g7h8", #0
"b1c2d3e4f5g6h7", #1
"c1d2e3f4g5h6", #2
"d1e2f3g4h5", #3
"e1f2g3h4",#4 
"f1g2h3", #5
"g1h2", #6
"h1", #7
"a2b3c4d5e6f7g8", #8
"a3b4c5d6e7f8", #9
"a4b5c6d7e8", #10
"a5b6c7d8", #11
"a6b7c8", #12
"a7b8", #13
"a8" #14
]
two = [
"a1", #0
"b1a2", #1
"c1b2a3", #2
"d1c2b3a4", #3
"e1d2c3b4a5", #4
"f1e2d3c4b5a6", #5
"g1f2e3d4c5b6a7", #6
"h1g2f3e4d5c6b7a8", #7
"h2g3f4e5d6c7b8", #8
"h3g4f5e6d7c8", #9
"h4g5f6e7d8", #10
"h5g6f7e8", #11
"h6g7f8", #12
"h7g8", #13
"h8" #14
]

#Creando la lista
squares = []

squares.append(square("a1", "a", "1", one[0], two[0])) 

#Testeo
a = 0
b = a + 1
c = b + 1
d = c + 1
e = d + 1
f = e + 1
g = f + 1
h = g + 1
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
