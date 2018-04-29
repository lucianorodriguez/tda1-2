import unittest
from grafo import Grafo


class GrafoTest(unittest.TestCase):
    
    def test_crear_grafo_empieza_vacio(self):
        g = Grafo()
        self.assertTrue(g.is_empty(), "Fallo crear grafo vacio")
        
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
        self.assertEqual(g.datos, {1:{}, 2:{}, 3:{}, 4:{}, 5:{}}, "Fallo agregar cinco vertices")
    
    def test_eliminar_un_vertice_existente(self):
        g = Grafo()
        g.add_vertice(1)
        g.pop_vertice(1)
        self.assertTrue(not g.contains_vertice(1), "El vertice sigue estando en el grafo")
        self.assertEqual(g.datos, {}, "Fallo borrar un vertice")
        
    def test_eliminar_un_vertice_inexistente_devuelve_None_y_deja_todo_igual(self):
        g = Grafo()
        aristas = g.pop_vertice(1)
        self.assertEqual(aristas, None, "Aristas no es None")
        self.assertTrue(g.is_empty(), "Grafo no esta vacio")
        self.assertEqual(g.datos, {}, "Fallo eliminar vertice inexistente")
        
    def test_agregar_una_arista(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_or_update_arista(1, 2)
        self.assertTrue(g.get_peso_arista(1, 2) == 1, "El peso de la arista es incorrecto 1")
        self.assertTrue(g.get_peso_arista(2, 1) == 1, "El peso de la arista es incorrecto 2")
        self.assertEqual(g.datos, {1:{2:1}, 2:{1:1}}, "Fallo agregar una arista")
        
    def test_agregar_una_arista_sin_peso_y_updatear_el_peso(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_or_update_arista(1, 2)
        g.add_or_update_arista(1, 2, 5)
        self.assertTrue(g.get_peso_arista(1, 2) == 5, "El peso de la arista es incorrecto 1")
        self.assertTrue(g.get_peso_arista(2, 1) == 5, "El peso de la arista es incorrecto 2")
        self.assertEqual(g.datos, {1:{2:5}, 2:{1:5}}, "Fallo updatear peso de una arista")
        
    def test_agregar_arista_en_vertice_inexistente_lanza_exception(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        with self.assertRaises(Exception):
            g.add_or_update_arista(1, 3)
        self.assertEqual(g.datos, {1:{}, 2:{}}, "Fallo agregar arista sobre vertice inexistente")
        
    def test_agregar_un_vertice_existente_no_elimina_sus_aristas(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_or_update_arista(1, 2)
        self.assertTrue(len(g.get_all_vertices_adyacentes(1)) == 1, "La cantidad de adyacentes es incorrecta 1")
        g.add_vertice(1)
        self.assertTrue(len(g.get_all_vertices_adyacentes(1)) == 1, "La cantidad de adyacentes es incorrecta 2")
        self.assertEqual(g.datos, {1:{2:1}, 2:{1:1}}, "Fallo agregar un vertice existente")
        
    def test_obtener_adyacentes(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_vertice(3)
        g.add_vertice(4)
        g.add_vertice(5)
        g.add_or_update_arista(1, 2)
        g.add_or_update_arista(1, 3)
        g.add_or_update_arista(1, 4)
        g.add_or_update_arista(5, 2)
        g.add_or_update_arista(4, 2)
        self.assertEqual(g.get_all_vertices_adyacentes(1), {2, 3, 4}, "Los adyacentes no son correctos 1")
        self.assertEqual(g.get_all_vertices_adyacentes(2), {1, 4, 5}, "Los adyacentes no son correctos 2")
        self.assertEqual(g.datos, {1:{2:1, 3:1, 4:1}, 2:{4:1, 5:1, 1:1}, 3:{1:1}, 4:{1:1, 2:1}, 5:{2:1}}, "Fallo obtener vertices adyacentes")

    def test_dijkstra_3_nodos(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_vertice(3)
        g.add_or_update_arista(1, 2, 4)
        g.add_or_update_arista(1, 3, 2)
        g.add_or_update_arista(2, 3, 1)
        self.assertEqual(g.get_dijkstra(1, 2), ([1, 3], 3), "Fallo dijkstra 3 nodos")
        
    def test_dijkstra_5_nodos(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_vertice(3)
        g.add_vertice(4)
        g.add_vertice(5)
        g.add_or_update_arista(1, 2, 2)
        g.add_or_update_arista(1, 4, 1)
        g.add_or_update_arista(4, 3, 3)
        g.add_or_update_arista(2, 3, 4)
        g.add_or_update_arista(2, 5, 5)
        g.add_or_update_arista(3, 5, 1)
        self.assertEqual(g.get_dijkstra(1, 5), ([1, 4, 3], 5), "Fallo dijkstra 5 nodos")
        
    def test_dijkstra_nodo_destino_aislado(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_vertice(3)
        g.add_vertice(4)
        g.add_vertice(5)
        g.add_or_update_arista(1, 2, 2)
        g.add_or_update_arista(1, 4, 1)
        g.add_or_update_arista(4, 3, 3)
        g.add_or_update_arista(2, 3, 4)
        self.assertEqual(g.get_dijkstra(1, 5), None, "Fallo dijkstra nodo aislado")
        
    def test_dijkstra_nodo_destino_inexistente(self):
        g = Grafo()
        g.add_vertice(1)
        g.add_vertice(2)
        g.add_or_update_arista(1, 2, 2)
        with self.assertRaises(Exception):
            g.get_dijkstra(1,5)
        

        
