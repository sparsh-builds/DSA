
# Next Permutation Algorithm is a classical algorithm that rearranges the array into its next lexicographically greater permutation. If such a permutation isn't possible, it rearranges the array into ascending order in-place.

# To find the next permutation, identify the first decreasing element from the right, swap it with the next larger element on its right, then reverse the remaining suffix.

# This algorithm finds the lexicographically next greater permutation of numbers in-place in 
# $O(n)$ time and $O(1)$ extra space.

def nextpermutation(arr):
    n=len(arr) 
    
    i=n-2
    # find 1st dec from right
    
    while i>=0  and arr[i] >= arr[i+1]:
        i-=1
    # if entire array is desc , i will be -1
    if i>=0:
        j=n-1
        while arr[j]<=arr[i]:  # kisse swap krna hai wo find krne k liye next bda element 
            j-=1
            
        arr[i],arr[j] =arr[j],arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    
    
if __name__=="__main__":
    arr=[1,2,3]
    nextpermutation(arr)
    print(arr)  # Output: [1, 3, 2]