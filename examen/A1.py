def  aUno ( arr ):
    total = 45
    aux = 0
    i = 0
    para i en  rango ( len (arr)):
        aux = aux + arr [i]
    if (total == aux y  len (arr) == 10 ):
        print ( " No falta ninguno " )
    más :
        print ( " Falta el número " +  str (total - aux))

arr = [ 2 , 1 , 9 , 3 , 8 , 7 , 4 , 6 , 0 ] # falta 5
arr2 = [ 2 , 1 , 9 , 3 , 8 , 7 , 4 , 6 , 5 ] # falta 0
arr3 = [ 2 , 1 , 9 , 3 , 8 , 7 , 4 , 6 , 0 , 5 ] # no falta ninguno

aUno (arr)
aUno (arr2)
aUno (arr3)