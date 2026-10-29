# Array Rotations is a transformation where the array is rotated k times to the right or left, causing elements to shift cyclically. This operation can be done efficiently in-place.

# To rotate the array, reverse the last k elements, reverse the first n − k elements, and finally reverse the entire array.


# Method 1 O(n*k) and O(k) space


def method1(arr,k):
    n=len(arr)
    if k==0:
        return arr
    
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    
    if k>0:
        method1(arr,k-1)
        
    return arr

# method2 O(n) and O(n) space

def  method2(arr,k):
    n=len(arr)
    k=k%n
    temp=[0]*n
    
    for i in range(n):
        if i<k:
            temp[i]=arr[n+i-k]
            
        else:
            temp[i]=arr[i-k]
            
    for i in range(n):
        arr[i]=temp[i]
        
    return arr



    
# Array Rotations is a transformation where the array is rotated k times to the right or left, causing elements to shift cyclically. This operation can be done efficiently in-place.

# To rotate the array, reverse the last k elements, reverse the first n − k elements, and finally reverse the entire array.



def rotateclockwise(arr, k):
    n = len(arr)
    if n == 0:
        return

    k = k % n

    # Reverse last k elements
    arr[n - k:] = reversed(arr[n - k:])

    # Reverse first n-k elements
    arr[:n - k] = reversed(arr[:n - k])

    # Reverse the entire array
    arr[:] = reversed(arr)

    # No return — modifies arr in-place
    



# [1,2,3,4,5]  => [4,5,1,2,3]  k=2 as 2 positions to the right 1 step -> 5.4  2nd step 3,2,1 3rd step -> 4,5,1,2,3


# also [5,4,3,2,1]=> 4,5 and 1,2,3

# for left rotation we can use the same logic but with k=n-k
def method3(arr,k):  # O(n) and O(1) space
    n=len(arr)
    k=k%n
    arr[:n-k]=reversed(arr[:n-k])
    
    arr[n-k:]= reversed(arr[n-k:])
    
    arr[:] =reversed(arr)
    
    return arr

if __name__=="__main__":
    arr=[1,2,3,4,5]
    arr2=[1,2,3,4,5]
    arr3=[1,2,3,4,5]
    k=2
    print(method1(arr,k))
    print(method2(arr2,k))
    print(method3(arr3,k))
        
        
3 Ques

class Solution:
    def rotateclockwise(self, arr, k):
        # code here
        k=k%len(arr)
        arr[:] =reversed(arr[:])
        
        arr[:k] =reversed(arr[:k])
        
        arr[k:] =reversed(arr[k:])
        
        return arr
        
        
#