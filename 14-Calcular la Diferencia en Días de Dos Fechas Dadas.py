#Calcular la Diferencia en Días de Dos Fechas Dadas

from datetime import date

fecha_actual = date(2020,7,18)
otra_fecha = date(2021,7,18)

delta = otra_fecha-fecha_actual
print(delta) #365 days, 0:00:00
print(delta.days) #365
