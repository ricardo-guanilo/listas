numeros = []

print("Ingresa números para la lista. Escribe 'fin' para terminar.\n")

# Leer los números del usuario
while True:
    valor = input("Número (o 'fin' para terminar): ")
    if valor.lower() == "fin":
        break
    else:
        numeros.append(int(valor))

# Crear listas para pares e impares
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

# Mostrar resultados
print("\nLista original:", numeros)
print("Pares:", pares)
print("Impares:", impares)
