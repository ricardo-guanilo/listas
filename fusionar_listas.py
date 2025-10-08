# Fusionar listas
lista_1 = []
lista_2 = []
fusion = []
while True:
    try:
        n = input('Ingrese valores para la primera lista o escriba \'fin\' para ir a la segunda: ')
        if n.lower() == 'fin':
            break
        else:
            n = int(n)
    except:
        print('ERROR: ingrese un número entero o \'fin\'')
    else:
        lista_1.append(n)
while True:
    try:
        n2 = input('Ingrese valores para la segunda lista o escriba \'fin\' para fusionar las listas: ')
        if n2.lower() == 'fin':
            break
        else:
            n2 = int(n2)
    except:
        print('ERROR: ingrese un número entero o \'fin\'')
    else:
        lista_2.append(n2)
lista_1.extend(lista_2)
for termino in lista_1:
    if termino not in fusion:
        fusion.append(termino)
fusion.sort()
print(f'Lista fusionada: {fusion}')

