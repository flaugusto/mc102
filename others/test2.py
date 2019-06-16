sudoku = [
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
def test(i, j):
    def test2():
        print(i,j)
    test2()


def searchInRegion(num, i, j):
        # Divide a matriz do sudoku em uma matriz 3x3 de matrizes 3x3 individuais
        divided = divide(sudoku)   
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
for x in range(1,10):
    print(x, searchInRegion(x, 0, 2))
