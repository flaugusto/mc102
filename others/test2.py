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