#Crear una Función para Determinar si un Número es Cercano a 1000 o 2000

#abs->valor absoluto
def cercania(n):
    """Comprueba si un número dado es cercano a 1000 o 2000"""
    # n = 900 , 1000-900 <= 100 ->si, es  cercano!
    return (abs(1000-n) <= 100 ) or (abs(2000-n) <= 100)

print(cercania(1000))
print(cercania(940))

print()

print(cercania(2000))
print(cercania(1900))
print(cercania(3900))


