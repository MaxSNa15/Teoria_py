'''
    ___________ Implementar el Grafo de ciudades españolas ___________
'''

# Indirect graph
# variable grafo se puede representar como un set
# G = (V, E) donde V es el conjunto de vértices y E es el conjunto de aristas

ver = (
    'Vigo', 'Coruña', 'Valladolid', 'Madrid', 'Bilbao', 'Oviedo', 'Zaragoza',
    'Barcelona', 'Gerona', 'Badajoz', 'Valencia', 'Jaen', 'Albacete', 'Murcia',
    'Cadiz', 'Sevilla', 'Granada'
)

ari = {
    ('Vigo', 'Coruña', 171), ('Vigo', 'Valladolid', 356),
    ('Coruña', 'Valladolid', 455),
    ('Valladolid', 'Bilbao', 280), ('Valladolid', 'Madrid', 193),
    ('Bilbao', 'Oviedo', 304), ('Bilbao', 'Zaragoza', 324), ('Bilbao', 'Madrid', 395),
    ('Madrid', 'Zaragoza', 325), ('Madrid', 'Badajoz', 403), ('Madrid', 'Jaen', 335), ('Madrid', 'Albacete', 251),
    ('Albacete', 'Murcia', 150), ('Albacete', 'Valencia', 191),
    ('Valencia', 'Murcia', 241), ('Valencia', 'Barcelona', 349),
    ('Barcelona', 'Gerona', 100), ('Barcelona', 'Zaragoza', 296),
    ('Granada', 'Jaen', 99), ('Granada', 'Sevilla', 256), ('Granada', 'Murcia', 278),
    ('Sevilla', 'Cadiz', 125), ('Sevilla', 'Jaen', 242)
}

########################################################################################
from grafo_class import *

def construirGrafo(grafo):
    g = grafo()
    for v in ver:
        g.addNodo(Nodo(v))

    for (origen, destino, peso) in ari:
        g.addArista(Arista(g.getNodo(origen), g.getNodo(destino), peso))

    return g


# Deap First Search (DFS) - Búsqueda en profundidad
def DFSPath1(grafo, inicio, fin, path):
    path.append(inicio) # Añadimos el nodo de inicio al camino
    #caso base
    if inicio == fin: # Si el nodo de inicio es el nodo de fin
        return path # Devolvemos el camino

    for n in grafo.getVecinos(inicio): # Para cada vecino del nodo de inicio
        if n not in path: # Si el vecino no está en el camino
            nuevo_path = DFSPath1(grafo, n, fin, path) # Realizamos la búsqueda en profundidad
            if nuevo_path is not None: # Si el camino no es nulo
                return nuevo_path # Devolvemos el camino


# Breadth First Search (BFS) - Búsqueda en anchura
def BFS1(grafo, inicio, fin):
    path = [inicio] # Inicializamos el camino path que es una lista || path = "Vigo"
    queue = [path] # Inicializamos la cola queue que es una lista
    while queue: # Mientras la cola no esté vacía
        actual_path = queue.pop(0) # Sacamos el primer elemento de la cola || actual_path = "Vigo"
        if actual_path[-1] == fin: # Si el último elemento del camino es el destino
            return actual_path # Devolvemos el camino
        for sn in grafo.getVecinos(actual_path[-1]): # Para cada vecino de la última ciudad del camino
            nuevo_path = actual_path + [sn] # Creamos un nuevo camino añadiendo el vecino al final
            queue.append(nuevo_path) # Añadimos el nuevo camino a la cola


########################################################################################
print('=======================================================================')
G1 = construirGrafo(Undirected_Grafo)
print(G1)
print('=======================================================================')
print()

path = DFSPath1(G1, G1.getNodo('Vigo'), G1.getNodo('Murcia'), [])
path2 = BFS1(G1, G1.getNodo('Vigo'), G1.getNodo('Murcia'))

print("Vigo -> Murcia en DFS")
for i in path:
    print(f'{i.getNombre()}', end=' ')

print()


print("Vigo -> Murcia en BFS")
for i in path2:
    print(f'{i.getNombre()}', end=' ')

print()
print('=======================================================================')
print()


path3 = DFSPath1(G1, G1.getNodo('Bilbao'), G1.getNodo('Cadiz'), [])
path4 = BFS1(G1, G1.getNodo('Bilbao'), G1.getNodo('Cadiz'))

print("Bilbao -> Cadiz en DFS")
for i in path3:
    print(f'{i.getNombre()}', end=' ')

print()


print("Bilbao -> Cadiz en BFS")
for i in path4:
    print(f'{i.getNombre()}', end=' ')

print()
print('=======================================================================')
print()


path5 = DFSPath1(G1, G1.getNodo('Murcia'), G1.getNodo('Sevilla'), [])
path6 = BFS1(G1, G1.getNodo('Murcia'), G1.getNodo('Sevilla'))

print("Murcia -> Sevilla en DFS")
for i in path5:
    print(f'{i.getNombre()}', end=' ')

print()


print("Murcia -> Sevilla en BFS")
for i in path6:
    print(f'{i.getNombre()}', end=' ')

print()
print('=======================================================================')
print()


path7 = DFSPath1(G1, G1.getNodo('Albacete'), G1.getNodo('Oviedo'), [])
path8 = BFS1(G1, G1.getNodo('Albacete'), G1.getNodo('Oviedo'))

print("Albacete -> Oviedo en DFS")
for i in path7:
    print(f'{i.getNombre()}', end=' ')

print()


print("Albacete -> Oviedo en BFS")
for i in path8:
    print(f'{i.getNombre()}', end=' ')

print()