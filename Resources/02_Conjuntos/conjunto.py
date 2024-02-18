'''
    ___________ Lista de ejercicios de conjuntos ___________
'''

''' # Ejercicio 1 #
    Dados los conjuntos A = {1, 2, 3} y B = {2, 3, 4}, realiza las operaciones
    de unión, intersección, diferencia
'''
A, B = {1, 2, 3}, {2, 3, 4}

# Union
print(A | B)
print(A.union(B))

# Intersección
print(A & B)
print(A.intersection(B)) 

# Diferencia
print(A - B)
print(A.difference(B))


''' # Ejercicio 2 #
    Crea un diagrama de Venn que represente tres conjuntos A = {rojo, azul} B = {azul, verde} C = {verde, amarillo}
    Luego realiza las operaciones como [A n B], [A u C]
'''
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Definiendo los conjuntos
A, B, C = {'rojo', 'azul'}, {'azul', 'verde'}, {'verde', 'amarillo'}

# Creando el diagrama de Venn para los tres conjuntos
venn = venn3([A, B, C], ('A', 'B', 'C'))

# Mostrando el diagrama de Venn
plt.title("Diagrama de Venn para los conjuntos A, B y C")
plt.show()

# Realizando las operaciones de conjuntos
interseccion_A_B = A.intersection(B)
union_A_C = A.union(C)

(interseccion_A_B, union_A_C)


''' # Ejercicio 3 #
    Si el conjunto universo es U = {1, 2, 3, 4, 5} encuentra el complemento de A = {2, 4}
'''
U = {1, 2, 3, 4, 5}
A = {2, 4}

complemento_A = U - A
print(complemento_A)


''' # Ejercicio 4 #
    Considera los conjuntos A = {1, 2, 3} y B = {3, 4, 5} 
    Determina si 2 pertenece a A, si 4 pertenece a B, y si 6 pertenece a A o B
'''
A, B = {1, 2, 3}, {3, 4, 5}

pertenece_2_A = 2 in A
pertenece_4_B = 4 in B
pertenece_6_A_o_B = 6 in A or 6 in B

print(pertenece_2_A, pertenece_4_B, pertenece_6_A_o_B)

''' # Ejercicio 5 #
    Sean A = {a, b, c, d} y B = {c, d, e} 
    Encuentra el numero de elementos de [A n B] y [A u B]
'''
A, B = {'a', 'b', 'c', 'd'}, {'c', 'd', 'e'}

num_elementos_interseccion = len(A.intersection(B))
num_elementos_union = len(A.union(B))

print(num_elementos_interseccion, num_elementos_union)

''' # Ejercicio 6 #
    Demuestra las identidades de conjuntos basicas, como la ley de idempotencia
    ( [A u A = A] y [A n A = A] ), 
    la ley de absorcion
    ( A u ( A n B ) = A y A n (A u B) = A) 
    entre otras...
'''
# Definiendo conjuntos de ejemplo A y B
A = {1, 2, 3}
B = {3, 4, 5}

# Ley de Idempotencia
idempotencia_union = A.union(A) == A
idempotencia_interseccion = A.intersection(A) == A

# Ley de Absorción
absorcion_union = A.union(A.intersection(B)) == A
absorcion_interseccion = A.intersection(A.union(B)) == A

print(idempotencia_union, idempotencia_interseccion, absorcion_union, absorcion_interseccion)



''' # Ejercicio 7 #
    Imagina que tienes 2 conjuntos que representan estudiantes que participan en diferentes actividades extraescolares
    Diseña un conjuntos para modelar estudiantes en deportes, musica y arte
    Luega realiza operaciones para encontrar estudiantes que participan en multiples actividades
'''

# Definiendo los conjuntos de estudiantes
deportes = {'Juan', 'Maria', 'Pedro'}
musica = {'Maria', 'Ana', 'Pedro'}
arte = {'Pedro', 'Luis', 'Ana'}

# Estudiantes que participan en multiples actividades
estudiantes_multiples = deportes.intersection(musica, arte)
print(estudiantes_multiples) # Muestra el conjunto de estudiantes que participan en todas las actividades
