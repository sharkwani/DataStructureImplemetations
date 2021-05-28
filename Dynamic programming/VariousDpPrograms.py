##############################################################################################################################################################
"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of
elements in both subsets is equal.

Input: {1, 2, 3, 4}
Output: True
Explanation: The  given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
"""
def startProcessing(arr,index,dp,sumVal=0):
    val=sum(arr)
    if index ==0 :
       
        if val % 2 != 0:
            return False
        if dp:
            pass
        else:
            return  findPartition(arr, val/2 , 0)
    elif index == 1 :
        if dp:
            dp_table=[[-1]* int(sumVal+1) for _ in range(len(arr))]
            return subSetDp(arr, sumVal , 0 , dp_table)
        else:
             return subSet(arr,sumVal,0)
def findPartition(arr, sumVal , ci):
    weight = sumVal
    if weight  == 0 :
        return True

    if ci >= len(arr) or len(arr) == 0:
        return False
    
    if arr[ci] <= weight:
        if(findPartition(arr , weight-arr[ci],ci+1)):
            return True
    return findPartition(arr,weight,ci+1)

##############################################################################################################################################################
"""
Count of Subset Sum (hard) 

Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
Example 1: #

Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
"""
#############################RECURSIVE#############################################################################
def subSet(arr,sumVal,ci):
    if sumVal == 0:
        return 1
    if len(arr) == 0 or ci >= len(arr):
         return 0 
    x=0 
    if arr[ci] <=sumVal:
        x=subSet(arr,sumVal-arr[ci],ci+1)
    y=subSet(arr,sumVal,ci+1)
    return x + y 
#############################RECURSIVE#############################################################################
#############################DP#############################################################################

def subSetDp(arr,sumVal,ci,dp_table):
    x=0
    if sumVal == 0:
        return 1
    if len(arr) == 0 or ci >= len(arr):
         return 0 
    if dp_table[ci][sumVal] == -1:
         if arr[ci] <=sumVal:
            x=subSetDp(arr,sumVal-arr[ci],ci+1,dp_table)
         y=subSetDp(arr,sumVal,ci+1,dp_table)
         dp_table[ci][sumVal] = x + y  
             
    return dp_table[ci][sumVal]
#############################DP#############################################################################



print(startProcessing([1,1,2,3],1,True,4))
#############################################################################################################################################