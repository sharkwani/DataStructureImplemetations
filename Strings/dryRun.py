from typing import Deque
from itertools  import permutations
import re
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
        print(len(arr) , end  =" ")
        
        for i in range(n):
                print(arr[i], end = " ")
		
	    
def reformSuffixArray(txt):
    
    suffixArray= buildSuffixArray(txt)
    
    rebuiltArray=[""]*len(suffixArray)
    for x in suffixArray:
        rebuiltArray[suffixArray.index(x)]= txt[x:]
    print(rebuiltArray)
    return rebuiltArray
def lcp(txt):
    print(len(txt))
    suffixArray = buildSuffixArray(txt)
   
    #suffixArray.appendleft(len(txt))
    print(suffixArray)
    lcpArray = [0]*len(txt)
    phi= [-1]*len(txt)
    phi[suffixArray[0]]=-1
    pclp = [-1]*len(txt)
    for i in range(1,len(txt)):
        phi[suffixArray[i]]=suffixArray[i-1]
    print(phi)
    l = 0   
    for i in range(len(txt)-1 ): # put -1 if extra symbol is present at the end of input 
        print(f" i + l ======> {i+l}"  )
        print(f" phii + l ======>   { phi[i] + l}")
        if (phi[i] == -1):
            pclp[i]= 0 
        while( txt[i + l] == txt[phi[i] + l ]):
            l = l + 1
            if phi[i] + l == len(txt) :
               break
        
           
            
        pclp[i] = l
        l = max(l-1 , 0 )
    for i in range(len(txt) - 1):
        lcpArray[i] = pclp[suffixArray[i]]
    lcpArray= lcpArray[1:]
    print(lcpArray)
def readTxtLineByLine(fileName):
   with open(fileName)as tempFile:
    string=''
    while True:
        line= tempFile.readline()
        if not line:
            break
        if line[0].strip()==".":
            print(line[:7])
            if line[:7] ==".......":
                continue
            else:
                     string = string + " " + line.strip()  
                
        else:
            string = string + " " + line.strip()
        print(string)
        
    
def isSubstring(findTxt ,txt):
    val = txt.find(findTxt)
    if  val != -1:
        return val 
    return val

def isSubstringMulValues(findTxt ,txt):
    indexes= [  i.start() for i in re.finditer(findTxt,txt) ]
            
    return indexes
def calCharac(text):
    listTxt=list(text)
    string=""
    vovels=0
    numbers=0
    consonants=0
    for i in range(len(text)):
        if text[i] in ["a", "e", "i" , "o" , "u" ,"A","E","I","O", "U"]:
            
            vovels+=1
        elif text[i].isnumeric():
            numbers +=1
        else:
            consonants+=1
         
        listTxt[i] = listTxt[i].lower()
          
    loweCaseString =string.join(listTxt)
    print(vovels)
    print(numbers)
    print(consonants)
        
        
def reverseString(s):
       
        lenStr= len(s)
        p1=0
        p2= lenStr-1
        
        while(p1 < p2):
               
                
                temp = s[p1]
                s[p1]=s[p2]
                s[p2]=temp
                
                p2-=1
                p1+=1
                
def chkIfAr1IsRo(arr1 , arr2):
    indexOfFirst= arr2.index(arr1[0])
    lenArr1=len(arr1)
    lenArr2= len(arr2)
    if lenArr1!=lenArr2 or lenArr1 == 0  or lenArr2 == 0:
        return False
    
    i =0
    while(lenArr1 != i+1):
        print(f"again {indexOfFirst}")
        if arr2[indexOfFirst]==arr1[i]:
           
            indexOfFirst = (indexOfFirst+1) % len(arr2) 
            i+=1
        else:
            return False
    return True
def postProcess(val):
    if len(val)==1:
        return "1"+val
    strt=0 
    end = 1
    string= ""
    
    while end < len (val):
        
    
        if  val[strt] == val[end]:
            end = end + 1 
            if end == len(val):
                string=string+f"{end - strt }{val[end-1]}"
                
        
        else:
                
                string=string+f"{end - strt }{val[end-1]}"
                strt= end 
                end= end + 1
                if end == len(val):
                     string=string+f"{end - strt }{val[end-1]}"
            
    print(string)        
    return string        
        
    
def countAndSay(n):
     if n == 1:
         return "1"
     if n > 1:
         val = countAndSay(n-1)
        
         return postProcess(val)
def checkPalindrome(txt):
    if  len(txt) == 1 :
        return True
    if len(txt) == 0:
        return False
    
    p1=0
    p2= len(txt) -1 
    while(p2> p1):
        print(p1)
        print(p2)
        if txt[p1] == txt[p2]:
            p1=p1+1
            p2=p2-1
        else:
            return False 
    return True 
def check_longest_palindrome(txt):
      p2=len(txt)
      maxValue=0
      stringTo=""
      for i in range(p2):
          
          for j in range(p2-1 , i-1 , -1):
              print(txt[i:j+1])
              flag =checkPalindrome(txt[i:j+1])
              print(flag)
              if flag:
                  flagLen = len(txt[i:j+1])        #     ABC        "A"    
                  if maxValue < flagLen:                # B
                      maxValue = flagLen
                      stringTo=txt[i:j+1]
     
      return stringTo

def call_permute(string , strsf , lstOfStrings ,lenOfOriginalString ):
      
      if len(string) <= 1:
          strsf+=string[0]
          lstOfStrings.append(strsf)
          print(lstOfStrings)
          
          return lstOfStrings
      for i in range(len(string)-1):
          print(f"{i} -------------> {string}")
          strsfc = strsf + string[i]
          print("complete =->"+strsf)
          nextString = string[:i]+string[i+1:]
          call_permute(string , strsfc , lstOfStrings , lenOfOriginalString)
         
          print(f"{i} -------enede------> {string}")
lst=[]        
def dartCopyStringPermutations(string , strsf , strLen):
  
    if  len(string) <=1 :
        print(strsf)
        lst.append(strsf+string[0]) 
  
    lenStr =  len(string)
    for i in range(lenStr-1): 
        x = strsf + string[i]
        nxtStr=    string[:i]+string[i+1:]
        print(nxtStr)
        dartCopyStringPermutations(nxtStr , x , strLen) 
def findPermutations(string , strsf):
    if len(string) == 1:
        strsf += string[0]
        print(strsf)
    else:
        lenStr = len(string)
        i= 0
        while i < lenStr -1 :
            print(i)
            x = strsf + string[i]
            nextString = string[:i]+string[i+1:]
            
            findPermutations(nextString , x)
            print("yello ")
            i+=1
            
        
        
        
        
def find_permutation(S):
    lstOfStrings=[]
    lstOfStrings = call_permute(S , "" , lstOfStrings ,len(S))  
    #dartCopyStringPermutations(S , ""  ,len(S))
    return lst 
def permute(string):
    listl = list(permutations(string))
    list2=[]
    for x in listl:
        string="".join(list(x))
        
        list2.append(string)
    list2=sorted(list2)
    
    return list2

def findBinaryStr(string):
    start = 0
    end= start+1
    countx=0
    while(end <= len(string) - 1):
        listq = list(string[start : end+1])
       
        count0=listq.count("0")
        count1=listq.count("1")
    
        if count1 == count0:
            countx += 1
            end += 2
            start = end-1
        else:
            end += 1
    if countx != 0:
        return countx
    else:
        return -1
def decryptPassword(s):
    # Write your code here
    lenStr= len(s)
    sx=list(s)
    xs=[""]*lenStr
    index2= 0 
    mapc={}
    for index , char in  enumerate(sx):
        if char == "0":
            mapc[index] = "+"
   
    while index2 <= lenStr -1 :
       
        if s[index2] == "*":
            sx[index2-1] = s[index2-2]
            sx[index2-2]  = s[index2-1]
            sx[index2]=""
            index2+=1
        elif s[index2].isdigit() and s[index2] != "0":
            char = s[index2]
            
            for key in sorted(mapc.keys()):
                
                sx[key]=char
            mapc.pop(key)
            sx[index2]=""
            index2+=1
        else:
            index2+=1
    return "".join(sx)
if __name__ == "__main__":
     
    #txt = input()
    #n = len(txt)
     
    #suffixArr = lcp(txt)
    
    #readTxtLineByLine("C:\\Users\\LENOVO\\Desktop\\dummyFile.txt")
    s1 = "AeIou123cdfg"
    s2 = "Ilove"
    s3= list(s2)
    print(len(s3) - 1 - s3[::-1].index("e"))
    #res = isSubstringMulValues(s1, s2)
    #print(res)
     
    #calCharac("AeIou123cdfg")
    #reverseString(['h', 'e', 'l', 'l'/, 'o'])
  
   # print(chkIfAr1IsRo("ABCD", "CADB"))
    #print(countAndSay(6))    51Pa*0Lp*0e aP1pL5e
   
    
    #print(check_longest_palindrome("rfkqyuqfjkxy"))

    #print(findPermutations("ABC" ,""))
   #print(permute("jlr"))

   
   
    