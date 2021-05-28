import math
import itertools 
from fpdf import FPDF 
import sys
import time

sys.setrecursionlimit(10000)
list_names=[]
p_a= ["A","P"]
count=0
def checkString(val):
    st=0
    
    for winen in range(len(val)):
           while(winen - st < 2):

               if val[st:winen+1]=="AA":
                   return False
                   
               else:
                    st=+1
    return True
        
def solve(tillString , n):
    global list_names
    global count
    if n == 0 :
        if "AA" not in tillString:
             list_names.append(tillString)
             print(tillString)
             print(tillString[-1])
             if tillString[-1]=="A":
                 count+=1

        return 
    for i in p_a:
         #print(n)
         val= tillString + i
         solve(val , n-1)
def s(n):
    seta=["A","P"]
    comb=list(itertools.combinations(seta,n))
    print(comb)
#print(solve("",3))
#print(f"{len(list_names)}/{count}")

    

def s2(N):
    edge = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]
    count={}
    for i in range(1,N+1):
         count[str(i)] =[0,-1] 
    for i in edge:
        x=i[0]
        y=i[1]
        print(i)
        for j in range(edge.index(i),len(edge)):
            if y == edge[j][0]:
                if str(x) in count.keys():
                    count[str(x)][0] =count[str(x)][0]+1
                else:
                   count[str(x)][0] =0 
                   count[str(x)][0] = count[str(x)][0]+1
                y=edge[j][1]
                count[str(x)][1]=y
            print(count)
       
        max1=max(count.values())
        
        list_map=[0]*(N)
        print(list_map)
        for x in count.keys():
            if count[str(x)][0]==max1[0]:
                list_map[int(x)-1]=1
                list_map[int(count[str(x)][1])-1]=1
                for y in count.keys():
                    if count[str(y)][1]==count[str(count[str(x)][1])][1]:
                         list_map[int(count[str(y)][1])-1]=1
    return list_map
def dfs(root, adj_list,visited,maxLen):#O(N)
    global length
    if maxLen:
        
        if root not in visited: 
            length = length+1
            visited.add(root)
            for node in adj_list[root]:

                dfs(node,adj_list,visited,maxLen)
    else:
        
        if root not in visited : 
            length = length+1
            visited.add(root)
            for node in adj_list[root]:
                if node >= root:
                    dfs(node,adj_list,visited,maxLen)
    
length=0
def se3(N):
    edge = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]
    adj_list={}
    
    for x in range(1,N+1): #O(N)
        adj_list[x]=[]
    for x in edge:
        adj_list[x[0]].append(x[1])
        adj_list[x[1]].append(x[0])
    print(adj_list)
    visited=set()
    print(dfs(6,adj_list,visited,False))
    print(length)
    
N=1000
cacheX=[1]*(N)
def fact(n):
    if n==1 :
        return 1
    print(n)
    if cacheX[n-1] == 1 :
        cacheX[n-1]=n*fact(n-1)
    return cacheX[n-1]



def ncr(n,r):
    if n<r:
        return 0
    fact(n)
    mode=10**9+7
    x=cacheX[n-1]//(cacheX[r-1]*cacheX[(n-r)-1])
    return x%mode

print(ncr(1000,116)) 

def binomialCoeff(n, k):
 
    # Declaring an empty array
    C = [0 for i in range(k+1)]
    C[0] = 1  # since nC0 is 1
 
    for i in range(1, n+1):
 
        # Compute next row of pascal triangle using
        # the previous row
        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j-1]
            j -= 1
    mode=10**9+7
    return C[k]%mode
start_time = time.time()
print(binomialCoeff(1000,116))
print("--- %s seconds one ---" % float(time.time() - start_time))