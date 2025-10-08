
# Crear una lista vacía para guardar los números
numeros = []

print("Ingresa números para la lista. Escribe 'fin' para terminar.\n")

# Ciclo para leer los números del usuario
while True:
    valor = input("Número (o 'fin' para terminar): ")
    
    # Si el usuario escribe 'fin', se sale del ciclo
    if valor.lower() == "fin":
        break
    else:
        # Convertir el valor a número entero y agregarlo a la lista
        numeros.append(int(valor))

# Crear una nueva lista para guardar los números sin duplicados
sin_duplicados = []

# Ciclo para eliminar duplicados manteniendo el orden
for n in numeros:
    if n not in sin_duplicados:
        sin_duplicados.append(n)

# Mostrar los resultados
print("\nLista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)