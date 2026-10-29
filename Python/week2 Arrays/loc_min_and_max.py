class Solution:
    def extractPoints(self, arr):
        # code here
        
        n=len(arr)
        
        if n<=2:
            if arr[0]==arr[1]:
                return [arr[0]]
            return arr
            
        
        res =[]
        
        
        res.append(arr[0])
        
        prev_diff =0 
        
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            
            if diff ==0:
                continue
            if prev_diff*diff<0:
                res.append(arr[i])
                
            prev_diff =diff 
        res.append(arr[n-1])
        
        return res
        
        
