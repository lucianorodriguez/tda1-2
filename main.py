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



#Se utiliza otro archivo o el archivo por defecto

option_f = False
option_f_argument = "grafo_ejemplo"
#Se utiliza los pesos euclidianos
option_con_peso = False
i = 1

while i < len(sys.argv):
  if sys.argv[i] == "-f":
      option_f = True
      sys.argv.pop(i)
      option_f_argument = sys.argv.pop(i)
  elif sys.argv[i] == "-peso":
    option_con_peso = True
    sys.argv.pop(i)
  elif sys.argv[i] == "-p1":
      sys.argv.pop(i)
      p1_x = sys.argv.pop(i)
      p1_y = sys.argv.pop(i)
  elif sys.argv[i] == "-p2":
      sys.argv.pop(i)
      p2_x = sys.argv.pop(i)
      p2_y = sys.argv.pop(i)
  else:
    i += 1


p1 = (p1_x, p1_y)
p2 = (p2_x, p2_y)
print('punto 1 :'+repr(p1)+" punto 2:"+repr(p2))
grafo = crear_grafo_desde_archivo(option_f_argument, option_con_peso)
