#Imprimir el calendario para un año y mes específico

import calendar

agnio = int(input('Ingrese el año: '))
mes = int(input('Ingrese el mes: '))

print(calendar.month(agnio,mes))