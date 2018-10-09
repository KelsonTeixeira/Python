import os 
import biblioteca_velha

def main (): #the principle one, it calls all functions
    os.system ("clear")
    define = nome()
    define = xo(define)
    matriz = mtz ()
    jogo(define, matriz)
    novo_jogo()

def nome (): # this function recieve the names of players, allocate it, prints and return theses names
    jogador_1 = raw_input ("Jogador 1, qual o seu nome? ")
    print 
    jogador_2 = raw_input ("Jogador 2, qual o seu nome? ")
    print
    print
    print ("%s vs %s" % (jogador_1, jogador_2))
    print 
    print
    nomes = {jogador_1: [], jogador_2: []}
    return nomes

def xo (define): #this function let the player choose wich character he/she will use, allocate it and return a dictionary with this information
    lista_nome = define.keys()
    while True:
        define [lista_nome[0]] = raw_input("%s o que voce escolhe, X ou O? " %lista_nome[0])
        define[lista_nome[0]] = define[lista_nome[0]].upper()
        if define [lista_nome[0]] == "X" or define [lista_nome[0]] == "O":
            break
        else:
            print "Resposta Invalida!"
    os.system ("clear")
    if define[lista_nome[0]] == "X":
        define[lista_nome[1]] = "O"
        print ("\n%s, lhe restou o O" %lista_nome[1])
    else:
        define[lista_nome[1]] = "X"
        print ("\n%s, lhe restou o X" %lista_nome[1])
    print
    print ("Ficou entao:\n")
    print ("%s: %s\n" % (lista_nome[0], define[lista_nome[0]]))
    print ("%s: %s\n" % (lista_nome[1], define[lista_nome[1]]))
    x = raw_input("Podemos comecar? Y/N? ")
    return define

def mtz (): # this function creates a list of three lists and return it (matrix)
    mtz_1 = [" ", " ", " "]
    mtz_2 = [" ", " ", " "]
    mtz_3 = [" ", " ", " "]
    matriz = [mtz_1, mtz_2, mtz_3]
    return matriz

def guarda (matriz,coordenada, lista, i, define): #this function allocates the "coordenada" where the player ask to
    mtz_1 = matriz [0]
    mtz_2 = matriz [1]
    mtz_3 = matriz [2]
    if coordenada[0] == "1":
        mtz_1 [int(coordenada[1]) - 1] = define [lista[i]]
    elif coordenada[0] == "2":
        mtz_2 [int(coordenada[1]) - 1] = define [lista[i]]
    else:
        mtz_3 [int(coordenada[1]) - 1] = define [lista[i]]
    matriz = [mtz_1, mtz_2, mtz_3]
    return matriz

def printf (matriz): #This function prints the matrix in the format of the game
    mtz_1 = matriz [0]
    mtz_2 = matriz [1]
    mtz_3 = matriz [2]
    print "    1   2   3\n"
    print "1   %s | %s | %s" % (mtz_1[0], mtz_1[1], mtz_1[2])
    print "   -----------"
    print "2   %s | %s | %s" % (mtz_2[0], mtz_2[1], mtz_2[2])
    print "   -----------"
    print "3   %s | %s | %s" % (mtz_3[0], mtz_3[1], mtz_3[2])
    print

def novo_jogo(): #this function ask to the player if he/she wants to play again
    op = raw_input ("Jogar Novamente? Y/N? ")
    print 
    op.lower()
    if op == "y":
        main ()
    elif op == "n":
        print
    else: 
        print "Resposta Invalida\n"
        novo_jogo()
    

def jogo (define, matriz): #this fuction runs the game
    lista = define.keys()
    i = 0
    j = 1
    lista_1 = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
    while True:
        os.system ("clear")
        printf (matriz)
        while True:
            coordenada = raw_input("%s,qual a coordenada voce deseja? " % lista[i])
            if coordenada in lista_1:
                break
            else:
                print "Resposta Invalida"
        matriz = guarda (matriz,coordenada, lista, i, define)
        if biblioteca_velha.verify (matriz, define, lista, j):
            printf (matriz)
            break
        j += 1
        if i == 0:
            i = 1
        else:
            i = 0

if __name__ == '__main__':
    main()