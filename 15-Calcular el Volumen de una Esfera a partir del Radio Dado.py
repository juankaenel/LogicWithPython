# calcular el volumen de una esfera a partir del radio dado
#https://www.wolframalpha.com/input/?i=volume%20of%20a%20sphere
# vol = (4/3 * pi * r^3)

from math import pi

radio = float(input('Ingrese el radio: '))

volumen = (4/3 * pi * (radio** 3))

print(f'El volúmen de la esfera de radio {radio} es: {volumen}')