def  multi ( lista ):
    "" "
    Esta función entrega la multiplicación de los números de una lista
    
    "" "
    res =  1
    para i en  rango ( len (lista)):
        res = res * lista [i]        
    volver res

prueba1 = [ 1 , 2 , 3 , 4 ] # 24
prueba2 = [ 1 , 2 ] # 2
print (multi (prueba1))
print (multi (prueba2))