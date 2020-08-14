#Jose Tomas Martinez Lavin
from numpy import *
from time import perf_counter
import matplotlib.pyplot as plt
def matriz_laplaciana(N,t=float32):
	m=eye(N,N)-eye(N,N,1)
	return t(m+m.T)

solvers=["Inversa","NumpySolver"]
Corridas=10
N = [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]
archivos=[open(f"{n}.txt","w") for n in solvers]

for i in range(len(N)):
	dts=zeros((Corridas,len(solvers)))
	for j in range(Corridas):
		#Invertir y Multiplicar
		A=matriz_laplaciana(N[i])
		b=ones(N[i])
		t1=perf_counter()
		Ainv=linalg.inv(A)
		x=Ainv@b
		t2=perf_counter()
		dt=t2-t1
		dts[j][0]=dt

		#Numpy Solver
		A=matriz_laplaciana(N[i])
		b=ones(N[i])
		t1=perf_counter()
		x=linalg.solve(A,b)
		t2=perf_counter()
		dt=t2-t1
		dts[j][1]=dt

	promedio=[mean(dts[:,p]) for p in range(len(archivos))]
	for j in range(len(archivos)):
		archivos[j].write(f"{promedio[j]}\n")
[a.close() for a in archivos]

T=[]
for s in solvers:
	t=[]
	a=open(f"{s}.txt")
	for i in a:
		t.append(float(i))
	T.append(t)

plt.title("Rendimiento Solvers")
plt.ylabel("Tiempo Transcurrido (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid()
tickt=[0.0001,0.001,0.01,0.1,1,10,60,600]
ticktstr=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
tickn=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
plt.yticks(tickt,ticktstr)
plt.xticks(tickn,tickn,rotation=75)
for i in range(len(solvers)):
	plt.plot(N,T[i],"o-")
plt.legend(solvers)
plt.savefig("Rendimiento Solvers")	
plt.show()
