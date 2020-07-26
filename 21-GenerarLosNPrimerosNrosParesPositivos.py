# Generar los n primeros nros pares positivos

# k es par si mod 2 == 0 => k es par

def generar_nros_pares(n=100):
    """
    Genera los n nros pares positivos
    """
    pares = []
    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        numero += 1
    return pares


n = int(input('Ingrese la cantidad de números pares positivos a generar'))
if n > 0:
    pares = generar_nros_pares(n)
    print(pares)
    print('Cantidad de números pares: ', len(pares))
else:
    print('El nro debe ser positivo')
#######################################################################################################################
pares1 = []
nro = int(input('Ingrese un nro: '))

for i in range(0,nro+1):
    if i % 2 ==0:
        pares1.append(i)

print(pares1)
print('Cantidad de números pares: ', len(pares1))

