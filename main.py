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


def crear_grafo_desde_archivo(nombre_archivo="grafo_ejemplo", sin_peso=True):
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



def resolver_problema_espia(posicion_espia_1, posicion_espia_2, posicion_aeropuerto, grafo, imprimir_distancia=False):
    arista_posicion_espia_1 = posicion_espia_1[0]+"-"+posicion_espia_1[1]
    arista_posicion_espia_2 = posicion_espia_2[0]+"-"+posicion_espia_2[1]
    arista_posicion_aeropuerto = posicion_aeropuerto[0]+"-"+posicion_aeropuerto[1]
    camino_espia_1, distancia_espia_1 = grafo.get_dijkstra(arista_posicion_espia_1, arista_posicion_aeropuerto)
    camino_espia_2, distancia_espia_2 = grafo.get_dijkstra(arista_posicion_espia_2, arista_posicion_aeropuerto)
    if distancia_espia_1 < distancia_espia_2:
        print("El espia 1 llega primero")
    elif (distancia_espia_2 < distancia_espia_1):
        print("El espia 2 llega primero")
    else:
        print("Ambos llega el mismo tiempo")


#Se utiliza otro archivo o el archivo por defecto

option_f = False
nombre_archivo = "grafo_ejemplo"
#Se utiliza los pesos euclidianos
opcion_espia_1 = False
opcion_espia_2 = False
opcion_aeropuerto = False
i = 1
p1_x, p1_y, p2_x, p2_y, a_x, a_y = 0, 0, 0, 0, 0, 0


while i < len(sys.argv):
  if sys.argv[i] == "-f":
      option_f = True
      sys.argv.pop(i)
      nombre_archivo = sys.argv.pop(i)
  elif sys.argv[i] == "-e1":
      opcion_espia_1 = True
      sys.argv.pop(i)
      p1_x = int(sys.argv.pop(i))
      p1_y = int(sys.argv.pop(i))
  elif sys.argv[i] == "-e2":
      opcion_espia_2 = True
      sys.argv.pop(i)
      p2_x = int(sys.argv.pop(i))
      p2_y = int(sys.argv.pop(i))
  elif sys.argv[i] == "-a":
      opcion_aeropuerto = True
      sys.argv.pop(i)
      a_x = int(sys.argv.pop(i))
      a_y = int(sys.argv.pop(i))
  else:
    i += 1


if ((not opcion_espia_2) or (not opcion_espia_1) or (not opcion_aeropuerto)):
    raise Exception("Falta algun parametro, verifique que este -e1,-e2 y -a")

espia_1 = (p1_x, p1_y)
espia_2 = (p2_x, p2_y)
aeropuerto = (a_x, a_y)

print('punto 1 :'+repr(espia_1)+" punto 2:"+repr(espia_2)+"aeropuerto:"+repr(aeropuerto))
print("Realizando el punto 1")
grafo_sin_peso_euclidiano = crear_grafo_desde_archivo(nombre_archivo, True)
resolver_problema_espia(espia_1, espia_2, aeropuerto, grafo_sin_peso_euclidiano)
print("Realizando el punto 2")
grafo_con_peso_euclidiano = crear_grafo_desde_archivo(nombre_archivo, False)
resolver_problema_espia(espia_1, espia_2, aeropuerto, grafo_con_peso_euclidiano)
print("Realizando el punto 4")
grafo_sin_peso_euclidiano_punto_4 = crear_grafo_desde_archivo(nombre_archivo)
resolver_problema_espia(espia_1, espia_2, aeropuerto, grafo_sin_peso_euclidiano_punto_4, imprimir_distancia=True)
grafo_con_peso_euclidiano_punto_4 = crear_grafo_desde_archivo(nombre_archivo, sin_peso=False)
resolver_problema_espia(espia_1, espia_2, aeropuerto, grafo_con_peso_euclidiano_punto_4, imprimir_distancia=True)

