#Crear un Histograma a partir de una Lista de Enteros

# [2,5,4,5] representamos con algún signo
# **
# *****
# ****
# *****

def crear_histograma(lista,caracter='*'):
    """
    Crea un histograma a partir de una lista y un caracter específico, por default *
    """
    for e in lista:
        #primer método
        print(caracter * e)

        #segundo método
        #for i in range(e):
        #    print(caracter, end='')
        #print()


crear_histograma([1,2,3])
