#obtener la representacion inversa de una cadena de caracteres

#Python => nohtyP

cadena = 'Python'
#range empieza en la ultima pos, va hasta 0 y disminuyendo
for i in range(len(cadena)-1,-1 , -1):
    print(cadena[i],end='')

print()

#método mas rapido
cadena2 = 'PyCharm'
print(cadena2[::-1])
