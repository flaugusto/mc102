#!/usr/bin/env python3
# Laboratório 20: Sudoku
# Nome: Flavio Augusto Pereira Cunha
# RA: 197083

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku

# O aluno pode criar outras funcoes que ache necessario

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario
def resolve(resposta):
    if findNext(resposta) != None:
        return True
    return False

####### Função recursiva principal #######
def findNext(sudoku):
    # Acha a próxima posição vazia na linha corrente 
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                # Para cada número válido encontrado:
                for valid in validNumbers(sudoku, i, j):
                    # Se não exisitr nenhum número válido por esse caminho, invalida o retorno
                    if valid == None:
                        return None
                    # Troca o zero pelo número encontrado
                    sudoku[i][j] = valid
                    print_sudoku(sudoku)
                    if findNext(sudoku) == None:
                        continue
                sudoku[i][j] = 0

####### Funções auxiliares #######

# Gerador de numeros válidos
#   Gera as possibilidades de números para uma dada posição
# Parametros:
#   sudoku:     A matriz do jogo sudoku 9x9 (com 0 em posições vazias)
#   i:          A posicao da linha para encontrar os números possíveis
#   j:          A posição da coluna para encontrar os números possíveis
# Retorno:
#   Um iterável contendo cada possibilidade encontrada para a posição
def validNumbers(sudoku, i, j):
    ### Geração de números possíveis ###
    # Divide a matriz do sudoku em uma matriz 3x3 de matrizes 3x3 individuais
    divided = divide(sudoku)

    # Para cada número de 1 a 9, testa se ele é possível e gera se for
    found = False
    for num in range(1,10):
        # Verifica se o número está na linha
        if searchInLine(sudoku, num, i):
            continue
        # Se não tem na linha, procura na coluna
        elif searchInColumn(sudoku, num, j):
            continue
        # Se não tem na coluna e linha, procura na região
        elif searchInRegion(divided, num, i,j):
            continue
        # Se não achou o número nas condições, é um número válido
        else:
            yield num
            found = True
    # Se para todos os números não foi encontrado nenhum válido, retorna None e termina
    if not found:
        yield None
    return

# Função: Procura na linha
#   Valida se número existe na linha i da tabela do jogo
# Parametros:
#   sudoku:     tabela do jogo
#   num:        um número de 1 a 9
#   i:          posição da linha
# Retorno:  True se econtrar, False senão
def searchInLine(sudoku, num, i):
    for x in sudoku[i]:
        if x == 0 or x != num:
            continue
        else:
            return True
    return False

# Função: Procura na coluna
#   Valida se número existe na coluna j da tabela do jogo
# Parametros:
#   sudoku:     tabela do jogo
#   num:        um número de 1 a 9
#   j:          posição da coluna
def searchInColumn(sudoku, num, j):
    for line in sudoku:
        for x in range(j, j + 1):
            if line[x] == 0 or line[x] != num:
                continue
            else:
                return True
    return False

# Função: Procura na região
#   Valida se número existe na região 3x3 da posição i,j da tabela do jogo
# Parametros:
#   divided:    tabela do jogo dividida em matrizes 3x3
#   num:        um número de 1 a 9
#   i:          indice da linha da posição avaliada
#   j:          indice da coluna da posição avaliada
# Retorno:  True se econtrar, False senão
def searchInRegion(divided, num, i, j):
    # Retorna os indices da região que deve ser avaliada
    regionLine = getRegionIndex(i)
    regionCol = getRegionIndex(j)
    # Retorna a matriz 3x3 da região que deve ser analisada
    region = divided[regionLine][regionCol]
    # Procura o número na matriz 3x3 da região
    # True se encontra, False senão
    for i in range(3):
        for j in range(3):
            x = region[i][j]
            if x == 0 or x != num:
                continue
            else:
                return True
    return False

# Função: Dividir sudoku
#   Divide a matriz do jogo em uma matriz bimensional de matrizes 3x3,
#   onde cada matriz 3x3 representa uma região (quadradinho) do jogo
# Parametros:
#   sudoku:     tabela do jogo sudoku 9x9
# Retorno:
#   Uma matriz bimensional 3x3 onde cada posição possui uma matriz 3x3
#   correspondente as sub-matrizes 3x3 da matriz do jogo
def divide(sudoku):
    r = []
    step = 3
    for z in range(3):
        a,b,c = [],[],[]
        for line in range(step - 3, step):
            st, nd, rd = [], [], []
            for x in range(3):
                st.append(sudoku[line][x])
            for x in range(3,6):
                nd.append(sudoku[line][x])
            for x in range(6,9):
                rd.append(sudoku[line][x])
            a.append(st)
            b.append(nd)
            c.append(rd)
        l = [a,b,c]
        r.append(l)
        step += 3
    return r

# Função: Pega indice da região
#   Esta função procura qual o indice da região correspondente na matriz dividida do sudoku
#   baseado no indice dado.
#   Se for passado um indice de linha, ela retornará o indice da linha da região,
#   assim também como de coluna.
# Parametros:
#   index:      indice (0-8) da posição que deseja saber o indice da regiao 
# Retorno:
#   Indice da região baseado no indice passado
def getRegionIndex(index):
    # Cria uma matriz que servirá de guia para localização da região a ser procurada
    indexes = [
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ]
    # Baseado no indice da posicao recebido, retorna qual o indice da região correspondente
    for i in range(3):
        for j in range(3):
            if indexes[i][j] == index:
                # indice da região
                return i