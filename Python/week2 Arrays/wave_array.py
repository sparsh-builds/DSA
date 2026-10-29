class Solution:
    def sortInWave(self, arr):
        # code here
        
        i =0
        j=0
        
        while i < len(arr)-1:
            
            j=i+1
            
            if j < len(arr):
                arr[i],arr[j]=arr[j],arr[i]
                
            
            i+=2
        return arr
        