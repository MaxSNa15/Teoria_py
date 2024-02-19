'''
    ___________ Implementar el Grafo de ciudades españolas ___________
'''

# Indirect graph
# variable grafo se puede representar como un set
# G = (V, E) donde V es el conjunto de vértices y E es el conjunto de aristas

ver = (
    'Virgo', 'Coruña', 'Valladolid', 'Madrid', 'Bilbao', 'Oviedo', 'Zaragoza',
    'Barcelona', 'Gerona', 'Badajoz', 'Valencia', 'Jaen', 'Albacete', 'Murcia',
    'Cadiz', 'Sevilla', 'Granada'
)

ari = {
    ('Virgo', 'Coruña', 171), ('Virgo', 'Valladolid', 356),
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

def DFSPath1(grafo, inicio, fin, path):
    path.append(inicio)
    #caso base
    if inicio == fin:
        return path

    for n in grafo.getVecinos(inicio):
        if n not in path:
            nuevo_path = DFSPath1(grafo, n, fin, path)
            if nuevo_path is not None:
                return nuevo_path

def DFSPath2(grafo, inicio, fin, path, mej):
    path = path + [inicio]
    #caso base
    if inicio == fin:
        return path
    for n in grafo.getVecinos(inicio):
        if n not in path:
            if mej == None or len(path) < len(mej):
                nuevo_path = DFSPath2(grafo, n, fin, path, mej)
                if nuevo_path is not None:
                    mej = nuevo_path
    return mej

def BFS1(grafo, inicio, fin):
    path = [inicio]
    queue = [path]
    while queue:
        actual_path = queue.pop(0)
        if actual_path[-1] == fin:
            return actual_path
        for sn in grafo.getVecinos(actual_path[-1]):
            nuevo_path = actual_path + [sn]
            queue.append(nuevo_path)

def BFS2(grafo, inicio, fin):
    path = [inicio]
    queue = [path]
    while queue:
        actual_path = queue.pop(0)
        if actual_path[-1] == fin:
            return actual_path
        for sn in grafo.getVecinos(actual_path[-1]):
            if sn not in actual_path:
                nuevo_path = actual_path + [sn]
                queue.append(nuevo_path)

# Definimos nuevamente la función DFS para la búsqueda en profundidad
def DFS(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)

    print(inicio.getNombre())

    for vecino in grafo.getVecinos(inicio):
        if vecino not in visitados:
            DFS(grafo, vecino, visitados)

    return visitados

# Re-construimos el grafo y ejecutamos DFS
grafo = Undirected_Grafo()
for v in ver:
    grafo.addNodo(Nodo(v))

for (origen, destino, peso) in ari:
    origen_nodo = grafo.getNodo(origen)
    destino_nodo = grafo.getNodo(destino)
    if origen_nodo and destino_nodo:
        grafo.addArista(Arista(origen_nodo, destino_nodo, peso))

# Realizamos la búsqueda en profundidad (DFS)
inicio = grafo.getNodo('Madrid')
visitados = DFS(grafo, inicio)



########################################################################################
# print('=======================================================================')
# G1 = construirGrafo(Undirected_Grafo)
# print(G1)
# print('=======================================================================')

# path = DFSPath1(G1, G1.getNodo('Virgo'), G1.getNodo('Sevilla'), [])

# for i in path:
#     print(f'{i.getNombre()}', end=' ')

# print()
# print('=======================================================================')

# path2 = DFSPath2(G1, G1.getNodo('Virgo'), G1.getNodo('Sevilla'), [], None)

# for i in path2:
#     print(f'{i.getNombre()}', end=' ')

# print()
# print('=======================================================================')

# path3 = BFS1(G1, G1.getNodo('Virgo'), G1.getNodo('Sevilla'))

# for i in path3:
#     print(f'{i.getNombre()}', end='-> ')

# print()
# print('=======================================================================')

# path4 = BFS2(G1, G1.getNodo('Virgo'), G1.getNodo('Sevilla'))

# for i in path4:
#     print(f'{i.getNombre()}', end='-> ')

# print()
# print('=======================================================================')



