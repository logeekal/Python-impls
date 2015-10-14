 #This program demonstrates linear hashing

class hash():
	def __init__(self, size):
		while  size <= 0:
			print 'Please reneter the correct size of Hash table you want to create : ' ,
			self.size = int(raw_input())
		else:
			self.size = size
		self.lst = [0 for i in range(self.size)]
		self.active_size = 0
	def add_key(self, key):
		""" Object.add_key(key) adds values to a particular hashTable"""
		#check if the HashTable is 75% full. stop new insertions.
		if self.active_size ==  int((3*self.size)/4):
			print self.active_size
			raise IndexError("No more insertion allowed. Hashtable is full")
		if type(key) == int :
			calc_key = key
		h_index = key%self.size
		#hash_func(self.size, calc_key)

		while self.lst[h_index] != 0:
			print h_index ,
			h_index = h_index + 1
			while h_index  >= self.size :
				h_index = self.size - h_index
			
		self.lst[h_index] = key
		self.active_size += 1
		print self.lst


	def linear_hash(size, key):
		return key%size + 1

	def hash_fun(size,key):
		return liner_hash(size,key)


a= hash(12)
a.add_key(55)

