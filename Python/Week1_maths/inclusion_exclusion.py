# PIE stands for the Principle of Inclusion-Exclusion.

# It is a counting rule used in mathematics and computer science to find the total size of combined sets without counting items that overlap more than once.

class Solution:
    def countDivisible(self, arr, m):
        #code here
        count = 0
        
        primes=list(num for num in set(arr) if num <=m)
        seen =set()  # set 
            
        for num in primes :
            for i in range(num, m+1,num):        
                seen.add(i)
                    
        return len(seen)            
