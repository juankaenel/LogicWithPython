# Calcular el Máximo Máximo Común Divisor (MCD) de Dos Números
# El número más grande que divide dos números
# from math import gcd -> py ya cuenta con una función para realizar esto

def mcd(x,y):
    mcd = 1 # 1 porque es generalmente el máximo común divisor de dos nros cuando no hay otro

    if x % y ==0: #8 % 4  == 0 -> 8 es divisible por 4 y  4 es divisible por 4
        return y

    for k in range(int(y/2),0,-1): #y = 17 -> y/2 = 8.5 -> 8 en cada ciclo baja 1 hasta el 1
        if x % k == 0 and y % k ==0:
            mcd = k
            break

    return mcd

print(mcd(20,25))
print(mcd(8,4))
print(mcd(17,12))
