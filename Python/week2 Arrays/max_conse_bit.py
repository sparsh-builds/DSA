class Solution:
    def maxConsecBits(self, arr):
        #code here 
        
        curr_len=1
        
        max_len=1
        
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                curr_len+=1
                max_len=max(curr_len,max_len)
            else:
                curr_len=1
        return max_len
    
    