#Calcular la Diferencia de Conjuntos con Elementos con Nombres de Colores
colores_lista1=['rojo','negro','azul','amarillo','rojo','violeta']
colores_lista2=['rojo','blanco','azul','amarillo'] #negro y violeta no tiene esta lista
#trabajamos con teoria de conjuntos
# A, B ; A -B ;  A / B;

colores_conjunto1 = set(colores_lista1)
colores_conjunto2 = set(colores_lista2) #seteamos los colores
diferencia = colores_conjunto1.difference(colores_conjunto2) #gracias al set puedo hacer uso del método difference que encontrará los valores de lista diferentes
print(diferencia)