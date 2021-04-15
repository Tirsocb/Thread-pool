import csv
import sys
import time as t
import threading
import numpy as np


# captura de argumentos en linea de comandos
print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))

fileA = open(sys.argv[1], "rb")
matrix = np.loadtxt(fileA, delimiter=",")

fileB = sys.argv[2]
fileO = sys.argv[4]
poolSize = int(sys.argv[3])


print(matrix)






