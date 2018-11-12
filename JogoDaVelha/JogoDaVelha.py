def ImprimirTabuleiro(pos):
    for i in range(0,3):
        for j in range (0,3):
            if pos[i][j] == 0:
                print('_', end = " ")
            elif pos[i][j] == 1:
                print('x', end = " ")
            elif pos[i][j] == 2:
                print('o', end = " ")
        print(" ")
pos = [[1,0,2],[1,0,2],[1,0,2]]

ImprimirTabuleiro(pos)

