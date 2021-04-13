import sys


# captura de argumentos en linea de comandos
print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))

fileA = sys.argv[1]
fileB = sys.argv[2]
fileO = sys.argv[4]

poolSize = int(sys.argv[3])

print(fileA + fileB + fileO + str(poolSize))

