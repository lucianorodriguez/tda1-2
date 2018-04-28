import unittest
from grafo import Grafo

class GrafoTest(unittest.TestCase):
    
    def test_agregar_un_vertice(self):
        g = Grafo()
        g.add_vertice(1)
        self.assertEqual(g.datos, {1:{}}, "Fallo agregar un vertice")
        
    def test_agregar_cinco_vertices(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_vertice(3)
        g.add_vertice(4)
        g.add_vertice(5)
        self.assertTrue(len(g.get_all_vertices()) == 5, "La cantidad de vertices no es cinco")
        self.assertEqual(g.datos, {1:{},2:{},3:{},4:{},5:{}}, "Fallo agregar cinco vertices")
    
    def test_eliminar_un_vertice_existente(self):
        g = Grafo()
        g.add_vertice(1)
        g.pop_vertice(1)
        self.assertTrue(not g.contains_vertice(1), "El vertice sigue estando en el grafo")
        self.assertEqual(g.datos, {}, "Fallo borrar un vertice")
        
    def test_agregar_una_arista(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_or_update_arista(1,2)
        self.assertTrue(g.get_peso_arista(1,2) == 1, "El peso de la arista es incorrecto 1")
        self.assertTrue(g.get_peso_arista(2,1) == 1, "El peso de la arista es incorrecto 2")
        self.assertEqual(g.datos, {1:{2:1},2:{1:1}}, "Fallo agregar una arista")
        
    def test_agregar_una_arista_sin_peso_y_updatear_el_peso(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_or_update_arista(1,2)
        g.add_or_update_arista(1,2,5)
        self.assertTrue(g.get_peso_arista(1,2) == 5, "El peso de la arista es incorrecto 1")
        self.assertTrue(g.get_peso_arista(2,1) == 5, "El peso de la arista es incorrecto 2")
        self.assertEqual(g.datos, {1:{2:5},2:{1:5}}, "Fallo updatear peso de una arista")
        
    def test_agregar_un_vertice_existente_no_elimina_sus_aristas(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_or_update_arista(1,2)
        self.assertTrue(len(g.get_all_vertices_adyacentes(1)) == 1, "La cantidad de adyacentes es incorrecta 1")
        g.add_vertice(1)
        self.assertTrue(len(g.get_all_vertices_adyacentes(1)) == 1, "La cantidad de adyacentes es incorrecta 2")
        self.assertEqual(g.datos, {1:{2:1},2:{1:1}}, "Fallo agregar un vertice existente")
    