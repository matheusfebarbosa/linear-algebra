import numpy as np

def lu_decomposition(matrix):
	U = np.copy(matrix)
	P = np.diag(np.ones(len(np.diag(U))))
	i=0
	j=0
	while i<len(U) and j<len(U[0]):
		pivot = np.argmax([abs(x) for x in U[i:,j]]) + i

		if(U[pivot][j] == 0):
			j+=1
		else:
			aux = [x for x in U[pivot]]
			U[pivot,:] = U[i]
			U[i,:] = aux[:]

			aux = [p for p in P[pivot]]
			P[pivot,:] = P[i]
			P[i,:] = aux[:]

			for k in range(i+1,len(U)):
				p = U[k,j]/U[i,j]
				U[k,j] = p
				for l in range(j+1,len(U[k])):
					U[k,l] = U[k,l] - (U[i,l] * p)

			i+=1
			j+=1

	L = np.tril(U)
	np.fill_diagonal(L,1)
	U = np.triu(U)

	return P,L,U