def  prometido ( arr ):
    suma =  0
    para x en el  rango ( 0 , len (arr)):
        suma + = arr [x]
    promedio = suma /  len (arr)
    retorno promedio

def  promLista ( arreglo ):
    suma =  0
    para i en  rango ( 0 , len (arreglo)):
        suma + = prometido (arreglo [i])
    devolver suma

prueba1 = [[ 1 , 2 , 2 , 2 , 2 , 1 ], [ 2 , 1 ]] # 3.1
prueba2 = [[ 10 , 5 ], [ 6 , 2 , 2 ], [ 1 ]] # 11.8
print (promLista (prueba1))    
print (promLista (prueba2))  