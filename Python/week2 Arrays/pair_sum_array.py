class Solution:
    def constructArr(self, arr):
        # code here
        
        
        m = len(arr)
        
        res =[]
        
        n =int((1 + math.sqrt(1+8*m))/2)
        
        if n<=2:
            return [1,arr[0]-1]
            
        res=[0]*n
        
        res[0]=(arr[0]+arr[1]-arr[n-1])//2
        
        for i in range(1,n):
            res[i]=arr[i-1]-res[0]
            
        return res
    
