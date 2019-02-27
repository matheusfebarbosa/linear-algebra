from lib.lu_decomposition import lu_decomposition
import lib.linalg_utils as la
import numpy as np

def main():
	A = np.array([[1,-2,3],[2,-5,12],[0,2,-10]],dtype=float)
	print("A: ")
	print(A)
	P,L,U = lu_decomposition(A)
	print("P:")
	print(P)
	print("L:")
	print(L)
	print("U:")
	print(U)
	print("inv(P).L.U:")
	print(np.dot(np.transpose(P),np.dot(L,U)))

if __name__ == "__main__":
	main()