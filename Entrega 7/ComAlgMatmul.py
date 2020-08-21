#Jose Tomas Martinez Lavin
from numpy import *
from time import perf_counter
import matplotlib.pyplot as plt
def matriz_laplaciana(N,t=double):
	m=eye(N,N)-eye(N,N,1)
	return t(m+m.T)
Corridas=10
N = [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,3000,5000,7000,10000]

ENcorridas=[]
ALcorridas=[]
for i in range(Corridas):
	ebj=[]
	alg=[]
	for n in N:
		t=perf_counter()
		A=matriz_laplaciana(n)
		B=matriz_laplaciana(n)
		t1=perf_counter()
		x=A@B
		t2=perf_counter()
		dte=t1-t
		dta=t2-t1
		ebj.append(dte)
		alg.append(dta)
	ENcorridas.append(ebj)
	ALcorridas.append(alg)
ec=[]
elineal=[]
ecuadratica=[]
ecubica=[]
ecuarta=[]
for i in range(len(N)):
	ec.append(ebj[len(ebj)-1])
	elineal.append((N[i])*((ebj[len(ebj)-1])/(N[len(N)-1])))
	ecuadratica.append((N[i]**2)*((ebj[len(ebj)-1])/(N[len(N)-1])**2))
	ecubica.append((N[i]**3)*((ebj[len(ebj)-1])/(N[len(N)-1])**3))
	ecuarta.append((N[i]**4)*((ebj[len(ebj)-1])/(N[len(N)-1])**4))

ac=[]
alineal=[]
acuadratica=[]
acubica=[]
acuarta=[]
for i in range(len(N)):
	ac.append(alg[len(alg)-1])
	alineal.append((N[i])*((alg[len(alg)-1])/(N[len(N)-1])))
	acuadratica.append((N[i]**2)*((alg[len(alg)-1])/(N[len(N)-1])**2))
	acubica.append((N[i]**3)*((alg[len(alg)-1])/(N[len(N)-1])**3))
	acuarta.append((N[i]**4)*((alg[len(alg)-1])/(N[len(N)-1])**4))

ax1=plt.subplot(2,1,1)
ax1.set(ylim=(0.00001,600))
plt.title("Complejidad algoritmica matmul")
plt.ylabel("Tiempo de ensamblado")
plt.xscale("log")
plt.yscale("log")
tickt=[0.0001,0.001,0.01,0.1,1,10,60,600]
ticktstr=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
plt.yticks(tickt,ticktstr)
plt.xticks(visible=False)
for i in range(Corridas):
	plt.plot(N,ENcorridas[i],"ko-")

plt.plot(N,ec,"--")
plt.plot(N,elineal,"--")
plt.plot(N,ecuadratica,"--")
plt.plot(N,ecubica,"--")
plt.plot(N,ecuarta,"--")

ax2=plt.subplot(2,1,2)
ax2.set(ylim=(0.000001,600))
plt.xlabel("Tamaño Matriz N")
plt.ylabel("Tiempo de multiplicación")
plt.xscale("log")
plt.yscale("log")
tickn=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
plt.xticks(tickn,tickn,rotation=45)
plt.yticks(tickt,ticktstr)
for i in range(Corridas):
	plt.plot(N,ALcorridas[i],"ko-")

plt.plot(N,ac,"--",label="Constante")
plt.plot(N,alineal,"--",label="O(N)")
plt.plot(N,acuadratica,"--",label="O($N^2$)")
plt.plot(N,acubica,"--",label="O($N^3$)")
plt.plot(N,acuarta,"--",label="O($N^4$)")
plt.legend()	
plt.savefig("Complejidad algoritmica matmul")	
plt.show()