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

	output(linkedlist.head)

if __name__ == "__main__":
	main()
















