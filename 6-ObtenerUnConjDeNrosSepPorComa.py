entrada = input('Ingres un conjunto de numeros separados por coma: ')
#esto va a estar en formato str..

print(entrada.split(',')) # me pasa a una lista separada por comas
print(entrada.format_map(',')) # me transforma a str
print(type(entrada))
