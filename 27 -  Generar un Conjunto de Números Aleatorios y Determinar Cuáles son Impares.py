#  Generar un Conjunto de Números Aleatorios y Determinar Cuáles son Impares
# K mod 2 == 1 -> impar

from random import randint
                     #expresion for valor in iterable
numeros_aleatorios = [randint(1,100) for num in range(30)] #me va a devolver 30 numeros por cada num en el rango entre 1 y 100

#print(numeros_aleatorios)
#----------primer método usando filter------------
numeros_impares = filter(lambda  nro: nro % 2 == 1, numeros_aleatorios)
#print(numeros_impares)#objeto de tipo filter
print(list(numeros_impares))

#----------segundo método ------------------------

def encontrar_impares(lista):
    impares = []
    for n in lista:
        if n % 2 == 1:
            impares.append(n)
    return impares

print (encontrar_impares(numeros_aleatorios))
