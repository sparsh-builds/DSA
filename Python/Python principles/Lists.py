# Python Lists

# comments
# In Python, a list is a built-in data structure that can hold an ordered collection of items. Unlike arrays in some languages, Python lists are very flexible:

# Can contain duplicate items
# Mutable: items can be modified, replaced, or removed
# Ordered: maintains the order in which items are added
# Index-based: items are accessed using their position (starting from 0)
# Can store mixed data types (integers, strings, booleans, even other lists)
# Creating a List
# Lists can be created in several ways, such as using square brackets, the list() constructor or by repeating elements. Let's look at each method one by one with example:

# 1. Using Square Brackets
# We use square brackets [] to create a list directly.




a = [1, 2, 3, 4, 5] # List of integers 
b = ['apple', 'banana', 'cherry'] # List of strings 
c = [1, 'hello', 3.14, True] # Mixed data types 
print(a) 
print(b) 
print(c)

a = list((1, 2, 3, 'apple', 4.5))   # USing LIst  COntainer
print(a) 
b = list("GFG") 
print(b)

a = [2] * 5 
b = [0] * 7 
print(a) 
print(b)  #  WIth repeatative 

a = [10, 20, 30, 40, 50] 
print(a[0]) 
print(a[-1]) 
print(a[1:4]) # elements from index 1 to 3

a = [] 
a.append(10) 
print("After append(10):", a) 
a.insert(0, 5) 
print("After insert(0, 5):", a) 
a.extend([15, 20, 25]) 
print("After extend([15, 20, 25]):", a) 
a.clear() 
print("After clear():", a)

a = [10, 20, 30, 40, 50]   # Updating 
a[1] = 25 
a[1:3]=[3.4]
print(a)

a = [10, 20, 30, 40, 50] 
a.remove(30) 
print("After remove(30):", a) 
popped_val = a.pop(1) # remove last emenet a.pop()
print("Popped element:", popped_val) 
print("After pop(1):", a) 
del a[0] 
print("After del a[0]:", a)

a = ['apple', 'banana', 'cherry'] 
for item in a: 
    print(item)
    if item == 'banana': 
        a.remove(item)  # Remove the item from the list
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 
print(matrix[1][2])

squares = [x**2 for x in range(1, 6)] 
print(squares)

a = [10, 20, "GfG", 40, True] 
print(a) 
print(a[0]) 
print(a[1]) 
print(a[2])


# List Comprehensions 

rows = len(mat)

cols =len(mat[0])

res = [[0] * cols for _ in range(rows)]


