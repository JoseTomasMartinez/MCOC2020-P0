from numpy import *
from scipy import matrix,rand
from time import perf_counter
N=2

#Aqui se comprueba con la matriz identidad que se estan muktiplicando matrices y no arreglos 
A=matrix([[1,2,3],[4,5,6],[7,8,9]])
I=matrix(identity(3))
print (A*I)

t1=perf_counter()

#Multiplicacion de matrices creadas manualmente
B=matrix([[10,11,12],[13,14,15],[16,17,18]])
print (A*B)
t2=perf_counter()

#Multiplicacion de matrices creadas aleatoriamente
C=matrix(rand(N,N))
D=matrix(rand(N,N))
print (C)
print (D)
print (C*D)
t3=perf_counter()
Ttotal=perf_counter()

MA_I=t1
MA_B=t2-t1
MC_D=t3-t2

print (f"Tiempo transcurrido al generar matriz identidad y multiplicarla por matriz manual A= {MA_I} s")
print (f"Tiempo transcurrido al generar matriz manual B y multiplicarla por matriz manual A= {MA_B} s")
print (f"Tiempo transcurrido al generar matriz aleatoria C y multiplicarla por matriz aleatoria D = {MC_D} s")
print (f"Tiempo total transcurrido = {Ttotal} s")

#Tiempos: Aproximadamente 0.45 segundos en realizar la multiplicacion de A*I
#Los demás procesos son rápidos (menor a 0.01 seg). Probando solo con la generación de matrices aleatorias, el tiempo es similar.
#Por lo tanto, se puede concluir que la primera parte del código relacionado a multiplicación de matrices
#toma algo más de tiempo, no importa si es manual o aleatorio. El tiempo total es prácticamente igual al tiempo
#del primer proceso.
