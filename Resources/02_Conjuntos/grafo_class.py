# Edge (Arista)
class Arista:
    def __init__(self, nodo1, nodo2, peso=1):
        self.nodo1 = nodo1 # origen
        self.nodo2 = nodo2 # destino
        self.peso = peso

    def getNodo1(self):
        return self.nodo1
    
    def getNodo2(self):
        return self.nodo2
    
    def getPeso(self):
        return self.peso
    
    def __str__(self):
        return self.nodo1.getNombre() + ' -> ' + self.nodo2.getNombre() + ' (' + str(self.peso) + ')'

# Vertex (Nodo)
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def __str__(self):
        return f'{self.nombre}'

# Grafo Dirigido
class Directed_Grafo:
    def __init__(self):
        self.grafo_dict = {}
    
    def addNodo(self, nodo):
        if nodo in self.grafo_dict:
            return 'Nodo ya existe en el grafo'
        self.grafo_dict[nodo] = []
    
    def addArista(self, arista):
        nodo1 = arista.getNodo1()
        nodo2 = arista.getNodo2()

        if nodo1 not in self.grafo_dict:
            raise ValueError('Nodo no existe en el grafo')
        if nodo2 not in self.grafo_dict:
            raise ValueError('Nodo no existe en el grafo')
        
        self.grafo_dict[nodo1].append(nodo2)
    
    def siNodoExiste(self, nodo):
        return nodo in self.grafo_dict
    
    def getNodo(self, nombre):
        for n in self.grafo_dict:
            if nombre == n.getNombre():
                return n
        print('Nodo no existe en el grafo')

    def getVecinos(self, nodo):
        return self.grafo_dict[nodo]
    
    def __str__(self):
        all_aristas = ''
        for n1 in self.grafo_dict:
            for n2 in self.grafo_dict[n1]:
                all_aristas += n1.getNombre() + ' <-> ' + n2.getNombre() + '\n'
        return all_aristas

# Grafo No Dirigido
class Undirected_Grafo(Directed_Grafo):
    def addArista(self, arista):
        Directed_Grafo.addArista(self, arista)
        arista_rev = Arista(arista.getNodo2(), arista.getNodo1())
        Directed_Grafo.addArista(self, arista_rev)
