# Calcular el Área de un Triángulo

base = None
altura = None

while True:
    try:
        base = float(input('Ingrese la base del triángulo: '))
        break
    except:
        print('Debe escribir un numero')

while True:
    try:
        altura = float(input('Ingrese la altura del triángulo: '))
        break
    except:
        print('Debe escribir un numero')

area = (base*altura/2)
print('El área del triángulo es: ',area,' metros')