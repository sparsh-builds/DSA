import math




class Solution:
    def median(self, arr):
        # code here
        n=len(arr)
        
        arr.sort()
        
        mid =n//2
        if n % 2!=0:
            return arr[mid]
        else:
            return (arr[mid-1] + arr[mid])//2
    def mean(self, arr):
        # code here
        
        return sum(arr)//len(arr)
    
    
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    obj = Solution()
    print(obj.median(arr))
    print(obj.mean(arr))