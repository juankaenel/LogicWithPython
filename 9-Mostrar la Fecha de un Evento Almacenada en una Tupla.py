#Mostrar la fecha de un evento almacenada en un tupla

fecha_evento = (2020,9,14)

#print(fecha_evento)

#primera opción
print('El evento programado será en la fecha: ', fecha_evento)

#segunda opción
print('El evento programado será en la fecha:  %i/%i/%i' % fecha_evento) # %i es integer -> mapeamos cada uno de los elementos de fecha_evento

#tercera opción
agnio, mes, dia = fecha_evento

print('El evento programado será en la fecha: {}/{}/{}'.format(agnio,mes,dia))
