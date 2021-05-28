"""
n_inputs= input()
n = len(n_inputs)
list_num = []
k = input()
index = 0
while index < n - 1:
    sev = ""
    flag=False
    while not n_inputs[index].isspace():
        sev =sev + n_inputs[index]
        
        index=index+1
        flag= True
        if index == n-1:
            sev =sev + n_inputs[index]
            break
    if sev != "":    
        list_num.append(sev)
    if not flag:
        index=index+1
for index , char  in enumerate(list_num):
    if char ==k :
        print(index)
        break

listNum=  n_inputs.split()
print(listNum)

##################################
tc = int(input())
for _ in range(tc):
    s= input()
    a=s.count("ab")
    b=s.count("bc")
    print(f"SUVO = {a}, SUVOJIT = {b}")
#########################################################

n = int(input())
list_vaal=[]
for _ in range(n):
    list_vaal.append(input())
list_vaal2=[""]*len(list_vaal)
list3=[""]*len(list_vaal)
index=0
while index < len(list_vaal) - 1:
       x = list_vaal[index]
       if x not in  list_vaal2:
           list_vaal2[index] = x 
           list3[index]="OK"
           index+=1
       else:
           if x[-1].isdigit():
               y = int(x[-1])+1
               x2= x+f"{y}"
               list_vaal[index] = x2
               list_vaal2[index] = x2
               list3[index]=x2
               index+=1
           else:
               x2= x+"1"
            
               list_vaal[index] = x2
               list_vaal2[index] = x2
               list3[index]=x2
               index+=1
#print("#######################")
for x in list3:
    print(x)


############################################################################## 
array=[i for i in range(10)]
print(array)

def find_max_two_sum(array):
    max1 , max2 = -1 ,-1
    for x in array:
        if x > max1:
            max2=max1
            max1 = x
            
    return max1+max2
def process_array(array):
    count=0
    endSum = find_max_two_sum(array)
    totalArray= set([i**3 for i in range(1, endSum+1)] + [i**2 for i in range(1, endSum+1)])
    totalArray= sorted(totalArray)
    for ele in totalArray:
        for y in array:
            val = ele - y
            if  val < 0 or val not in array:
                continue
            if val == y :
                continue
            if val in array:
                count+=1

    print(count//2)
def paris(a):
    possible_magic={**{i**2:0 for i in range(1,13)},**{i**3:0 for i in range(1,13)}}
    print(possible_magic)
    number_dict={}
    for i in a:
        if  i in number_dict:
            number_dict[i]+=1
            continue
        number_dict[i]=1
    print(number_dict)
    net=0
    for i in possible_magic:
        
        for num,count in number_dict.items():
            value=i-num
            if value<0 or value not in number_dict:
                continue
            if value==num:
                net+=(count-1)*count
                print("is it")
                continue
            net+=count*number_dict[value]
            print(net)
    print(round(net//2))

array = [int(i) for i in input().split()]
paris(array)
#######################################################################

nums = input().split()
rows , colums = int(nums[0]) , int(nums[1])
matrix1=[[1] * colums] * rows
inputMatrix= []
for _ in  range(rows):
    inputMatrix.append([int(i) for i in input().split()])
for rowIndex , row  in enumerate(inputMatrix):
     for columIndex , val in enumerate(row) :
         if val == 0:
             matrix1[rowIndex] = [0]*colums
             for j in range(rows):
                 matrix1[j][columIndex] = 0

def check() :             
    for rowIndex , row  in enumerate(inputMatrix):
        for columIndex , val in enumerate(row) :
            if val == 1:
                dic=[]
                for j in range(rows):
                    dic.append(matrix1[j][columIndex])
                if 1 not in matrix1[rowIndex] and 1 not in dic:
                    return "NO"
               
    return "YES"
                
                
                
checkVal = check()
if checkVal =="NO":
    print("NO")
else:
    print("YES")
    for row in matrix1:
        print(" ".join(str(x) for x in row))
###################################################
n = int(input())  
array= [int(i) for i in input().split()]
nq= int(input())
nql = []
for _ in range(nq):
    nql.append([int(i) for i in input().split()])
ansL=[-1]*n
ansL[0]= array[0]

for i in range(1 , n):
    ansL[i] = ansL[i-1]+ array[i]
   
def sumQuery(query):
      if query[0] != 0:
        upper , lower  = query[0]-1 , query[1]
        return ansL[lower] - ansL[upper]
      return ansL[query[1]]
for x in nql :
    print(sumQuery(x))
#######################
tc = int(input())
for _ in range(tc):
    n = int(input())
    array = [int(i) for i in input().split()]
    array2=[-12333]*n
    array2[0] =array[0]
    for i in range(1,n):
        if array[i] != -1:
            array2[i] = array2[i-1]+array[i]
        else:
            
            array[i] = array2[i-1] // i 
            array2[i] = array2[i-1]+  array[i] 
    print(array)
#########################################

# A optimized school method based
# Python3 program to check
# if a number is prime


def isPrime(n) :

	# Corner cases
	if (n <= 1) :
		return False
	if (n <= 3) :
		return True

	# This is checked so that we can skip
	# middle five numbers in below loop
	if (n % 2 == 0 or n % 3 == 0) :
		return False

	i = 5
	while(i * i <= n) :
		if (n % i == 0 or n % (i + 2) == 0) :
			return False
		i = i + 6

	return True


	
	


tc = int(input())
testCases=[] 
for _ in range(tc):
    testCases.append([int(i) for i in input().split()])
def callCheck(x):
    if x[0] !=0 :
        return array[x[1]] - array[x[0]]
    return array[x[1]]
array = [0]*1000001
for i in range(1, 1000001):
   
    midVal=0
    for x in str(i):
        midVal += int(x)
    
    if isPrime(midVal) and isPrime(i):
        array[i] = array[i-1]+1
    else:
        array[i] = array[i-1]
for x in testCases:
    print(callCheck(x)) 
"""
data =  [int(i) for i in input().split()]
stl , points =  data[0], data[1]
lights=[]
array=[1]*(points+1)
for _ in range(stl):
    lights.append([int(i) for i in input().split()])
if stl == 0:
    print(points+1)
    exit()
for light in lights:
    
    upper , lower = 0 if light[0]- light[1] < 0 else  light[0]- light[1] , light[0] + light[1] if  light[0] + light[1] < points else points
    
    for i in range(upper , lower+1): 
        
        array[i] = array[i] -1

count =0 
index = 0
endPoint=0
startpoint=0

while index < len(array):
      if array[index] == 0  and startpoint == 0:
            continue
      elif array[index] == 1 or array[index] < 0 and startpoint == 0:
       
          startpoint = index
      elif array[index] == 0 and startpoint != 0 and  array[index-1] != 0:
          startpoint = index +1
          endPoint = index + 1
          count+=1
      elif array[index] == 1  or array[index] < 0  and startpoint !=0:
          endPoint = index
      index=index+1

if  count ==  0:
    count = len(array)
print(count)    
      