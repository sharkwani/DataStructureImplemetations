class practice():
    def cs(self, amount , coins , ci ):
        
        if amount == 0:
            return 1
        if ci>len(coins)-1:
            return 0
        if coins[ci]>amount or amount <0:
            return 0
        
        incl= self.cs(amount-coins[ci],coins,ci)
        excl=self.cs(amount,coins,ci+1)
        return incl+excl
    
amount = 3
coins = [99,1]

obj=practice()
print(obj.cs(amount,coins,0))
cache=[[0 for _ in range(amount+1)] for _ in range(len(coins))]
print(cache)