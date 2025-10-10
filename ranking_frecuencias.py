# ranking_frecuencias.py
lista = []
while True:
    text = input('Ingrese cadena a almacenar en la lista o \'-1\' para salir: ')
    text.replace(' ', '')
    if text == '-1':
        break
    else:    
        lista.append(text)
frecuencias = []
unicos = []

for cadena in lista:
    if cadena not in unicos:
        unicos.append(cadena)
for t in unicos:
    frecuencias.append([t,lista.count(t)])
print(frecuencias)



