# Comprobar si un caracter dado es una vocal

# a,e,i,o,u
#vocales = ['a','e','i','o','u']

#caracter = input('Ingrese un caracter: ')

#for i in range(0, len(vocales)):
    # if caracter == vocales[i]:
    #     print('Es una vocal')
    #     break
    # else:
    #     print('No es una vocal')
    #

    #if caracter != vocales[i]:
    #    continue
    #else:
    #    print('Es una vocal')

def es_vocal(c):
    """
    Comprueba si un caracter es vocal
    """
    if len(c)==1:
        vocales = 'aeiou'
        c = c.lower()
        if c in vocales:
            print('Es una vocal')
        else:
            print('No es una vocal')

        return ''

print(es_vocal('a'))