#obtener extension de un archivo q nos de un usr

nombre_archivo = input('Ingrese el nombre del archivo: ')

partes_nombre_archivo = nombre_archivo.split('.') #el separador de las cadenas es el .

print(partes_nombre_archivo)


print(partes_nombre_archivo[-1])

