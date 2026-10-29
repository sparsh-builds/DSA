from collections import Counter


class Solution:
    def findTwoElement(self, arr):
        n=len(arr)
        counts =[0] * (n+1)
        
        missing =-1
        repaeting =-1
        
        for num in arr:
            counts[num]+=1
            
        for i in range(1,n+1):
            if counts[i]==2:
                repeating =i
            elif counts[i]==0:
                missing =i
        return [repeating , missing]
        
