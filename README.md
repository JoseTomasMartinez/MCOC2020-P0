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
  * https://github.com/JoseTomasMartinez/MCOC2020-P0/blob/master/Graficos%20Rendimiento%20MATMUL.JPG

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
  * https://github.com/JoseTomasMartinez/MCOC2020-P0/blob/master/Procesadores%20utilizados%20MATMUL.jpg
   * La imagen muestra los porcentajes de uso de los cuatro procesadores lógicos. Al inicio del gráfico se ve un uso menor al 50%. El aumento brusco del uso de los 
     procesadores que se puede notar en la imagen, sucede cuando se corre el código timing_matmul.py. Como el aumento se produce en todos los procesadores se puede 
     afirmar que se esta utilizando más de uno.
# Desempeño MiMatmul
* Gráfico Rendimiento MiMatmul:
* Imagen uso de procesador:
![myimage-alt-tag]
