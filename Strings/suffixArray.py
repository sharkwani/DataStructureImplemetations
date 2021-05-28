class SuffixNode:
     def __init__(self):
         self.rank=[0,0]
         self.index=0
def buildSuffixArray(txt):
    n = len(txt)
    suffixArray = [SuffixNode() for _ in range(n)]
    for i in range(n):
        suffixArray[i].index = i 
        suffixArray[i].rank[0] =  ord(txt[i]) - ord("a")
        suffixArray[i].rank[1] =   ord(txt[i+1]) - ord("a") if (i + 1 < n ) else -1 
    suffixArray = sorted(suffixArray , key = lambda x:(x.rank[0] , x.rank[1]))
    k = 4
    ind = [0] * n 
    while( k < 2*n):
        rank = 0 
        prevRank = suffixArray[0].rank[0]
        suffixArray[0].rank[0] = rank
       
        ind[suffixArray[0].index] = 0
        for i in range(1,n):

                if (suffixArray[i].rank[0] == prevRank and suffixArray[i].rank[1] == suffixArray[i - 1].rank[1]):
                    prevRank = suffixArray[i].rank[0]
                    suffixArray[i].rank[0] = rank
                else:
                    prevRank = suffixArray[i].rank[0]
                    rank += 1
                    suffixArray[i].rank[0] = rank
                ind[suffixArray[i].index] = i   
        for i in range(n):
            nextindex = suffixArray[i].index + k // 2
            suffixArray[i].rank[1] = suffixArray[ind[nextindex]].rank[0] if (nextindex < n) else -1
        suffixArray = sorted(suffixArray , key = lambda x:(x.rank[0] , x.rank[1]))
        k = k * 2
    suffixArr = [0] * n
     
    for i in range(n):
        suffixArr[i] = suffixArray[i].index
 
    # Return the suffix array
    return suffixArr
def printArr(arr, n):
	
	for i in range(n):
		print(arr[i], end = " ")
		
	print()
def reformSuffixArray(txt):
    
    suffixArray= buildSuffixArray(txt)
    
    rebuiltArray=[""]*len(suffixArray)
    for x in suffixArray:
        rebuiltArray[suffixArray.index(x)]= txt[x:]
    print(rebuiltArray)
    return rebuiltArray
def lcp(txt):
   
    suffixArray = buildSuffixArray(txt)
    lcpArray = [0]*len(txt)
    phi= [-1]*len(suffixArray)
    phi[suffixArray[0]]=-1
    pclp = [-1]*len(txt)
    for i in range(1,len(suffixArray)):
        phi[suffixArray[i]]=suffixArray[i-1]
    l = 0   
    for i in range( len(txt)- 1 ):
        
        if (phi[i] == -1):
            pclp[i]= 0 
        while(txt[i + l] == txt[phi[i] + l ]):
            l +=1
        pclp[i] = l
        l = max(l-1 , 0 )
    for i in range(len(txt) - 1):
        lcpArray[i] = pclp[suffixArray[i]]
    lcpArray = lcpArray[1:]
    return lcpArray ,  suffixArray 
        
if __name__ == "__main__":
     
    txt = "banana"
    n = len(txt)
     
    lcpArray , suffixArr = lcp(txt)
     
    print("Following is suffix array for", txt)
     
    printArr(suffixArr, n)
    
    
    

def longestCommonPrefix( strs) :

    prefixSf= strs[0]
    print(prefixSf)
    for i in range(1,len(strs)):
            
            while(strs[i].find(prefixSf) != 0):
                
                    prefixSf = prefixSf[:len(prefixSf)-1]
                    print(prefixSf)
              
       
            
    return prefixSf


  