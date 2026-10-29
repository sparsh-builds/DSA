Given a matrix mat[][] of size n × n, compute its transpose. The transpose of a matrix is obtained by converting its rows into columns and its columns into rows.

Example:

Input: mat[][] = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
Output: [[1, 2, 3 ,4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
Explanation:  The output is the transpose of the input matrix, where each row becomes a column. This rearranges the data so that vertical patterns in the original matrix become horizontal in the result.

Input: mat[][] = [[1, 2], [9, -2]]
Output: [[1, 9], [2, -2]]
Explanation:  The output is the transpose of the input matrix, where each row becomes a column. This rearranges the data so that vertical patterns in the original matrix become horizontal in the result.

Table of Content

[Naive Approach] - Brute Force Matrix Transposition O(n^2) Time and O(n^2) Space
[Expected Approach] - Using constant space for Square Matrix O(n^2) Time and O(1) Space
[Naive Approach] - Brute Force Matrix Transposition O(n^2) Time and O(n^2) Space
The idea is to create a new matrix where rows become columns by swapping indices — element at position [i][j] in the original becomes [j][i] in the transposed matrix.

Step by Step Implementations:

Initialize a new matrix of size n × n (rows become columns and vice versa).
Iterate through each element of the original matrix.
Assign each element from row r and column c in the original matrix to row c and column r in the new matrix.
Return the new transposed matrix.




def transpose(mat):
    n = len(mat)
​
    # Create a result matrix of size n x n
    tMat = [[0 for _ in range(n)] for _ in range(n)]
​
    # Fill the transposed matrix by
    # swapping rows with columns
    for i in range(n):
        for j in range(n):
​
            # Assign transposed value
            tMat[j][i] = mat[i][j]
​
    return tMat
​
​
if __name__ == "__main__":
    mat = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]
    ]
​
    res = transpose(mat)
​
    for row in res:
        for elem in row:
            print(elem, end=" ")
        print()

Output
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 
[Expected Approach] - Using constant space for Square Matrix O(n^2) Time and O(1) Space
This approach works only for square matrices, where the number of rows is equal to the number of columns. It is called an in-place algorithm because it performs the transposition without using any extra space.

Step by Step Implementations:

Initialize two nested loops:

Outer loop: i from 0 to n-1
Inner loop: j from i+1 to n-1
This avoids diagonal and already swapped positions.
Swap elements:

For each pair (i, j), swap mat[i][j] with mat[j][i]
This mirrors the elements across the main diagonal.
Continue until all such upper-triangle elements are swapped with their lower-triangle counterparts.





def transpose(mat):
    
    # Number of rows (and columns, since it's square)
    n = len(mat)  
​
    # Traverse the upper triangle of the matrix 
    for i in range(n):
        for j in range(i + 1, n):
            
            # Swap elements across the diagonal
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
​
    return mat  
​
​
if __name__ == "__main__":
    mat = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    res = transpose(mat)  
    for row in res:
        print(" ".join(map(str, row)))

Output
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 
If you are facing any issue on this