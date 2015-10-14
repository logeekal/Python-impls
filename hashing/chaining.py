from linked_list import LinkedList as llist

class chain:
	def __init__(self,size):
		self.chain = [0 for i in range(size)]
		self.size = size
		self.active_size = 0
	def add(self,key):
		""" Object,add(key) adds a particular key at designated location """
		h_index = key%self.size
		if self.chain[h_index] == 0 :
			self.chain[h_index] =  llist()
		self.chain[h_index].add(key)
	def display(self):
		"""object.display() displays the chained hash table"""
		for h_index in xrange(self.size):
			if self.chain[h_index] != 0:
				print str(h_index)  + ' ---> ' , self.chain[h_index].prnt() ,'\n'
			else:
				print h_index, ' \n'

	def search(self,key):
		for h_index in xrange(self.size):
			if self.chain[h_index] != 0:
				if self.chain[h_index].lookup(key) != -1:
					print str(h_index)  + ' ---> ' , self.chain[h_index].prnt() ,'\n'
					return h_index 
				else:
					print "Key not Found"
					return False

"""
a = chain(12)
a.add(12)
a.add(55)
a.add(67)
a.display()"""
