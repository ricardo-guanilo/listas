# Se crea una lista vacía donde se guardarán los números ingresados por el usuario
numeros = []

print("Ingresa números para la lista. Escribe 'fin' para terminar.\n")

# Ciclo infinito que pide al usuario ingresar números
while True:
    valor = input("Número (o 'fin' para terminar): ")

    # Si el usuario escribe "fin", se rompe el ciclo con 'break'
    if valor.lower() == "fin":
        break
    else:
        # Convierte el valor ingresado a entero y lo agrega a la lista
        numeros.append(int(valor))

# Si la lista está vacía, significa que el usuario no ingresó ningún número
if len(numeros) == 0:
    print("\nNo ingresaste ningún número.")
else:
    # Si hay números, se pide un número para buscar en la lista
    valor_buscar = int(input("\nIngresa el número que deseas buscar: "))

    # Se crea una lista vacía para guardar las posiciones donde aparece el número buscado
    posiciones = []

    # Ciclo que recorre la lista usando índices (0, 1, 2, ...)
    for i in range(len(numeros)):
        # Si el número en la posición 'i' es igual al buscado, se guarda su posición
        if numeros[i] == valor_buscar:
            posiciones.append(i)

    # Si la lista de posiciones tiene elementos, significa que el número fue encontrado
    if posiciones:
        print(f"\nEl número {valor_buscar} aparece en las posiciones:", posiciones)
    else:
        # Si la lista de posiciones está vacía, el número no está en la lista
        print(f"\nEl número {valor_buscar} no se encuentra en la lista.")
