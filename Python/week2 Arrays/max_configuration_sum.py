# current_val = 0
# for i in range(len(arr)):
#     current_val += i * arr[i]

class Solution:
    def maxSum(self, arr): 
        # Code here
        
        n = len(arr)
        
        if n==0:
            return 0
        
        
        total_sum=sum(arr)
        
        current_val = sum(i * val  for i,val in enumerate(arr))
        
        max_val =current_val 
        
        for i in range(1,n):
            current_val = current_val + total_sum - n*arr[n-i]
            
            if current_val > max_val :
                max_val = current_val
        return max_val
        
        
        
