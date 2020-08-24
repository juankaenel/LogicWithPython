#emular el funcionamiento de la funcion join para concatenar una lista
numeros = [2,3,4,7,10]
# 234710
#con list comprehension
#list = [ expresion for valor in iterable if condicion] siendo la condicion opcional

#print(''.join([str(n) for n in numeros])), me va a devolver un join por cada n in numeros

#sin list comprehension
#for n in numeros:
#    print (''.join(str(n)),end='')

def concatenar_lista(lista):
    """
    Emula el funcionamiento de join
    """
    resultado = ''
    for n in lista:
        resultado += str(n)
    return resultado

print(concatenar_lista(numeros))
