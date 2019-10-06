def  repetidos ( lista_original ):
    lista_nueva = []
    conta = 0
    para j en  rango ( len (lista_original)):
        conta = 0
        para i en  rango ( 0 , len (lista_original)):
            if (lista_original [j] == lista_original [i]):
                conta = conta + 1 
        si (conta == 1 ):   
            lista_nueva.append (lista_original [j])
    imprimir (lista_nueva)
    volver lista_nueva

repetidos ([ 9 , 3 , 1 , 3 , 2 , 9 ]) # [1,2]
repetidos ([ 6 , 2 , 2 , 2 , 1 , 8 ]) # [6,1,8]
repetidos ([ 1 ]) # [1]