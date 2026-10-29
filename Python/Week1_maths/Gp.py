class Solution:
	
	def res( r , n):
	    
	    result =1
	    MOD = (10**9) +7 
	    r = r%MOD
	    
	    if n==0:
	        return 1 
	 
	    while n >0:
	        
	            
	        if n % 2 ==1:
	            result = (result *r) % MOD
	        
	            n-=1
	 
	        r =(r *r) % MOD
	        
    	    n//=2
	    return result
	
	
	def nthTerm(self, a, r, n):
	    
	    
		# code here
		MOD = (10 ** 9) + 7
		
		return (a * (Solution.res(r, n-1)))% MOD