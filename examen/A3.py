def  posYneg ( arr ):
    positivos = 0
    negativos = 0
    para i en  rango ( len (arr)):
        if (arr [i] > 0 ):
            positivos = positivos + 1
        más :
            Negativos = Negativos + arr [i]
    print ( " El número de los positivos es: " +  str (positivos))
    de impresión ( " La Suma de los Negativos es: " +  str (Negativos))


posYneg ([ 9 , - 8 , 2 , 1 , - 2 ]) # 3 positivos, -10 negativos