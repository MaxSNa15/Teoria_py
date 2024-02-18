import time

import lista_des as listass

print("Metodo de ordenamiento MergeSort")

lista = listass.lista_desordenada

def mergeSort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        mergeSort(izquierda)
        mergeSort(derecha)

        i = 0
        j = 0
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista



# Registrando el tiempo de inicio
inicio = time.time()

# Llamando a la función mergeSort
lista_ordenada = mergeSort(lista)

# Registrando el tiempo de finalización
fin = time.time()

# Calculando la duración en milisegundos
duracion = (fin - inicio) * 1000

print("Lista ordenada:", lista_ordenada)
print("Tiempo de ejecución (milisegundos):", duracion)

# Guardar el resultado en un txt
# Guardar el resultado en un archivo txt
with open('resultado_mergeSort.txt', 'w') as archivo:
    archivo.write("Lista ordenada: " + str(lista_ordenada) + "\n")
    archivo.write("Tiempo de ejecución (milisegundos): " + str(duracion))