

def main():
    n = int(input())
    m = matrixRead(n)
    matrixPrint(m)

def matrixRead(n):
    mat = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = float(input('Insira aqui na pos (%d, %d): ' %(i + 1, j + 1)))
    return mat



def matrixPrint(matrix):
    if (matrix != []):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                print('%2.f ' %matrix[i][j], end='')
            print()
main()