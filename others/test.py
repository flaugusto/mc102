m = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def findNext(resposta):
    lines = len(resposta)
    cols = len(resposta[0])
    
    # Acha a próxima posição vazia na linha corrente (considerando os critérios)
    #   Números na linha, coluna e região devem ser distintos


    # Encontra os valores possíveis para a posição
    # Para cada valor possível, testa o proximo (chama a função novamente)


# Gerador numeros válidos
#   Gera as possibilidades de números para uma dada posição
# Parametros:
#   sudoku:     A matriz do jogo sudoku 9x9
#   i:          A posicao da linha para encontrar os números possíveis
#   j:          A posição da coluna para encontrar os números possíveis
# Retorno:
#   Um iterável contendo cada possibilidade encontrada para a posição
def validNumbers(sudoku, i, j):
    nums = [1,2,3,4,5,6,7,8,9]      # possibilidades iniciais
    ret = True     # controlador para validar se o numero pode ser retornado
    # para cada número de 1 a 9, testa se ele é possível e gera

    #
    #
    def searchInLine():
        for x in sudoku[i]:
            if x != 0 and x != num:
                continue
            else:
                return False
        return True
    #
    #
    def searchInColumn():
        for line in sudoku:
            for x in range(j, j + 1):
                if line[x] != 0 and line[x] != num:
                    continue
                else:
                    return False
        return True
    #
    #
    def searchInRegion():
        divided = divide(sudoku)    # Divide a matriz do sudoku em matrizes 3x3 individuais
        # Retorna os indices da região que deve ser avaliada
        regionLine = getRegionIndex(i)
        regionCol = getRegionIndex(j)
        # Retorna a matriz 3x3 da região que deve ser analisada
        region = divided[regionLine][regionCol]
        for i in range(3):
            for j in range(3):
                x = region[i][j]
                if x !=0 and x != num:
                    continue
                else:
                    ret = False
    for num in nums:
        # Verifica as possibilidades na linha da posição
        # Verifica as possibilidades na coluna
        
        # Verificar as possibilidades para a região        
       
        if ret:
            yield num
        else:
            continue
    return None

# print(validNumbers(m, 0,2))

def divide(sudoku):
    r = []
    step = 3
    for z in range(3):
        a,b,c = [],[],[]
        for line in range(step - 3, step):
            st, nd, rd = [], [], []
            for x in range(3):
                st.append(m[line][x])
            for x in range(3,6):
                nd.append(m[line][x])
            for x in range(6,9):
                rd.append(m[line][x])
            a.append(st)
            b.append(nd)
            c.append(rd)
        l = [a,b,c]
        r.append(l)
        step += 3
    return r

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

# print(findRegion(6))