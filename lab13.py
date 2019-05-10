# Este programa é um simulador de apocalipse zumbi.
# Ele calculará com base em algumas regras de sobrevivência como se dará a evolução
# de uma população dada uma posição inicial de cada tipo de ser em uma matriz de ordem também fornecida.
# Entrada:
# Número de linhas da matriz
# Número de colunas da matriz
# Dias para simular
# As proximas linhas são as linhas da matriz composta por n inteiros (0 = vazio, 1 = humano, 2 = zumbi)

n = int(input()) # n linhas
m = int(input()) # m colunas
planet = [0 for j in range(m)] # matriz inicial 1 x m com zeros

def readMatrix(matrix):
    # Adiciona cada linha lida para cada posição das linhas da matriz
    n = len(matrix)
    for i in range(n):
        line = input().split(' ')
        for j in range(len(line)):
            matrix[i][j] = line[j]
    return matrix

def matrixPrint(matrix):
    if (matrix != []):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                print(matrix[i][j], end='')
            print()

readMatrix(planet)
matrixPrint(planet)