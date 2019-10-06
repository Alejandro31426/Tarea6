def  divisibles Por ( lista , n ):
    lista_nueva = []
    para i en  rango ( len (lista)):
        if (lista [i] % n == 0 ):
            lista_nueva.append (lista [i])
    imprimir (lista_nueva)
volver lista_nueva

divisiblesPor ([ 1 , 2 , 3 , 4 , 5 , 6 ], 2 ) # [2,4,6]
divisibles Por ([ 9 , 12 , 3 , 0 , 1 , 4 ], 3 ) # [9, 12, 3]
divisiblesPor ([ 10 , 11 , 3 ], 1 ) # [10, 11, 3]