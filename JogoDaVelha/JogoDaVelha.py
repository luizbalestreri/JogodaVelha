import os
def clear():
    os.system( 'cls' ) 

def ImprimirTabuleiro(pos):
    for i in range(0,3):
        for j in range (0,3):
            if pos[i][j] == 0:
                print(j, end = " ")
            elif pos[i][j] == 1:
                print('x', end = " ")
            elif pos[i][j] == 2:
                print('o', end = " ")
        print(" ")
pos = [[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,9):
    if i%2 == 0:
        x = 1
    else:
        x = 2
    clear()
    ImprimirTabuleiro(pos)
    i = int(input ("Por favor, insira o número da linha para posicionar:"))
    j = int(input ("Por favor insira a coluna para posicionar:"))
    pos[i][j] = x

