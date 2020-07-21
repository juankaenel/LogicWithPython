#Emular el funcionamiento del Producto de Cadenas de Caracteres
#print('hola '*3)

def emular(cadena,repeticion):
    """
    Emula el funcionamiento del producto de cadenas
    """
    resultado=''

    for i in range(repeticion):
        resultado += cadena

    return resultado

print(emular('hola',4))

