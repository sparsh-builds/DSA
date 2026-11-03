class Solution:
	def rotateMatrix(self, mat):
		# code here
	    mat.reverse()
	    
	    for row in mat:
	        row.reverse()
	        
	    return mat
 
 
# 2nd method
class Solution:
	def rotateMatrix(self, mat):
		# code here
		n=len(mat)
		res = [[0]*n for _ in range(n)]
		
		for i in range(n):
		    for j in range(n):
		        
		        res[i][j]=mat[n-i-1][n-j-1]
		        
		for i in range(n):
		    for j in range(n):
		        mat[i][j]=res[i][j]
		return mat

