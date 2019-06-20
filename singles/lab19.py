# Este programa extrai a lista de subordinados de
# uma árvore de hierarquia de uma empresa utilizando métodos recursivos.
# Entrada
#   Na primeira linha de entrada o programa recebe 2 entradas separadas por espaço:
#       - A ordem da matriz que será recebida
#       - O número do funcionário (posição da linha na matriz) que deseja-se obter a cadeia hierárquica
#   Da segunda em diante a entrada esperada são as linhas da matriz hierárquica da empresa, definida na forma:  
#       - Uma matriz quadrada composta de zeros e uns onde cada coluna e linha
#       representa um funcionário da empresa.
#       Dada a posição i, j, e a matriz de hierarquia M, sendo i o índice da linha e j o da coluna:
#           - Se M[i][j] conter o número 1, o funcionário i é superior do j
#           - Se M[i][j] for 0, o funcionário i não é superior do j
# Saída
#   O programa exibe uma linha com todos os números de funcionários subordinados no funcionário requisitado, incluindo ele mesmo.

# Nome: Flavio Augusto Pereira Cunha
# RA: 197083

# Leitura e processamento
def main():
    line = input().split()
    n = int(line[0])        # ordem da matriz
    emp = int(line[1])      # funcionário a ser analisado
    matrix = []
    for i in range(n):
        line = input().split()
        intline = [int(x) for x in line]
        matrix.append(intline)
    tree = []
    subFinder(tree, matrix, emp)
    printer(tree)


# Função recursiva que encontra os subordinados de um dado funcionário
# Parametros:   
#   tree:   lista para inserir os subordinados
#   mat:    matriz da hierarquia
#   i:      posição da linha do funcionário para a analise
def subFinder(tree, mat, i):
    insertSorted(tree, i)
    for j in range(len(mat[i])):
        if mat[i][j] == 1:
            subFinder(tree, mat, j)

# Função auxiliar de inserção ordenada
# Parametros:
#   v:      lista de números ordenada ou vazia
#   num:    número a ser inserido
def insertSorted(v, num):
    v.append(num)
    if len(v) == 1:
        return
    else:
        i = len(v) - 1
        aux = v[-1]
        j = i - 1
        while j>=0 and v[j] > aux:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = aux

# Função de exibição da cadeia de subordinados
# Parametros:
# v:        lista normal
def printer(v):
    for x in v[:-1]:
        print(x, end=' ')
    print(v[-1])

main()