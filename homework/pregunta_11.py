"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    a = open("files/input/data.csv", "r").readlines()
    b = {}
    for i in a:
        c = i.split("\t")
        d = c[3].split(",")
        e = c[1]
        for j in d:
            f = j.split(":")[0]
            if f in b:
                b[f] += int(e)
            else:
                b[f] = int(e)
    return dict(sorted(b.items()))