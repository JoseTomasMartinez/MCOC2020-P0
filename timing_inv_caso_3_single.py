#Caso 3 np.single
from numpy import *
from time import perf_counter
import scipy
from scipy.linalg import inv
import numpy as np
import matplotlib.pyplot as plt

def laplaciana(n):
	M = zeros([n,n],dtype=np.single)
	for j in range(n):
		for k in range(n):
			if j==k:
				M[j][k]=2
			if (j-k)==(1) or (j-k)==(-1):
				M[j][k]=-1
	return matrix(M)

Corridas=10
for k in range(Corridas):
	N = [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]
	memoria=[]
	tiempos=[]
	for i in range(len(N)):
		ML = laplaciana(N[i])
		t1 = perf_counter()
		C = scipy.linalg.inv(ML,overwrite_a=True)
		t2 = perf_counter()
		dt = t2 - t1
		tam=2*(N[i]**2)*4 #2 Matrices (Laplaciana e invertida), 4 bytes (single=float32)
		tiempos.append(dt)
		memoria.append(tam)
	a=open(f"matmul{k}.txt","w")
	for i in range(len(N)):
		a.write(f"{N[i]} {tiempos[i]} {memoria[i]}.\n")
	a.close()

Tcorridas=[]
Mcorridas=[]
for i in range(Corridas):
	t=[]
	m=[]
	a=open(f"matmul{i}.txt")
	for j in a:
		l=j.split()
		t.append(float(l[1]))
		m.append(float(l[2]))
	Tcorridas.append(t)
	Mcorridas.append(m)

plt.subplot(2,1,1)
plt.title("Rendimiento Caso 3 SINGLE")
plt.ylabel("Tiempo Transcurrido (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid()
tickt=[0.0001,0.001,0.01,0.1,1,10,60,600]
ticktstr=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
plt.yticks(tickt,ticktstr)
plt.xticks(visible=False)
for i in range(Corridas):
	plt.plot(N,Tcorridas[i],"o-")

plt.subplot(2,1,2)
plt.xlabel("Tamaño Matriz N")
plt.ylabel("Uso memoria (b)")
plt.xscale("log")
plt.yscale("log")
plt.grid()
tickm=[1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
tickmstr=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
tickn=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
plt.xticks(tickn,tickn,rotation=75)
plt.yticks(tickm,tickmstr)
for i in range(Corridas):
	plt.plot(N,Mcorridas[i],"o-")
plt.savefig("Rendimiento Caso 3 Single")	
plt.show()