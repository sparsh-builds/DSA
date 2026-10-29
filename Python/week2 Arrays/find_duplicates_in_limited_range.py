# find repeaetd elemets in a iimited range and imited repetition


# Method 1 O(n^2)


def findDuplicates(arr) :
    ans = []

    # traverse each element in the array
    for  i in range(len(arr)):
        cnt = 0

        # check if element is already added to result
        for it in ans :
            if arr[i] == it:
                cnt+=1
                break
            
        

        # if already added, skip checking again
        if cnt : # means if cnt>0
            continue

        # check if current element appears again 
        # in the rest of the array
        for j in range(i+1,len(arr)) :
            if arr[i] == arr[j] :
                cnt+=1
                break
            
        

        # if duplicate found, add to result
        if (cnt > 0):
            ans.append(arr[i])
    

    return ans


# Method 2     O(n) -> freq based and spce -O(n)
def findDuplicateswithfreq(arr):
    
    n = len(arr)
    
    # frequency array with 1-based indexing
    freq = [0] * (n + 1) 
    ans = []

    
    for item in arr:
        freq[item]+=1
        
    for i in range(1,n+1):
        if freq[i]==2:
            ans.append(i)
            
    return ans
# Method 3 negative marking O(n)
def method3(arr):
    
    n=len(arr)
    ans=[]
    
    for i in range(n):
        idx =abs(arr[i])-1
        
        if arr[idx]<0:   #  already visited 
            
            ans.append(abs(arr[i]))
        else:
            arr[idx]=-arr[idx]
            
    return ans
if __name__=="__main__":
    arr=[2,1,2,3,4,3]
    print(findDuplicates(arr))
    print(findDuplicateswithfreq(arr))
    print(method3(arr))