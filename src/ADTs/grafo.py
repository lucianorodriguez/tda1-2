class Grafo:
    
    def __init__(self, conPesos):
        self.datos = {}
        self.conPesos = conPesos
    
    # Si el nodo es un objeto asegurarse que tenga implementado __hash__(self)
    def add_vertice(self, vertice):
        self.datos.__setitem__(vertice, {})
    
    def pop_vertice(self, vertice):
        if(self.datos.__contains__(vertice)):
            return self.datos.pop(vertice)
        return None
        
    def add_arista(self, unVertice, otroVertice, peso=1):
        aristasUnVertice = self.datos.get(unVertice)
        aristasOtroVertice = self.datos.get(otroVertice)
         # Si no existe alguno de los vertices levanto exception
        if(aristasOtroVertice == None or aristasUnVertice == None):
            raise Exception('Uno de los vértices no se encontró en el grafo')
        aristasUnVertice.__setitem__(otroVertice, peso)
        aristasOtroVertice.__setitem__(unVertice, peso)
        
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
    
    def get_peso_arista(self, unVertice, otroVertice):
        aristasUnVertice = self.datos.get(unVertice)
        if(aristasUnVertice == None):
            return None
        return aristasUnVertice.get(otroVertice)
