class TNode:
	def __init__(self,data=None,left=None,right= None):
		self._data   = data
		self._left   = left
		self._right  = right
		self._parent = parent

	def setData(self,._data):
		self._data = data
		return True
	def setLeft(self, node):
		self._left = left
		return True
	def setRight(self, node):
		self._right = right
	def getData(self):
		return self._data
	def getLeft(self):
		return self._left
	def getRight(self):
		return self._right
	def getParent(self):
		return self._parent

class BST():
	def __init__(self,data=None):
		self._root = TNode(data)
	def getRoot(self):
		return self._root
	def add(self, data):
		root_val = self.getRoot().getData()
		if  root_val is None:
			self.getRoot().setData() = data
		current = self.getRoot()
		while current is not None:
			if root_val > data:
				current = current.getLeft()
			elif root_val < data:
				current = current.getRight()


