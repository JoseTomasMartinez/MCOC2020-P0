from numpy import *
from scipy import matrix,rand
from time import perf_counter
N=2

#Aqui se comprueba con la matriz identidad que se estan muktiplicando matrices y no arreglos 
A=matrix([[1,2,3],[4,5,6],[7,8,9]])
I=matrix(identity(3))
print (A*I)



#Multiplicacion de matrices creadas manualmente
B=matrix([[10,11,12],[13,14,15],[16,17,18]])
print (A*B)

#Multiplicacion de matrices creadas aleatoriamente
C=matrix(rand(N,N))
D=matrix(rand(N,N))
print (C)
print (D)
print (C*D)

