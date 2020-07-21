#Comprobar si una Cadena de Caracteres Termina con la Extensión .py

archivo = input('Ingrese el nombre de un archivo con extensión .py ')

def validar_archivo(archivo):
    if len(archivo) >= 3 and archivo[-3:] == '.py':
        return archivo
    else:
        return archivo + '.py'

print(validar_archivo(archivo))