#Simular el Funcionamiento del Operador incorporado in
#nos permite comprobar sobre una colección, si el elemento está dentro de ella
#print (5 in [2,3,4,5]) ->true
#print (k in 'jddfk') ->true

def pertenece_a(lista, elemento):
    """
    Comprueba si un elemento está en una lista.
    """
    for e in lista:
        if elemento == e: # elemento a buscar == posicion actual de la lista
            return True
    return False

print(pertenece_a([1,2,3,4],4))
print(pertenece_a([1,2,3,4],5))


