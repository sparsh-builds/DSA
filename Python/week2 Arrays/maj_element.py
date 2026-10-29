from collections import Counter


class Solution:
    def majorityElement(self, arr):
        
        
        freq = Counter(arr)
    
    
        for key , val in freq.items():
        
            if val > len(arr)//2:
                return key
        return -1 
    