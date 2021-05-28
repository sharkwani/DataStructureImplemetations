# Sparse table implementation in python 
import math
class SparseTables():
	LOGBASEVALUE=2
	
	def __init__(self , array_to_sparse):
		self.array_to_sparse = array_to_sparse
		self.sparse_table=[]
		
	def __len__(self):
		return len(self.array_to_sparse) , len(sparse_table)
		
		
		
	def calculateLogValue(self):
		
		input_array_length = len(self.array_to_sparse)
			
		if input_array_length != 0:
			return math.ceil(math.log(input_array_length , self.LOGBASEVALUE ))
		else:
			raise Exception("input array is of length ZERO")
			
	def build(self):
		
		LOG = self.calculateLogValue() + 1
		self.sparse_table = [[0 for i in range(LOG)] for j in range(len(self.array_to_sparse))]
		for index in range(n):
			self.sparse_table[index][0] = self.array_to_sparse[index]
		for logValues in range(1,LOG):
			index = 0
			while  (index + (1 << logValues))  <= len(self.array_to_sparse):
				self.sparse_table[index][logValues] = min(self.sparse_table[index][logValues-1],self.sparse_table[index+(1<<(logValues -1 ))][logValues-1])
				
				index+=1
		return self.sparse_table