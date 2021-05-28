
def lcs(s1,s2):
   
    index= -1
    index2= -1
    if len(s1) == 1:
        index=0
    if len(s2) == 1:
        index2=0
    if len(s1)==0 or len(s2) ==0: 
     return 0
    if s1[index] == s2[index2]:
        return 1 +lcs(s1[0:len(s1)-1],s2[0:len(s2)-1])
    else:
        return max(lcs(s1[0:len(s1)-1],s2[0:len(s2)]) , lcs(s1[0:len(s1)],s2[0:len(s2)-1]) )

#######################################################Dynamic Soln########################################################
def lcsDp(s1,s2,string):
    n,m=len(s1),len(s2)
    dp_t=[[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m):
        for j in range(n):
           
            if s1[j] == s2[i]:
                 dp_t[i+1][j+1]=1+dp_t[i][j]
                
            else:
                dp_t[i+1][j+1]=max(dp_t[i+1][j],dp_t[i][j+1])
      
    return dp_t 

    
    
######################################################Dynamic Soln########################################################
# Dynamic programming implementation of LCS problem

# Returns length of LCS for X[0..m-1], Y[0..n-1]
def lcs(X, Y, m, n):
	L = [[0 for x in range(n+1)] for x in range(m+1)]

	# Following steps build L[m+1][n+1] in bottom up fashion. Note
	# that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])

	# Following code is used to print LCS
	index = L[m][n]

	# Create a character array to store the lcs string
	lcs = [""] * (index+1)
	lcs[index] = ""

	# Start from the right-most-bottom-most corner and
	# one by one store characters in lcs[]
	i = m
	j = n
	while i > 0 and j > 0:

		# If current character in X[] and Y are same, then
		# current character is part of LCS
		if X[i-1] == Y[j-1]:
			lcs[index-1] = X[i-1]
			print ("".join(lcs))
			i-=1
			j-=1
			index-=1

		# If not same, then find the larger of two and
		# go in the direction of larger value
		elif L[i-1][j] > L[i][j-1]:
			i-=1
		else:
			j-=1

	print ("".join(lcs))

# Driver program
X = "AJKEQSLOBSROFGZ "
Y = "OVGURWZLWVLUXTH "
m = len(X)
n = len(Y)
lcs(X, Y, m, n)

# This code is contributed by BHAVYA JAIN
