#Crear una Subcadena de n Caracteres Replicada n Cantidad de Veces
#'Python' => n=2 , 'Py' => 'PyPy'
def replicar_subcadena(cadena, n):
    nro_caracteres = n

    if nro_caracteres > len(cadena):
        nro_caracteres = len(cadena) #en caso que mi longitud de cadena sea 4 y el valor ingresado sea 6 igualo a 4

    subcadena = cadena[:nro_caracteres] #subcadena va desde 0 hasta el nro de caracteres

    resultado = ''

    for i in range(n):
        resultado += subcadena

    return resultado

print(replicar_subcadena('juanito',2))