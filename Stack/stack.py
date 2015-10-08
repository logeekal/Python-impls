#this file is for the implementation of stack

class Stack:
	def __init__(self):
		self.stack = []
		self.top = -1
	#funtion to retrieve length of the stack.
	def length(self):
		return self.top+1
	#Push function
	def push(self, x):
		self.stack.append(x);
		self.top = self.top + 1
	#Pop Function
	def pop(self):
		if self.top == -1 :
			raise IndexError('Nothing more to pop')
		else:
			print  str(self.stack[self.top] ) + ' being popped out'
			self.top = self.top - 1
			return self.stack[self.top + 1]
	#printing the stack
	def display(self):
		print self.stack[:self.top + 1]



