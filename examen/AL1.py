lista_primos = []
lista_noprimos = []
lista = []
para i en  rango ( 2 , 101 ):
    lista.append (i)
imprimir (lista)
para j en el  rango ( 2 , 101 ):
    si ((j % 2 ! = 0  o j == 2 ) y (j % 3 ! = 0  o j == 3 ) y (j % 5 ! = 0  o j == 5 ) y (j % 7 ! = 0  o j == 7 ) y (j % 11 ! = 0  o j == 11 )):
        lista_primos.append (j)
    más :
        lista_noprimos.append (j)
print ( " Los primos son: " + str (lista_primos))
print ( " Los no primos son: " + str (lista_noprimos))