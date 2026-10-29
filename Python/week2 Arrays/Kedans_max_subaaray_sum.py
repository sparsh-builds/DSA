#Kadane’s Algorithm is a classical algorithm used to find the maximum sum of a contiguous subarray in linear time (O(n)). It works by maintaining a current sum and updating the maximum sum found so far during a single pass through the array.




def maxSubarraySum(arr):
    
    # Stores the result (maximum sum found so far)
    res = arr[0]
    
    # Maximum sum of subarray ending at current position
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Either extend the previous subarray or start 
        # new from current element
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update result if the new subarray sum is larger
        res = max(res, maxEnding)
    
    return res