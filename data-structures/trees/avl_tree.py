class Node():
	def __init__(self, value):
		self.value = value
	
class AVLTree():
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

	def insert(self, value):
		self.value = value

	def display(self):
		print("display")