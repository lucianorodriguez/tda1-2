def armar_tabla_de_falla(str):
    i = 0
    j = 0
    tabla = []
    for c in str:
        if i==0 :
            tabla.append(-1)
        else :
            if c == str[j]:
                tabla.append(tabla[j])
                j+=1
            else:
                tabla.append(j)
                j = tabla[j]
                while c != str[j] and j >= 0:
                    j = tabla[j]
                j+=1
        i+=1
    return tabla

def search_kmp(patron, texto):
    tablaFalla = armar_tabla_de_falla(patron)
    i = 0
    j = 0
    while i < len(texto):
        if texto[i] == patron[j]:
            j+=1
            i+=1
            if j == len(patron):
                return True
        else:
            i = i - tablaFalla[j]
            j = 0 if tablaFalla[j] < 0 else tablaFalla[j]
        
    return False
