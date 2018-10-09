
def verify (matriz, define, lista, variavel): #this function verify who won or if got a tie
    mtz_1 = matriz [0]
    mtz_2 = matriz [1]
    mtz_3 = matriz [2]
    # verify the lines
    if mtz_1[0] == mtz_1 [1] and mtz_1 [1] == mtz_1 [2] and mtz_1[0] != " ":
        if define [lista [0]] == mtz_1 [0]:
            print "\nParabens %s, voce ganhou\n" % lista[0]
        else:
            print "\nParabens %s, voce ganhou\n" % lista[1]
        return True
    elif mtz_2[0] == mtz_2 [1] and mtz_2 [1] == mtz_2 [2] and mtz_2[0] != " ":
        if define [lista [0]] == mtz_2 [0]:
            print "\nParabens %s, voce ganhou\n" % lista[0]
        else:
            print "\nParabens %s, voce ganhou\n" % lista[1]
        return True
    elif mtz_3[0] == mtz_3 [1] and mtz_3 [1] == mtz_3 [2]and mtz_3[0] != " ":
        if define [lista [0]] == mtz_3 [0]:
            print "\nParabens %s, voce ganhou\n" % lista[0]
        else:
            print "\nParabens %s, voce ganhou\n" % lista[1]
        return True
    # verify the columns
    elif mtz_1[0] == mtz_2 [0] and mtz_1 [0] == mtz_3 [0] and mtz_1[0] != " ":
        print "1"
        if define [lista [0]] == mtz_1 [0]:
            print "\nParabens %s, voce ganhou\n" % lista[0]
        else:
            print "\nParabens %s, voce ganhou\n" % lista[1]
        return True
    elif mtz_1[1] == mtz_2 [1] and mtz_2 [1] == mtz_3 [1] and mtz_1[1] != " ":
        print "2"
        if define [lista [0]] == mtz_1 [1]:
            print "\nParabens %s, voce ganhou\n" % lista[0]
        else:
            print "\nParabens %s, voce ganhou\n" % lista[1]
        return True
    elif mtz_1[2] == mtz_2 [2] and mtz_1 [2] == mtz_3 [2]and mtz_1[2] != " ":
        print "3"
        if define [lista [0]] == mtz_1 [2]:
            print "\nParabens %s, voce ganhou\n" % lista[0]
        else:
            print "\nParabens %s, voce ganhou\n" % lista[1]
        return True
    # verify the diagonals
    elif mtz_1[0] == mtz_2 [1] and mtz_2 [1] == mtz_3 [2] and mtz_1[0] != " ":
        print "4"
        if define [lista [0]] == mtz_1 [0]:
            print "\nParabens %s, voce ganhou\n" % lista[0]
        else:
            print "\nParabens %s, voce ganhou\n" % lista[1]
        return True
    elif mtz_1[2] == mtz_2 [1] and mtz_1 [2] == mtz_3 [0] and mtz_1[2] != " ":
        print "5"
        if define [lista [0]] == mtz_1 [2]:
            print "\nParabens %s, voce ganhou\n" % lista[0]
        else:
            print "\nParabens %s, voce ganhou\n" % lista[1]
        return True
    # verify if got a tie
    elif variavel == 9:
        print "\nDEU VELHA!\n"
        return True            
    return False
