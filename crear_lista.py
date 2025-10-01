## Crear_lista.py
lista = []
while True:
    try:
        n = input('Ingrese número para agregar a la lista, o escriba \'fin\' para salir: ')
        if  n == 'fin':
            break
        else:
            n = float(n)
    except:
        print('ERROR: ingrese un número real')
    else:
        lista.append(n)
print(f'Lista generada: {lista}')