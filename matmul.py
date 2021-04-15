import csv
import sys
import time as t
from threading import Thread
import numpy as np

# captura de argumentos en linea de comandos
print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))
try:

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


def Multiplication(s, e):
    for i in range(s, e):
        print(str(i))
        for j in range(n):
            for k in range(n):
                matrixC[i][j] += int(matrixA[i][k] * matrixB[k][j])


def parallel(size):
    threadHandler = []
    for i in range(0, size):
        thread = Thread(target=Multiplication, args=(int((n / size) * i), int((n / size) * (i + 1))))
        threadHandler.append(thread)
        thread.start()

    for j in range(0, size):
        threadHandler[j].join()


start = t.time()
parallel(poolSize)
end = t.time()
totalTime = end - start

print(totalTime)