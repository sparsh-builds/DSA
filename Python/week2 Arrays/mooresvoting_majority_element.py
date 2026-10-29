#
# Moore’s Voting Algorithm is a classical algorithm used to find the majority element (appearing more than ⌊n/2⌋ times) in an array. It works in a single pass by maintaining a candidate and a counter, making it highly efficient in both time and space.

# Illustration:


def mooresvoting(arr):
    count = 0
    cand = 0
    for num in arr:
        # new candidate
        if count == 0:
            cand = num  
        # vote count
        
        count += 1 if num == cand else -1
    return cand

if __name__ == "__main__":
    arr = [1,1,1,2,3]  # Sorted Hai 
    print(mooresvoting(arr))  # Output: 4  # find majjorty element and ot its frequency 