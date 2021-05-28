import math
#####################ITERATIVE METHOD###############################################################
def binarySearch(arr,ele):
    index=0
    right_index=len(arr) - 1

    while(index<=right_index):
        print(f"{right_index} + {index} ")
       
        midIndex=math.floor((right_index+index)/2)
        print(midIndex)
        midEle=arr[midIndex]
        print(midEle)
        if ele == midEle:
            return "Found at index " +str(midIndex)
        if midEle < ele:
            index=midIndex+1
            
        if midEle > ele:
            right_index=midIndex-1
    return "Not Found"
array=[1,5,6,7,8,10,50,55]
#print(binarySearch(array,int(input())))
#####################ITERATIVE METHOD###############################################################
#####################REcursive METHOD###############################################################


def recursiveBs(arr,ele,l,r):
     midIndex=math.floor((l+r)/2)
  
     midEle=arr[midIndex]
     print(midEle)
     if (l>r):
         return "not  found"
     elif ele == midEle:
           
            return "Found at "+str(midIndex)
     elif midEle < ele:
       return recursiveBs(arr,ele,midIndex+1,r)
        
     else:
       return recursiveBs(arr,ele,l,midIndex-1)
#####################REcursive METHOD###############################################################  
print(recursiveBs(array,int(input()),0,len(array)-1))