# Classical Algorithm and Problem on 2D-Arrays
# Matrix multiplication is a classical matrix problem where each element of the resulting matrix is calculated as the dot product of a row from the first matrix and a column from the second. It combines two matrices to form a new one based on this rule.

# Core Idea: For C[i][j], sum the product of corresponding elements from row i of matrix A and column j of matrix B: C[i][j] = A[i][0]*B[0][j] + A[i][1] * B[1][j] + ... + A[i][k] * B[k][j]






def multiply(arr, brr):
    n = len(arr)

    # to store the resultant matrix
    res = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += arr[i][k] * brr[k][j]

    return res


if __name__ == "__main__":
    arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    brr = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

    result = multiply(arr, brr)

    for row in result:
        print(row)
        
        
The main idea is to multiply two matrices by following the standard row-by-column multiplication method. For each element in the result matrix, it takes a row from the first matrix and a column from the second matrix, multiplies their corresponding elements, and adds them up to get a single value. This process is repeated for every position in the result matrix.

1-




# Function to add two matrices of same dimensions r×c
def add(mat1, mat2):
    r = len(mat1)
    c = len(mat1[0])
​
    # Initialize result matrix with dimensions r×c
    res = [[0] * c for _ in range(r)]
​
    # Perform element-wise addition
    for i in range(r):
        for j in range(c):
            res[i][j] = mat1[i][j] + mat2[i][j]
​
    return res
​
# Function to multiply mat1 (n×m) with mat2 (m×q)
def multiply(mat1, mat2):
    n = len(mat1)
    m = len(mat1[0])
    q = len(mat2[0])
​
    # Initialize result matrix with dimensions n×q
    res = [[0] * q for _ in range(n)]
​
    # Matrix multiplication logic
    for i in range(n):
        for j in range(q):
            for k in range(m):
                res[i][j] += mat1[i][k] * mat2[k][j]
​
    return res
    
if __name__ == "__main__":
    mat1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    mat2 = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    res = multiply(mat1, mat2)
    
    for row in res:
        print(" ".join(map(str, row)))

Output
58 64 
139 154 
[Approach 3] - Using Strassen's Method
Strassen’s algorithm originally applies to square matrices, but when adapted for multiplying an n*m matrix with an m*q matrix, the matrices are padded to form square matrices of size s*s where s = next power of two ≥ max(n, m, q). The algorithm then performs 7 recursive multiplications on these square blocks.

2
Note: Strassen's Method is often not preferred in practice due to its high constant factors, making the naive method faster for typical applications. It performs poorly with sparse matrices, where specialized algorithms work better. The recursive submatrix divisions require extra memory. Additionally, due to limited precision in floating-point arithmetic, Strassen’s algorithm tends to accumulate more errors than the naive approach.





import math
​
# Return the next power of two greater than or equal to n
def nextPowerOfTwo(n):
    return int(math.pow(2, math.ceil(math.log2(n))))
​
# Resize a matrix to newR x newC and 
# fill extra space with zeros
def resizeMatrix(mat, newR, newC):
    resized = [[0 for _ in range(newC)] for _ in range(newR)]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            resized[i][j] = mat[i][j]
    return resized
​
# Perform matrix addition or subtraction 
# of size×size matrices
# sign = 1 for addition, -1 for subtraction
def add(a, b, size, sign=1):
    res = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            res[i][j] = a[i][j] + sign * b[i][j]
    return res
​
# Recursive implementation of Strassen's 
# matrix multiplication
# Assumes both matrices are size×size 
# and size is a power of 2
def strassen(mat1, mat2):
    n = len(mat1)
​
    # Base case: 1×1 matrix multiplication
    res = [[0 for _ in range(n)] for _ in range(n)]
    if n == 1:
        res[0][0] = mat1[0][0] * mat2[0][0]
        return res
​
    # Split matrices into 4 submatrices
    newSize = n // 2
    a11 = [[0 for _ in range(newSize)] for _ in range(newSize)]
    a12 = [[0 for _ in range(newSize)] for _ in range(newSize)]
    a21 = [[0 for _ in range(newSize)] for _ in range(newSize)]
    a22 = [[0 for _ in range(newSize)] for _ in range(newSize)]
    b11 = [[0 for _ in range(newSize)] for _ in range(newSize)]
    b12 = [[0 for _ in range(newSize)] for _ in range(newSize)]
    b21 = [[0 for _ in range(newSize)] for _ in range(newSize)]
    b22 = [[0 for _ in range(newSize)] for _ in range(newSize)]
​
    # Fill the submatrices
    for i in range(newSize):
        for j in range(newSize):
            a11[i][j] = mat1[i][j]
            a12[i][j] = mat1[i][j + newSize]
            a21[i][j] = mat1[i + newSize][j]
            a22[i][j] = mat1[i + newSize][j + newSize]
            b11[i][j] = mat2[i][j]
            b12[i][j] = mat2[i][j + newSize]
            b21[i][j] = mat2[i + newSize][j]
            b22[i][j] = mat2[i + newSize][j + newSize]
​
    # Compute the 7 products using Strassen’s formulas
    m1 = strassen(add(a11, a22, newSize), add(b11, b22, newSize))
    m2 = strassen(add(a21, a22, newSize), b11)
    m3 = strassen(a11, add(b12, b22, newSize, -1))
    m4 = strassen(a22, add(b21, b11, newSize, -1))
    m5 = strassen(add(a11, a12, newSize), b22)
    m6 = strassen(add(a21, a11, newSize, -1), add(b11, b12, newSize))
    m7 = strassen(add(a12, a22, newSize, -1), add(b21, b22, newSize))
​
    # Calculate result quadrants from m1...m7
    c11 = add(add(m1, m4, newSize), add(m7, m5, newSize, -1), newSize)
    c12 = add(m3, m5, newSize)
    c21 = add(m2, m4, newSize)
    c22 = add(add(m1, m3, newSize), add(m6, m2, newSize, -1), newSize)
​
    # Combine result quadrants into final matrix
    for i in range(newSize):
        for j in range(newSize):
            res[i][j] = c11[i][j]
            res[i][j + newSize] = c12[i][j]
            res[i + newSize][j] = c21[i][j]
            res[i + newSize][j + newSize] = c22[i][j]
​
    return res
​
# Multiply mat1 (n×m) and mat2 (m×q) 
# using Strassen’s method
def multiply(mat1, mat2):
    # Compute size of the smallest power of 2 ≥ max(n, m, q)
    n = len(mat1)
    m = len(mat1[0])
    q = len(mat2[0])
    size = nextPowerOfTwo(max(n, max(m, q)))
​
    # Pad both matrices to size×size with zeros
    aPad = resizeMatrix(mat1, size, size)
    bPad = resizeMatrix(mat2, size, size)
​
    # Perform Strassen multiplication on padded matrices
    cPad = strassen(aPad, bPad)
​
    # Extract the valid n×q result from the padded result
    C = [[0 for _ in range(q)] for _ in range(n)]
    for i in range(n):
        for j in range(q):
            C[i][j] = cPad[i][j]
​
    return C
​
if __name__ == "__main__":
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[7, 8], [9, 10], [11, 12]]
​
    res = multiply(mat1, mat2)
​
    for row in res:
        for val in row:
            print(val, end=" ")
        print()

# Output
# 58 64 
# 139 154 
# Time Complexity: O(s³) to O(s^log₂7) ≈ O(s^2.807), where s is the next power of two greater than max(n, m, q), due to only 7 recursive multiplications.
# Auxiliary Space: O(s²) because of the padding and the creation of intermediate submatrices during recursion.