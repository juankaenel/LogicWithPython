def sumar_numeros(a,b,c):
    """
    Calcula la suma de tres números. Si los tres son iguales,
    la suma se multiplica por tres
    """

    suma = a + b + c

    if a == b and a==c: #por ley de transitividad, si a == b y a == c entonces b == c
        suma *= 3 # suma = suma * 3

    return suma

print(sumar_numeros(2,2,2)) #6*3 = 18
print(sumar_numeros(2,2,3)) # = 7