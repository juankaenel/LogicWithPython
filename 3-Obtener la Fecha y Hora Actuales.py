#ejercicio 2 Obtener fecha y hora actuales

import datetime

ahora = datetime.datetime.now()
print(ahora)

print(type(ahora))

print(ahora.strftime('%d/%m/%Y %H:%M:%S'))  #12/05/2020 21:13:19

