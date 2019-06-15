

def main():
    n = int(input())
    m = matrixRead(n)
    matrixPrint(m)

def matrixRead(n):
    mat = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = int(input())
    return mat



def matrixPrint(matrix):
    if (matrix != []):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m - 1):
                print(matrix[i][j], end=' ')
            print(matrix[i][j + 1])
    else:
        print('[]')

main()