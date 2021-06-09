class DisjointSet:
	def __init__(self , vertices):
		self.vertices = vertices
		self.parent = {}
		for node in self.vertices:
			self.parent[node] = node
			
		self.rank = dict.fromkeys(vertices , 0)
	
	
	def find(self, node):
		if self.parent[node] == node:
			return node
		else:
			return self.find(self.parent[node])
			
	def union(self , A , B):
		nodeA = self.find(A)
		nodeB= self.find(B)
		if self.rank[nodeA] < self.rank[nodeB]:
			self.parent[nodeB] = nodeA
			self.rank[nodeA]+=1
		elif self.rank[nodeA] > self.rank[nodeB]:
			self.parent[nodeA] = nodeB
			self.rank[nodeB]+=1
			
			
		else:
			self.parent[nodeB] = nodeA
if __name__ =="__main__":	
	vertices = ["A" , "B" , "C", "D" , "E" ,"F"]
	disjointObj = DisjointSet(vertices)

	print(disjointObj.parent)


	disjointObj.union("D" , "E")
	disjointObj.union("D" , "F")
	disjointObj.union("D" , "A")
	disjointObj.union("A" , "C")

	print(disjointObj.parent)