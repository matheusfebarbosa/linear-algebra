import numpy as np

def gaussian_elimination(matrix):
	i=0
	j=0
	while i<len(matrix) and j<len(matrix[0]):
		pivot = np.argmax([abs(x) for x in matrix[i:,j]]) + i
		
		if(matrix[pivot][j] == 0):
			j+=1
		else:
			aux = [x for x in matrix[pivot]]
			matrix[pivot,:] = matrix[i]
			matrix[i,:] = aux[:]

			for k in range(i+1,len(matrix)):
				p = matrix[k,j]/matrix[i,j]
				for l in range(j,len(matrix[k])):
					matrix[k,l] = matrix[k,l] - (matrix[i,l] * p)

			i+=1
			j+=1



ex = np.array([[1.0,3.0,1.0],[1.0,1.0,-1.0],[3.0,11.0,5.0]])
print(ex)
gaussian_elimination(ex)
print(ex)