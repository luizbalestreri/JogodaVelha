import os
def clear():
    os.system( 'cls' ) 

def ImprimirTabuleiro(pos):
    for i in range(0,3):
        print(i + 1, end = " :")
        for j in range (0,3):
            if pos[i][j] == 0:
                print('| _ |', end = " ")
            elif pos[i][j] == 1:
                print('| X |', end = " ")
            elif pos[i][j] == 2:
                print('| O |', end = " ")
        print(" ")
    print('     1     2     3')
pos = [[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,9):
    if i%2 == 0:
        x = 1
    else:
        x = 2
    clear()
    ImprimirTabuleiro(pos)
    i = int(input ("Por favor, insira o número da linha para posicionar:")) - 1
    j = int(input ("Por favor insira a coluna para posicionar:")) - 1
    pos[i][j] = x

