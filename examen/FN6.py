def  sumDif ( arr ):
    para i en  rango ( len (arr)):
        diferencia = arr [ 0 ]
        diferencia = diferencia - arr [i]
    imprimir (diferencia)
    volver diferencia


sumDif ([ 10 , 2 , 1 ]) # (10 - 2) + (2 - 1) = 9
sumDif ([ 11 , 10 , 5 ]) # ( 11-10 ) + ( 10-5 ) = 6
sumDif ([ 4 , 3 , 2 , 1 ]) # (4 - 3) + (3 - 2) + (2 - 1) = 3