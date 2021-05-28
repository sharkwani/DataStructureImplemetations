def knuthMorrisonPreprocess(pattern , m ):
    fail = [0]*m
    i = 0 
    j= 1
    fail[0]=-1
    while(j < m ):
        if pattern[i] == pattern[j]:
            fail[j]= i+1
            i+=1
            j+=1
        elif i > 0:
            i = fail[i-1]
        else:
            j+=1
    return fail
def knuthMorrisonMatch(txt , pattern):
    n , m = len(txt), len(pattern)
    if m == 0 :  return 0
    fail= knuthMorrisonPreprocess(pattern , m )
    
    i , j = 0,0
    indexes = []
    while(j < n ):
        if pattern[i] == txt[j]:
            if i == m -1:
                
                 indexes.append(j - m + 1)
                 i = 0 
                 j+=1
            else:
                i+=1
                j+=1
        elif i > 0:
            i = fail[i-1]
        else:
            j+=1
    return indexes
print(knuthMorrisonMatch("ababab" , "ab"))










#####################################








def knuthMorrisonPreprocess(pattern , m ):
    fail = [0]*m
    i = 0 
    j= 1
    
    while(j < m ):
        if pattern[i] == pattern[j]:
            fail[j]= i+1
            i+=1
            j+=1
        elif i > 0:
            i = fail[i-1]
        else:
            fail[j]=i
            j+=1
    return fail
def knuthMorrisonMatch( txt , pattern):
    
    n , m = len(txt), len(pattern)
    if m == 0 or n == 0:  return 0
    fail= knuthMorrisonPreprocess(pattern , m )
    count= 0
    i , j = 0,0
    while(j < n ):
        if pattern[i] == txt[j]:
            if i == m - 1:
                 return True
            else:
                i+=1
                j+=1
        elif i > 0:
            i = fail[i-1]
        else:
            j+=1
    return False