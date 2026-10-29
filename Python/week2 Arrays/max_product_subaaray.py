class Solution:
	def maxProduct(self,arr):
		# code here
		
		n= len(arr)
		res = arr[0]
		
		prefix =1
		suffix =1
		
        
        
        for i in range(n):
            
            if prefix==0:
                prefix =1
            if suffix==0:
                suffix =1 
                
            
            
            prefix*=arr[i]
            
            suffix*=arr[n-i-1]
            
            res =max(res,max(prefix , suffix))
            
        return res