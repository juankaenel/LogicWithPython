def evaluar(num):
    """
    Calcula la diferencia del valor pasado como argumento. Se deben seguir dos reglas
    """
    if num<=15:
        return 15 - num
    else:
        return (15- num) *2

print(evaluar(15))