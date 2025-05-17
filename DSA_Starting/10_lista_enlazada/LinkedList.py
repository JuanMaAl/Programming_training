# import pdb

class Node:
	data = ''
	next = None

	def __init__(self, data, next):
		self.data = data
		self.next = next


class LinkedList:
	__head = None
	__tail = None

	def init(self):
		self.__head = Node("A", None)
		nodeB = Node("B", None)
		self.__head.next = nodeB

		nodeC = Node("C", None)
		nodeB.next = nodeC

		#el ultimo nodo llamado cola nodo
		self.__tail = Node("D", None)
		nodeC.next = self.__tail
	
	def insert(self, insertPosition, newNode):
		# pdb.set_trace()
		p = self.__head
		i = 0
		# Mueva el nodo a la posicion de insercion
		while p.next != None and i < insertPosition -1:
			p = p.next
			i += 1
		newNode.next = p.next
		p.next = newNode

	def remove(self, removePosition):
		p = self.__head
		i = 0
		# Mueve el nodo a la posicion anterior del nodo a remover
		while p.next != None and i < removePosition -1:
			p = p.next
			i += 1
		temp = p.next # Guarda el nodo que desea eliminar
		p.next = p.next.next
		temp.next = None # Elimina el nodo
		
	@property
	def head(self):
		return self.__head
	
############################# test ############################

def output(node):
	p = node
	while(p != None): # Desde el principio hasta el final
		data = p.data
		print(data, "-> ", end="")
		p = p.next
	print("End\n\n")

def main():
	linkedlist = LinkedList()
	linkedlist.init()

	linkedlist.insert(3, Node("E", None)) # Insertar un nuevo nodo en la posicion 2
	linkedlist.remove(2) # Remover el nodo en la tercera posicion
	output(linkedlist.head)

if __name__ == "__main__":
	main()
















