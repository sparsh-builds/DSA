# our task is to swap major and minor diagonals 

# [[1,2,3],[4,5,6],[7,8,9]] => [[3,2,1],[4,5,6],[9,8,7]]

class Solution:
    def swapDiagonal(self, mat):
      # code here
        n = len(mat)
        
    
        

        for i in range(n):
            
                mat[i][i],mat[i][n-i-1]=mat[i][n-1-i],mat[i][i]
            
                
        
        return mat
        
        