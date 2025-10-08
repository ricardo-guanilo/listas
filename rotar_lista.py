
# Se crea una lista vacía donde se guardarán los números
numeros = []

print("Ingresa números para la lista. Escribe 'fin' para terminar.\n")

# Ciclo para leer los números del usuario
while True:
    valor = input("Número (o 'fin' para terminar): ")
    if valor.lower() == "fin":
        break
    else:
        numeros.append(int(valor))

# Verificar que la lista no esté vacía.
if len(numeros) == 0:
    print("\nNo ingresaste ningún número.")
else:
    # Mostrar la lista original
    print("\nLista original:", numeros)

    # Preguntar hacia qué dirección rotar
    direccion = input("¿Deseas rotar a la 'derecha' o a la 'izquierda'? ").lower()

    # Pedir la cantidad de posiciones a rotar
    n = int(input("¿Cuántas posiciones deseas rotar?: "))

    # Ajustar el valor de n para que no sea mayor que el tamaño de la lista
    n = n % len(numeros)

    # Rotar a la derecha
    if direccion == "derecha":
        # Los últimos n elementos se mueven al inicio
        rotada = numeros[-n:] + numeros[:-n]

    # Rotar a la izquierda
    elif direccion == "izquierda":
        # Los primeros n elementos se mueven al final
        rotada = numeros[n:] + numeros[:n]

    # Si el usuario escribió otra palabra
    else:
        print("Dirección no válida. Debes escribir 'derecha' o 'izquierda'.")
        rotada = numeros  # No se modifica la lista

    # Mostrar resultado final
    print("\nLista rotada:", rotada)
