'''
Puzle de MU de Douglas Hofstadter

Este programa intenta resolver el puzle de MU, un famoso ejercicio de lógica descrito en el libro "Gödel, Escher, Bach" de Douglas Hofstadter. El objetivo es transformar la cadena inicial "MI" en "MU" utilizando un conjunto de reglas de transformación de cadenas.

El programa utiliza un enfoque de búsqueda en profundidad (DFS) para aplicar las reglas y explorar las diferentes combinaciones posibles. Las reglas son las siguientes:
1. Si la última letra de una cadena es 'I', se puede agregar una 'U' al final.
2. Si la cadena es de la forma 'Mx', se puede formar 'Mxx' (donde 'x' es cualquier secuencia de letras).
3. Tres 'I' consecutivas ('III') pueden ser reemplazadas por una 'U'.
4. Dos 'U' consecutivas ('UU') pueden ser eliminadas de la cadena.

El programa intenta aplicar estas reglas para transformar "MI" en "MU", aunque es importante notar que, de acuerdo con las reglas dadas, no existe una solución que permita esta transformación.
'''

def transform_to_MU(current_string, depth=0, max_depth=10):
    # Regla 1: Si la última letra es I, se puede agregar U
    if current_string[-1] == 'I':
        new_string = current_string + 'U'
        if new_string == 'MU':
            return ['MU']
        elif depth < max_depth:
            result = transform_to_MU(new_string, depth + 1, max_depth)
            if result:
                return [new_string] + result

    # Regla 2: Se puede duplicar la parte después de M
    new_string = current_string + current_string[1:]
    if new_string == 'MU':
        return ['MU']
    elif depth < max_depth:
        result = transform_to_MU(new_string, depth + 1, max_depth)
        if result:
            return [new_string] + result

    # Regla 3: III se puede reemplazar por U
    if 'III' in current_string:
        new_string = current_string.replace('III', 'U', 1)
        if new_string == 'MU':
            return ['MU']
        elif depth < max_depth:
            result = transform_to_MU(new_string, depth + 1, max_depth)
            if result:
                return [new_string] + result

    # Regla 4: UU se puede eliminar
    if 'UU' in current_string:
        new_string = current_string.replace('UU', '', 1)
        if new_string == 'MU':
            return ['MU']
        elif depth < max_depth:
            result = transform_to_MU(new_string, depth + 1, max_depth)
            if result:
                return [new_string] + result

    # No se encontró una solución en este camino
    return None

# Intenta transformar MI en MU
solution = transform_to_MU("MI")
if solution:
    print("Se encontró una solución:", solution)
else:
    print("No se encontró una solución.")