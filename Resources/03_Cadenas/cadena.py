def aplicar_regla1(cadena):
    return cadena + 'U'

def aplicar_regla2(cadena):
    return cadena * 2

def aplicar_regla3(cadena):
    cadena = cadena.replace('III', 'U', 1)
    return cadena

def aplicar_regla4(cadena):
    cadena = cadena.replace('UU', 'U')
    return cadena  

def resolver(cadena_actual, cadena_objetivo, historial=[]):
    if cadena_actual == cadena_objetivo:
        return historial + [cadena_actual]

    if len(cadena_actual) > len(cadena_objetivo):
        return None

    if cadena_actual in historial:
        return None

    nuevo_historial = historial + [cadena_actual]

    resultado = resolver(aplicar_regla1(cadena_actual), cadena_objetivo, nuevo_historial)
    if resultado:
        return resultado

    resultado = resolver(aplicar_regla2(cadena_actual), cadena_objetivo, nuevo_historial)
    if resultado:
        return resultado

    resultado = resolver(aplicar_regla3(cadena_actual), cadena_objetivo, nuevo_historial)
    if resultado:
        return resultado
    
    resultado = resolver(aplicar_regla4(cadena_actual), cadena_objetivo, nuevo_historial)
    return resultado

# Ejemplo de uso
cadena_inicial = "MI"
cadena_objetivo = "MU"
solucion = resolver(cadena_inicial, cadena_objetivo)

if solucion:
    print(f"Se puede llegar de '{cadena_inicial}' a '{cadena_objetivo}' mediante las siguientes operaciones:")
    for i, paso in enumerate(solucion):
        print(f"Paso {i + 1}: {paso}")
else:
    print(f"No es posible llegar de '{cadena_inicial}' a '{cadena_objetivo}'.")