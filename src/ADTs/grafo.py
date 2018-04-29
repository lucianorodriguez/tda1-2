from heap import Heap
import sys


class Grafo:
    
    # Inicializa un grafo vacio sin pesos por default.
    def __init__(self, conPesos=False):
        self.datos = {}
        self.conPesos = conPesos
        self.cantidadVertices = 0
    
    # Agrega un vertice al grafo. Si el vertice ya existia deja todo igual
    # IMPORTANTE: Si el vertice es un objeto asegurarse que tenga implementado __hash__(self)
    def add_vertice(self, vertice):
        if(not self.contains_vertice(vertice)):
            self.datos.__setitem__(vertice, {})
            self.cantidadVertices += 1
    
    # Elimina el vertice o deja todo igual en caso de no existir.
    # Devuelve todas las aristas adyacentes con sus pesos o None segun exista o no exista el vertice.
    def pop_vertice(self, vertice):
        if(self.contains_vertice(vertice)):
            aristas = self.datos.pop(vertice)
            for key in aristas.keys():
                self.datos.get(key).pop(vertice)
            self.cantidadVertices -= 1
        return None
    
    # Devuelve true o false segun el vertice exista o no en el grafo.
    def contains_vertice(self, vertice):
        return self.datos.__contains__(vertice)
    
    # PRE CONDICION: peso es un numero o algo que se pueda comparar por > o <
    # Agrega o actualiza una arista entre unVertice y otroVertice con el peso indicado o peso 1 por default si no se indica.
    # En caso de no existir alguno de los vertices devuelve una Exception
    def add_or_update_arista(self, unVertice, otroVertice, peso=1):
        aristasUnVertice = self.datos.get(unVertice)
        aristasOtroVertice = self.datos.get(otroVertice)
         # Si no existe alguno de los vertices levanto exception
        if(aristasOtroVertice == None or aristasUnVertice == None):
            raise Exception('Uno de los vertices no se encontro en el grafo')
        aristasUnVertice.__setitem__(otroVertice, peso)
        aristasOtroVertice.__setitem__(unVertice, peso)
        
    # Elimina la arista entre unVertice y otroVertice o deja todo igual en caso de no existir.
    # Devuelve el peso de la arista o None segun exista o no exista la arista.
    def pop_arista(self, unVertice, otroVertice):
        aristasUnVertice = self.datos.get(unVertice)
        aristasOtroVertice = self.datos.get(otroVertice)
        # Si no existe alguno de los vertices devuelvo None
        if(aristasOtroVertice == None or aristasUnVertice == None):
            return None
        peso = None
        if(aristasOtroVertice.__contains__(unVertice)):
            peso = aristasOtroVertice.pop(unVertice)
        if(aristasUnVertice.__contains__(otroVertice)):
            peso = aristasUnVertice.pop(otroVertice)
        return peso
    
    # Devuelve el peso de la arista entre unVertice y otroVertice o None en caso de no haber una arista entre esos vertices.
    def get_peso_arista(self, unVertice, otroVertice):
        aristasUnVertice = self.datos.get(unVertice)
        if(aristasUnVertice == None):
            return None
        return aristasUnVertice.get(otroVertice)
    
    # Devuelve un set con todos los vertices del grafo.
    def get_all_vertices(self):
        return self.datos.keys()
    
    # Devuelve un set con los vertices adyacentes a unVertice parametro o None en caso de no existir unVertice en el grafo.
    def get_all_vertices_adyacentes(self, unVertice):
        aristasUnVertice = self.datos.get(unVertice)
        if(aristasUnVertice == None):
            return None
        return aristasUnVertice.keys()
    
    # Devuelve true o false segun si el grafo esta vacio o no.
    def is_empty(self):
        return self.datos == {}
    
    def get_dijkstra(self, verticeOrigen, verticeDestino):
        if(not self.contains_vertice(verticeOrigen) or not self.contains_vertice(verticeDestino)):
            raise Exception('Uno de los vertices no se encontro en el grafo')
        nodoActual = self.NodoDijkstra(verticeOrigen, 0, [])
        visitados = {}
        heap = Heap([])
        heap.push(self.NodoDijkstra(verticeDestino, sys.maxsize, []))
        while (verticeDestino != nodoActual.vertice):
            if(not visitados.__contains__(nodoActual.vertice)):
                visitados.__setitem__(nodoActual.vertice, 1)
                for adyacente in self.get_all_vertices_adyacentes(nodoActual.vertice):
                    if(not visitados.__contains__(adyacente)):
                        heap.push(self.NodoDijkstra(adyacente, nodoActual.distancia + self.get_peso_arista(nodoActual.vertice, adyacente), nodoActual.camino + [nodoActual.vertice]))
            nodoActual = heap.pop()
        if(nodoActual.distancia == sys.maxsize):
            return None
        return nodoActual.camino, nodoActual.distancia
    
    class NodoDijkstra:
        
        def __init__(self, vertice, distancia, camino):
            self.vertice = vertice
            self.distancia = distancia
            self.camino = camino
        
        def __lt__(self, other):
            return self.distancia < other.distancia
        
        def __le__(self, other):
            return self.distancia <= other.distancia
            
        def __ne__(self, other):
            return self.distancia != other.distancia
            
        def __gt__(self, other):
            return self.distancia > other.distancia
            
        def __ge__(self, other):
            return self.distancia >= other.distancia
        
