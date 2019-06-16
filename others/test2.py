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
####### Função recursiva principal #######

def findNextZero(sudoku):
    
    # Acha a próxima posição vazia na linha corrente 
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for valid in val
findNextZero(sudoku)

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

# matrixPrint(sudoku)