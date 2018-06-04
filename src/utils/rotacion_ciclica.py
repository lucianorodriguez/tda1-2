from stringSearcher import *

def __rotar(str):
    return str[len(str) - 1] + str[:len(str) - 1]

def es_rotacion_fuerza_bruta(unStr,otroStr):
    if len(unStr) != len(otroStr):
        return False
    i = 0
    while unStr != otroStr and i < len(unStr):
        otroStr = __rotar(otroStr)
        i+=1
    return i < len(unStr)

def es_rotacion_kmp(unStr,otroStr):
    if len(unStr) != len(otroStr):
        return False
    i = 0
    while not search_kmp(unStr, otroStr) and i < len(unStr):
        otroStr = __rotar(otroStr)
        i+=1
    return i < len(unStr)

def es_rotacion_kmp_optimizado(unStr,otroStr):
    if len(unStr) != len(otroStr):
        return False
    return search_kmp(unStr, otroStr + otroStr)