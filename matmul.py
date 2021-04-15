import csv
import sys
import time as t
import threading
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

print("MATRIX A")
print(matrixA)

print("\n MATRIX B")
print(matrixB)

print("\n THREADS: "+ str(poolSize))










