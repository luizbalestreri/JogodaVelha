import os
def clear():
    os.system( 'cls' ) 

def ImprimirTabuleiro(pos):
    clear()
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

def ReceberComando():
    i = int(input ("Por favor, insira o número da linha para posicionar:")) - 1
    j = int(input ("Por favor insira a coluna para posicionar:")) - 1
    if pos[i][j] != 0:
        print('posição ocupada, aperte enter para continuar')
        input()
        ImprimirTabuleiro(pos)
        ReceberComando()
    else: pos[i][j] = x


def VerificarGanhador():
    for i in range(0,3):
        if pos[i][0] > 0:
            if pos[i][0] == pos[i][1] and pos[i][2] == pos [i][1]:
                return pos[i][0]
    for i in range(0,3):
        if pos[0][i] > 0:
            if pos[0][i] == pos[1][i] and pos[1][i] == pos [2][i]:
                return pos[0][i]
    if pos[1][1] > 0:
        if pos[0][0] == pos [1][1] and pos [1][1] == pos [2][2]:
            return pos[0][0]
        if pos[0][2] == pos [1][1] and pos [1][1] == pos[2][0]:
            return pos[1][1]
    return 0

for n in range (0,9):
    if n%2 == 0:
        x = 1
    else:
        x = 2
    ImprimirTabuleiro(pos)
    if VerificarGanhador() > 0:
        if VerificarGanhador() == 1:
            print('X ganhou')
            break;
        elif VerificarGanhador() == 2:
            print('O ganhou')
            break;
    ReceberComando()
    

