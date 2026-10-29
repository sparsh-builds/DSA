class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        
        
        arr.sort()
        
        min_no=min(arr)
        
        for num in arr:
            if num > min_no:
                return [min_no,num]
            
            
        return [-1]
    
    
# also 


first =second =arr[0]

for num in arr:
    if num < first:
        second = first
        first = num
    elif first < num < second:
        second = num

return [first, second]