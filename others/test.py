m = [
    [87,65,86,121,174],
    [90,65,50,72,163],
    [112,77,56,66,157],
    [108,74,53,87,177],
    [72,57,66,126,197]
]
core = [
    [1,0,0],
    [0,0,0],
    [0,0,0]
]
global w, h
w, h = len(m), len(m[0])
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
                    # print('(', core[x][y], ' x ', matrix[i + offset[x]][j + offset[y]], ')')
            newPixel = numerator//divider
            # print(newPixel)
            # Limitação para o máximo suportado no PGM
            if newPixel < 0:
                newPixel = 0
            elif newPixel > 255:
                newPixel = 255
            result[i][j] = newPixel
            
    return result

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

def deepcopy(arr):
    b = []
    for line in arr:
        l = []
        for col in line:
            l.append(col)
        b.append(l)
    return b


matrixPrint(m)
print('-----')
matrixPrint(convolution(m, core, 1))
