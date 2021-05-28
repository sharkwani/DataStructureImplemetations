
def computeZArray(string):
	left , r  = 0 , 0
	n = len(string)
	array=[0]*n
	for l in range(1,n):
		if l <= r:
			array[l] = min(r-l+1 ,array[l-left])
		while l+array[l] < n and string[array[l]] == string[l+array[l]] :
			array[l]+=1
		if l+array[l] -1 > r:
			left = l
			r= l +array[l] -1
	print(array)
	return array

string = input()
pattern = input()
stringToProcess= pattern+"$"+string
z = computeZArray(stringToProcess)

n = len(stringToProcess) - len(string)

patlen = len(pattern)
for index , x   in enumerate(z):
	if x == patlen :
		print(index - n)