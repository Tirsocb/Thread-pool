import csv
import sys
import time as t
from threading import Thread
import numpy as np

# captura de argumentos en linea de comandos
print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))
try:

    """
    Convierte los csv files ingresados a matrices,
    indicando que están delimitadas por ','

    Lo realiza tanto para fileA, como para fileB
    """
    fileA = open(sys.argv[1], "rb")
    matrixA = np.loadtxt(fileA, delimiter=",")

    fileB = open(sys.argv[2], "rb")
    matrixB = np.loadtxt(fileB, delimiter=",")

    poolSize = int(sys.argv[3])

except:
    print("ERROR, check input parameters & existence of input files in the correct directory")
    print("\nto retry: python3 matmul.py <matrixA.csv> <matrixB.csv> <Pool size (int)> <OutputFile.txt>")
fileO = sys.argv[4]

# obtener dimensiones de la matriz (columnas)
n = int(matrixA.shape[0])
# crear matriz para guardar resultado
matrixC = np.zeros((n, n), int)

print(n)

print("MATRIX A")
print(matrixA)

print("\n MATRIX B")
print(matrixB)

print("\n THREADS: " + str(poolSize))

"""
Función para multiplicar las dos matrices ingresadas
Se multiplican por bloques calculados según el número de threads
El resultado es guardado en matrixc
input: límite superior, límite inferior
"""
def Multiplication(s, e):
    for i in range(s, e):
        print(str(i))
        for j in range(n):
            for k in range(n):
                matrixC[i][j] += int(matrixA[i][k] * matrixB[k][j])

"""
Ejecuta la multiplicación de dos matrices a través de threads
Son calculados los bloques (segmentos) en los que se multiplicarán las matrices
Se calculan los límites de los segmentos de la matriz
"""
def parallel(size):
    threadHandler = []
    # For i, significa que lo realiza en las filas
    for i in range(0, size): # size número de cores
        """
        Aquí se indica que el target del thread es la función multiplicación y se calculan los argumentos
        El primero es límite inferior del segmento de la matriz
        El segundo argumento es el límite superior del segmento de la matriz
        """
        # n es el tamaño de la matriz
        thread = Thread(target=Multiplication, args=(int((n / size) * i), int((n / size) * (i + 1))))
        threadHandler.append(thread)
        thread.start()

    # For j, significa que lo realiza en las columnas
    for j in range(0, size):
        threadHandler[j].join()

"""
Ejecuta la multiplicación parelela y calcula el tiempo de ejecución 
El tiempo es dado en segundos
"""
start = t.time()
parallel(poolSize)
end = t.time()
totalTime = end - start

"""
Guardar los resultados en un archivo .csv
* El tiempo de ejecución
* El número de cores
* La matriz resultante
"""
poolSize = str(poolSize) # número de cores

with open(fileO, 'w') as fp:
    fp.write("%s = %s\n" % ("Time: ", totalTime))
    fp.write("%s = %s\n" % ("Treads: ", poolSize))
    np.savetxt(fp, matrixC, '%s', ',')