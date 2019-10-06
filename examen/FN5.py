def  promedio ( valores , pos ):
    resultado =  0.0
    para x en el  rango ( 0 , len (valores)):
        si x ! = pos:
            resultado = resultado + valores [x]
    regresa = resultado / ( len (valores) - 1 )      
    retorno regresa

def  sacaLider ( listas ):
    anterior = - 1
    resultado = []
    para i en  rango ( 0 , len (listas)):
        si listas [i] > promedio (listas, i):
            resultado.append (listas [i])
            anterior = listas [i]
    si anterior > =  0 :
        devolver resultado
    más :
        print ( " No hay lider de heno " )


a = [ 3 , 2 , 10 , 1 ] # 10
b = [ 5 , 0 , 1 , 2 ] # 5
c = [ 1 , 1 , 4 , 1 ] # 4

# print (promedio (lider, 0))
print (sacaLider (a))
print (sacaLider (b))
imprimir (sacaLider (c))