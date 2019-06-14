# Este programa faz o processamento de imagens em formato PGM aplicando o método da convolução
# Entrada
# As entradas são feitas a partir de parâmetros para a execução do script
# A utilização é da forma:
# python3 lab18.py imagem.pgm matriz.txt
# Os parâmetros são 2 arquivos:
#  - O arquivo da imagem a ser processada no formato PGM
#  - O arquivo da matriz núcleo que será usada para formar as novas imagens
# Saída
# A saída será a imagem após o processamento também no formato PGM

# Nome: Flavio Augusto Pereira Cunha
# RA: 197083

import sys

############### Leitura das entradas ###############
pgm = open(sys.argv[1], mode='r') # arquivo PGM
txt = open(sys.argv[2], mode='r') # arquivo da matriz núcleo

# Arquivo 1, leitura da matriza imagem em PGM
linecount = 0   # Marcador que diz qual linha do arquivo está sendo lida 
img = []
for line in pgm.readlines():
    linecount += 1
    # Recupera as dimensões na segunda linha do arquivo
    if linecount == 2:
        dim = line.split()
        w, h = int(dim[0]), int(dim[1])
    # Lê a matriz a partir da 3 linha
    elif linecount > 3:
        # Adiciona as linhas na matriz imagem
        splitted = line.split()
        intline = [int(pxl) for pxl in splitted]
        img.append(intline)

# Arquivo 2, matriz núcleo e o divisor
linecount = 0
core = [] # inicializa a matriz nucelo
for line in txt.readlines():
    linecount += 1
    if linecount == 1:
        div = int(line) # divisor
    else:
        # Adiciona as linhas na matriz nucleo
        splitted = line.split()
        intline = [int(pxl) for pxl in splitted]
        core.append(intline)

# Função imprime matriz
# @parametro: vetor de duas dimensões
def matrixPrint(matrix):
    if (matrix != []):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                print('%2.f ' %matrix[i][j], end='')
            print()

############### Processamento da imagem (convolução) ###############


############### Exibição da saída ###############
matrixPrint(img)
matrixPrint(core)
pgm.close()
txt.close()