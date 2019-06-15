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
global w, h # Define as variáveis para altura e largura da imagem

# Arquivo 1, leitura da matriz imagem em PGM
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
core = [] 
for line in txt.readlines():
    linecount += 1
    if linecount == 1:
        div = int(line) # divisor
    else:
        # Adiciona as linhas na matriz nucleo
        splitted = line.split()
        intline = [int(pxl) for pxl in splitted]
        core.append(intline)
pgm.close()
txt.close()

############### Processamento e Saída ###############

def main():
    createPGM(convolution(img, core, div), h, w)

############### Funções auxiliares ###############

# Funcao convolução
#    Aplica o processo de convolução em uma matriz de duas dimensões,
#    dados os pesos e a matriz núcleo
# Parametros:
#   matrix:     Matriz de 2 dimensões a ser processada
#   core:       Matriz núcelo 3x3 utilizada como peso no processo
#   divider:    Divisor da função de convolução
# Retorno:
#   Matriz gerada após aplicado o processamento
def convolution(matrix, core, divider):
    offset = [-1, 0, 1] # matriz de distâncias do pixel para seus vizinhos    
    result = deepcopy(matrix) 
    
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # Analisa da sub-matriz 3x3 para cada posição da matriz imagem
            numerator = 0
            for x in range(3):
                for y in range(3):
                    numerator += core[x][y] * matrix[i + offset[x]][j + offset[y]]
            newPixel = numerator//divider
            # Limitação para o máximo suportado no PGM
            if newPixel < 0:
                newPixel = 0
            elif newPixel > 255:
                newPixel = 255
            result[i][j] = newPixel
    return result

# Função imprime matriz
#   Imprime uma matriz de duas dimensões formatada
# Parametros: 
#   matrix:     Uma matriz de números (int ou float) de duas dimensões
def matrixPrint(matrix):
    if (matrix != []):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(0, m - 1):
                print(matrix[i][j], end=' ')
            print(matrix[i][j + 1])
    else:
        print('[]')

# Função criar PGM
#   Monta o arquivo PGM e exibe na tela suas linhas
#   A função assume 255 como valor máximo para branco
# Parametros:
#   matrix:     Matriz da imagem a ser escrita no PGM
#   lines:      Linhas da matriz
#   cols:       Colunas da matriz
def createPGM(matrix, lines, cols):
    print('P2')
    print(cols, lines)
    print('255')
    matrixPrint(matrix)

# Funcão cópia profunda
#   Copia uma matriz bidimensional a nivel de cada item
#   para não manter a referência das listas internas
# Parametros:
#   arr:    Uma lista bimensional como fonte de cópia
# Retorno:
#   Retorna exatamente a mesma matriz bidimensional no parametro
#   porém sem as referências de suas linhas
def deepcopy(arr):
    b = []
    for line in arr:
        l = []
        for col in line:
            l.append(col)
        b.append(l)
    return b

# Chamada principal
main()
