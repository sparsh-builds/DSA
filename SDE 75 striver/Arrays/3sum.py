def method1(nums):
    st = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    st.add(triplet)
    return [list(triplet) for triplet in st]


def method2(nums): # Using Hashmap
    ans =set()
    # Sort the array to handle duplicates and for easier triplet formation
    for i in range(len(nums)):
            # Set to store elements seen in this iteration
            hashset = set()

            # Second loop for second element
            for j in range(i + 1, len(nums)):
                
                # Calculate third element needed
                third = -(nums[i] + nums[j])

                # If third already in set, we found a triplet
                if third in hashset:
                    triplet = tuple(sorted([nums[i], nums[j], third]))
                    ans.add(triplet)

                # Add current element to set
                hashset.add(nums[j])
                
    return [list(triplet) for triplet in ans]

def method3(nums): # Using Two Pointers
    ans =[]
    nums.sort()  # Sort the array to use two pointers
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
                continue
        
        
        left, right = i + 1, len(nums) - 1
        while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
    return ans