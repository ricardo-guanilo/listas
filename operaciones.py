## operaciones.py
lista = []
while True:
    try:
        numero = (input('''Ingrese valores para calcular las siguientes operaciones
Suma, Promedio, Máximo y Mínimo
Ingrese \'fin\' para salir.
'''))
        if numero == 'fin':
            break
        else:
            numero = float(numero)
    except:
        print('ERROR: ingrese un númeo real')
    else:
        lista.append(numero)
print(f'''
Suma: {sum(lista)}
Promedio: {sum(lista)/len(lista):.2f}
Máximo: {max(lista)}
Mínimo: {min(lista)}
''')


    