#!/usr/bin/python3
# Este programa é um simulador de apocalipse zumbi.
# Ele calculará com base em algumas regras de sobrevivência como se dará a evolução
# de uma população dada uma posição inicial de cada tipo de ser em uma matriz de ordem também fornecida.
# Entrada:
# Número de linhas e colunas da matriz separadas por ' '
# Dias para simular
# As proximas linhas são as linhas da matriz (0 = vazio, 1 = humano, 2 = zumbi)
# Saída: (repetida pela quantidade de dias informados)
# Uma linha explicitando qual iteracao (dia) está sendo simulado
# A matriz inicial (1 vez)
# A matriz após a simulacao (dias de simulacao vezes)

# Nome: Flavio Augusto Pereira Cunha
# RA: 197083
import random

def main():
    dim = input().split(' ') # dimensão da matriz
    n = int(dim[0]) # linhas
    m = int(dim[1]) # colunas
    d = int(input()) # dias para simular
    # matriz inicial n x m com zeros, adicionando 2 colunas e 2 linhas
    planet = [[random.randint(0, 2) for j in range(m + 2)] for x in range(n + 2)]
    simulate(planet, d)

def simulate(pastDay, days):
    # Define os tipos para facilitar o entendimento no código
    zombie = 2
    human = 1
    empty = 0
    n = len(pastDay)
    m = len(pastDay[0])
    offset = [-1, 0, 1] # matriz de distâncias do individuo para seus vizinhos
    # print('iteracao 0')
    matrixPrint(pastDay)
    # Inicia a simulação
    for d in range(1, days + 1):
        # Matriz simulada do proximo dia com zeros, de mesma ordem da inicial
        simulated = [[0 for j in range(m)] for x in range(n)]
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                zcounter = 0 # zumbis
                hcounter = 0 # humanos
                # Analisa da sub-matriz 3x3 para cada posição da matriz do planeta
                for x in range(len(offset)):
                    for y in range(len(offset)):
                        # Ignora o caso i + 0 e j + 0, pois é o próprio individuo
                        if (offset[x] != 0 or offset[y] != 0):
                            neigh = pastDay[i + offset[y]][j + offset[x]] # vizinho
                            if (neigh == human):
                                hcounter += 1
                            if (neigh == zombie):
                                zcounter += 1
                # Depois de contar os vizinhos zumbis ou humanos
                # faz as validações para cada caso
                ind = pastDay[i][j] # individuo
                if (ind == human and zcounter >= 1):
                    ind = zombie
                elif (ind == zombie):
                    if (hcounter >= 2 or hcounter == 0):
                        ind = empty
                elif (ind == empty and hcounter == 2):
                    ind = human
                # Salva o novo individuo para a matriz do próximo dia
                simulated[i][j] = ind
        # print('iteracao', d)
        matrixPrint(simulated)
        pastDay = simulated.copy()

# Função de leitura da matriz de entrada
def readMatrix(matrix):
    # Adiciona cada linha lida para cada posição das linhas da matriz
    n = len(matrix) # linhas da matriz
    for i in range(1, n - 1): # pula a 1a linha de zeros's e vai até a penúltima linha
        line = input().split(' ')
        intline = [int(line[i]) for i in range(len(line))]
        matrix[i] = [0] + intline + [0]
    return matrix

# Impressão da matriz com zeros
def matrixPrint(matrix):
    if (matrix != []):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                print(matrix[i][j], end='')
            print()

main()
