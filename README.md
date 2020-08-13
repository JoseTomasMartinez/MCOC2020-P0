# MCOC2020-P0

# Mi computador principal

* Marca/modelo: Lenovo ideapad 320 80XG
* Tipo: Notebook
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: Intel Core i3-6006U
  * Velocidad Base: 2.00 GHz
  * Numero de núcleos: 2 
  * Numero de hilos: 4
  * Arquitectura: x64

* Tamaño de las cachés del procesador
  * L1d: 32KB
  * L1i: 32KB
  * L2: 256KB
  * L3: 3000KB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR4
  * Velocidad 1064 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Nvidia GeForce 920MX
  * Memoria dedicada: 2048 MB
  * Resolución: 1366 x 768
* Disco 1: 
  * Marca: Western Digital
  * Tipo: HDD
  * Tamaño: 440 GB
  * Particiones: 1
  * Sistema de archivos: NTFS
* Disco 2: 
  * Marca: Lenovo
  * Tipo: HDD
  * Tamaño: 25 GB
  * Particiones: 1
  * Sistema de archivos: NTFS

  
* Dirección MAC de la tarjeta wifi: E8:2A:44:E7:72:C5 
* Dirección IP (Interna, del router): 192.168.1.1
* Dirección IP (Externa, del ISP): 191.114.36.190
* Proveedor internet: Movistar

# Desempeño Matmul
* Gráfico Rendimiento Matmul:
  ![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P0/blob/master/Graficos%20Rendimiento%20MATMUL.JPG)

* Respuestas preguntas:
  * Los gráficos muestran diferencias en los tiempos de ejecución. En el gráfico del profesor se ve que la primera multiplicación de matrices de cada corrida
    se demora 0.1 ms, mientras que en el gráfico del alumno se demora 0.1 s. en la mayoría de las corridas. Parece ser que el computador del alumno toma mas
    tiempo en los primeros calculos, pero una vez que el ciclo avanza, los calculos alcanzan tiempos parecidos a los del profesor. Esto se demuestra en las 
    últimas multiplicaciones en cada corrida.
  * Las diferencias pueden deberse muy probablemente a las cualidades de cada computador. Memoria RAM, procesador, espacio utilizado, etc. Estos elementos 
    afectan los procesos del computador, en los que se incluyen este tipo de programas, por lo tanto según las caracteristicas de cada computador los tiempos
    varian. De todas maneras, a simple vista los valores son bastante similares.
  * El gráfico del uso de memoria es líneal debido a que el aumento de las dimensiones de la matriz es líneal. El uso de memoria depende de la cantidad de números
    utilizados, por lo tanto a mayor dimension de las matrices que se multiplican, mayor es la cantidad de memoria utilizada. Como todas las corridas utilizan matrices
    con las mismas dimensiones, la memoria utilizada es exactamente igual en todas las corridas, mientras que el tiempo tiene pequeñas variaciones en cada corrida, las 
    cuales se pueden notar en el gráfico.
  * Versión de python: 3.7
  * Versión de numpy: 1.18.2
  * Imagen uso de procesador: 
  ![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P0/blob/master/Procesadores%20utilizados%20MATMUL.jpg)
   * La imagen muestra los porcentajes de uso de los cuatro procesadores lógicos. Al inicio del gráfico se ve un uso menor al 50%. El aumento brusco del uso de los 
     procesadores que se puede notar en la imagen, sucede cuando se corre el código timing_matmul.py. Como el aumento se produce en todos los procesadores se puede 
     afirmar que se esta utilizando más de uno.
# Desempeño MiMatmul
* Gráfico Rendimiento MiMatmul:
 ![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P0/blob/master/Rendimiento%20MiMatmul%20(dim%20600).PNG)
   * Los gráficos de rendimiento de la multiplicacion de matrices de python y del método implementado "a mano" son prácticamente iguales, con la diferencia en que el
     el segundo llega solo hasta la matriz de 600x600. Es decir, con el método de python el programa se demora el mismo tiempo en 10 corridas hasta matrices de 
     10000x10000 que el método implementado, siendo que para este solo se llegó hasta matrices de 600x600, dado que con mas números el tiempo era demasiado. Por lo tanto,
     el método de python es mucho más eficiente que el método implementado
* Imagen uso de procesador:

 ![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P0/blob/master/Procesadores%20utilizados%20MIMATMUL.JPG)
   * Al igual que con la multiplicación de matrices de python, se utilizan los 4 procesadores que posee el computador, sin embargo se puede observar que el porcentaje 
     de uso es menor para el caso del método implementado "a mano". Esto probablemente se debe a que el método que usa python es más complejo y efectivo, por lo tanto
     el procesador debe trabajar más.
# Desempeño de INV
* Tamaños en memoria tipos de datos:
   * np.half: float16 (2 bytes)
   * np.single: float32 (4 bytes)
   * np.double: float64 (8 bytes)
   * np.longdouble: float64 (8 bytes)
   * Como los datos de tipo double y longdouble son iguales en el sistema del alumno, el desempeño de la inversa de la matriz laplaciana se realizó para los primeros tres
     tipos de datos
* Aálisis memoria y procesadores:
   * Para mostrar como afectan las cachés en el desempeño se toma como ejemplo el gráfico de rendimiento del caso 3 (scipy overflow=True) con el tipo de dato single (float32).
    ![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P0/blob/master/Rendimiento%20Caso%202%20Single.png)
   * Se puede notar que los saltos que se producen en los tiempos son a la altura de las líneas azules marcadas en la memoria, las cuales representan las memorias de las cachés
     del procesador. Esto se debe al aumento en el uso de memoria dado al aumento de dimension en las matrices que se invierten. Cuando el uso de memoria es cercano al tamaño 
     de alguna de las cachés se comienza a utilizar la siguiente. En ese traspaso existen pequeños saltos, pues el procesador comienza a utilizar otra memoria para realizar el
     proceso. Estos saltos se pueden ver también en todos los otros casos, cuyos gráficos fueron subidos al repositorio. 
   * Otra cosa que se puede observar es que los tiempos son algo menores a medida que el tipo de dato es menos pesado. Es decir los tiempos para un tipo de dato half (float16)
     es menor que un tipo de dato single (float32) y este a su vez menor que un tipo de dato double(float64), lo cual tiene bastante lógica. Esto se puede observar en los
     tiempos para las matrices mas grandes. Cabe mencionar que numpy muestra un error al intentar calcular la inversa de matrices para el tipo de dato half (float16), es por 
     eso que no existe gráfico de rendimiento para el caso 1 en este tipo de dato, mientras que si los hay para los casos 2 y 3, pues scipy si lo calcula. 
   * En cuanto a las diferencias de rendimiento entre scipy utilizando overflow=True o False, no se aprecian mayores diferencias a simple vista. En general el tiempo de
     ejecución para todas las corridas era parecido. Sí se notaba una demora mayor en el tipo de dato double, lo que también es lógico dado que son datos más pesados.
   * El uso de los procesadores es practicamente máximo en cualquiera de los casos y en todos, los cuatro procesadores trabajan al mismo tiempo. La única diferencia es que
     para el tipo de dato half (float16) el uso no comienza siendo alto como en los demás, si no que va subiendo de a poco hasta que en cierto numero de elementos de la
     matriz el uso es máximo, tal como muestra la imagen:
     ![myimage-alt-tag](https://github.com/JoseTomasMartinez/MCOC2020-P0/blob/master/Procesadores%20Desempe%C3%B1o%20INV%20Half.png)
