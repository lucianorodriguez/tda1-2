from src.ADTs.grafo import Grafo
import math
import sys

def get_x_y(p):
    x, y = p.split("-")
    return int(x), int(y)


def calcularPeso(p1, p2):
    p1_x, p1_y = get_x_y(p1)
    p2_x, p2_y = get_x_y(p2)
    return math.sqrt((p1_x - p2_x)**2 + (p1_y - p2_y)**2)


def crear_grafo_desde_archivo(nombre_archivo="as", sin_peso=True):
    grafo = Grafo()
    f = open("./files/"+nombre_archivo, "r")
    for line in f:
        p1, p2 = line.split("-")
        p1 = p1[:-1].replace(" ", "-").replace("\n", "")
        p2 = p2[1:].replace(" ", "-").replace("\n", "")
        grafo.add_vertice(p1)
        grafo.add_vertice(p2)
        print('Distancia euclideana entre p1 y p2: '+str(calcularPeso(p1, p2)))
        grafo.add_or_update_arista(p1, p2, 1 if sin_peso else calcularPeso(p1, p2))
    return grafo



grafo = crear_grafo_desde_archivo("grafo_ejemplo")
for arg in sys.argv[1:]:
  print(arg)