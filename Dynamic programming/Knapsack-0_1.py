#####################################BruteForce#########################################
def start_process(w,p,c,dyna):
    if dyna:
        dp_arr=[[-1 for _ in range (c+1)] for _ in range (len(w))]
        return dyKnapScak(w,p,c,0,dp_arr)
    else:
      return knapScak(w,p,c,0)
def knapScak(w,p,c,ci):
    profit1=0
    if ci>=len(p) or c <=0:
        return 0
    if w[ci]<=c:
        profit1=p[ci]+knapScak(w,p,c-w[ci],ci+1)
    profit2=knapScak(w,p,c,ci+1)
    return max(profit1,profit2)


###########################################BruteForce########################################
#########################################Dynamic Approach########################################
def dyKnapScak(w,p,c,ci,dp_arr):
    profit1=0
    if  c <=0 or ci>=len(p):
        return 0
    if dp_arr[ci][c] != -1:
        return dp_arr[ci][c]
    if w[ci]<= c :

        profit1=p[ci]+dyKnapScak(w,p,c-w[ci],ci+1,dp_arr)
    profit2=dyKnapScak(w,p,c,ci+1,dp_arr)
    profit=max(profit1,profit2)
    dp_arr[ci][c]=profit
    return dp_arr[ci][c]
###########################################Dynamic Approach########################################
print(start_process([1,2,3,5],[1,6,10,16],7,True))