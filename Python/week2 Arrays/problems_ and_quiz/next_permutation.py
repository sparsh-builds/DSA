class Solution:
    def nextPermutation(self, arr):
        # code here
        
        
        n= len(arr)
        
        i=n-2
        
        while i >=0 and arr[i]>=arr[i+1]:
            i-=1
        
        if i>=0:
            j=n-1
            while arr[j]<=arr[i]:
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
        
        arr[i+1 :] =reversed(arr[i+1:])
    
        return arr
    
if __name__=="__main__":
    arr=[1,2,3]
    sol=Solution()
    print(sol.nextPermutation(arr))  # Output: [1, 3, 2]