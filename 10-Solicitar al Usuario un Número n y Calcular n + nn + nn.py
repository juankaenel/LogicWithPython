#Solicitar al usuario un número n y calcular n + nn +nnn

n = input('Ingrese un número n: ')

#n = 3 , nn = 33, nnn= 333

#una forma
nn = int('{}{}'.format(n,n))
#otra forma
nnn = int('%s%s%s' % (n,n,n))

print(f'n: {n}, nn: {nn}, nnn: {nnn}')