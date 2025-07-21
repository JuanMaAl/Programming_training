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
squares.append(square("b1", "b", "1", one[1], two[1])) 
squares.append(square("c1", "c", "1", one[2], two[2])) 
squares.append(square("d1", "d", "1", one[3], two[3])) 
squares.append(square("e1", "e", "1", one[4], two[4])) 
squares.append(square("f1", "f", "1", one[5], two[5])) 
squares.append(square("g1", "g", "1", one[6], two[6])) 
squares.append(square("h1", "h", "1", one[7], two[7])) 

squares.append(square("a2", "a", "2", one[8], two[1])) 
squares.append(square("b2", "b", "2", one[0], two[2])) 
squares.append(square("c2", "c", "2", one[1], two[3])) 
squares.append(square("d2", "d", "2", one[2], two[4])) 
squares.append(square("e2", "e", "2", one[3], two[5])) 
squares.append(square("f2", "f", "2", one[4], two[6])) 
squares.append(square("g2", "g", "2", one[5], two[7])) 
squares.append(square("h2", "h", "2", one[6], two[8])) 

squares.append(square("a3", "a", "3", one[9], two[2])) 
squares.append(square("b3", "b", "3", one[8], two[3])) 
squares.append(square("c3", "c", "3", one[0], two[4])) 
squares.append(square("d3", "d", "3", one[1], two[5])) 
squares.append(square("e3", "e", "3", one[2], two[6])) 
squares.append(square("f3", "f", "3", one[3], two[7])) 
squares.append(square("g3", "g", "3", one[4], two[8])) 
squares.append(square("h3", "h", "3", one[5], two[9])) 

squares.append(square("a4", "a", "4", one[10], two[3])) 
squares.append(square("b4", "b", "4", one[9], two[4])) 
squares.append(square("c4", "c", "4", one[8], two[5])) 
squares.append(square("d4", "d", "4", one[0], two[6])) 
squares.append(square("e4", "e", "4", one[1], two[7])) 
squares.append(square("f4", "f", "4", one[2], two[8])) 
squares.append(square("g4", "g", "4", one[3], two[9])) 
squares.append(square("h4", "h", "4", one[4], two[10])) 

squares.append(square("a5", "a", "5", one[11], two[4])) 
squares.append(square("b5", "b", "5", one[10], two[5])) 
squares.append(square("c5", "c", "5", one[9], two[6])) 
squares.append(square("d5", "d", "5", one[8], two[7])) 
squares.append(square("e5", "e", "5", one[0], two[8])) 
squares.append(square("f5", "f", "5", one[1], two[9])) 
squares.append(square("g5", "g", "5", one[2], two[10])) 
squares.append(square("h5", "h", "5", one[3], two[11])) 

squares.append(square("a6", "a", "6", one[12], two[5])) 
squares.append(square("b6", "b", "6", one[11], two[6])) 
squares.append(square("c6", "c", "6", one[10], two[7])) 
squares.append(square("d6", "d", "6", one[9], two[8])) 
squares.append(square("e6", "e", "6", one[8], two[9])) 
squares.append(square("f6", "f", "6", one[0], two[10])) 
squares.append(square("g6", "g", "6", one[1], two[11])) 
squares.append(square("h6", "h", "6", one[2], two[12])) 

squares.append(square("a7", "a", "7", one[13], two[6])) 
squares.append(square("b7", "b", "7", one[12], two[7])) 
squares.append(square("c7", "c", "7", one[11], two[8])) 
squares.append(square("d7", "d", "7", one[10], two[9])) 
squares.append(square("e7", "e", "7", one[9], two[10])) 
squares.append(square("f7", "f", "7", one[8], two[11])) 
squares.append(square("g7", "g", "7", one[0], two[12])) 
squares.append(square("h7", "h", "7", one[1], two[13])) 

squares.append(square("a8", "a", "8", one[14], two[7])) 
squares.append(square("b8", "b", "8", one[13], two[8])) 
squares.append(square("c8", "c", "8", one[12], two[9])) 
squares.append(square("d8", "d", "8", one[11], two[10])) 
squares.append(square("e8", "e", "8", one[10], two[11])) 
squares.append(square("f8", "f", "8", one[9], two[12])) 
squares.append(square("g8", "g", "8", one[8], two[13])) 
squares.append(square("h8", "h", "8", one[0], two[14])) 

#Testeo
a = 0
b = 8
c = 16
d = 24
e = 32
f = 40
g = 48
h = 56
solutions = 0
while a < 8:
	while b < 16:
		while c < 24:
			while d < 32:
				while e < 40:
					while f < 48:
						while g < 56:
							while h < 64:
								if all_ok(squares[a], squares[b], squares[c], squares[d], squares[e], squares[f], squares[g], squares[h]):
									solutions += 1
									print(squares[a].name, squares[b].name, squares[c].name, squares[d].name, squares[e].name, squares[f].name, squares[g].name, squares[h].name)
								h += 1
							g += 1
							h = 56
						f += 1
						g = 48
					e += 1
					f = 40
				d += 1
				e = 32
			c += 1
			d = 24
		b += 1
		c = 16
	a += 1
	b = 8

print(solutions)
