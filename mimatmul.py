#Jose Tomas Martinez Lavin
from scipy import matrix, rand
from time import perf_counter
import matplotlib.pyplot as plt


def mimatmul(A,B):
	A=A.tolist()
	B=B.tolist()
	C=[]
	for i in range(len(A)):
		C.append([])
		for j in range(len(A)):
			C[i].append(0)
	for i in range(len(A)):
		for j in range(len(A)):
			for k  in range(len(A)):
				C[i][j]+=A[i][k]*B[k][j]
	return matrix(C)