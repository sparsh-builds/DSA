class Solution:
    def rotateMatrix(self, mat: list[list[int]]) -> None:
        # code here
        
        # mtlb [[1,2,3],[4,5,6],[7,8,9]] ko rotate in anti clockwise direction means become [[3,6,9],[2,5,8],[1,4,7]]
        
        n = len(mat)
        
        # Transpose the matrix