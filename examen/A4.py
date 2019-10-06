def  prometido ( arr ):
    suma =  0
    para x en el  rango ( 0 , len (arr)):
        suma + = arr [x]
    promedio = suma /  len (arr)
    retorno promedio
def  aprobados ( alumnos ):
    aproba =  0
    para i en  rango ( 0 , len (alumnos)):
        si es prometido (alumnos [i]) > =  6 :
            aproba + =  1
    resultado = aproba /  len (alumnos)
    devolver resultado *  100


prueba10 = [[ 9 , 8 , 7 , 5 , 2 ], [ 5 , 5 , 5 , 5 , 5 , 5 ], [ 0 , 1 , 2 ], [ 4 , 2 , 4 , 5 , 7 , 8 ] , [ 1 , 1 , 1 , 1 ]] # 20
print (aprobados (prueba10), " % " )
