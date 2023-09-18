'''7. Considerar la ecuaci´on x − e
−x = 0.
1
(a) Demostrar que la ecuaci´on tiene una ´unica soluci´on en el intervalo
[0,1].
(b) Si usamos el m´etodo de bisecci´on conintervalo inicial [0,1]. Cu´antas
iteraciones nos hacen falta para asegurar 4 decimales exactos?
(c) Calcular las 5 primeras iteraciones'''

import math
from Biseccion import biseccion_con_tolerancia, biseccion_con_iteraciones

def funcion(x):
    return(x- math.e**-x)

''' para calcular si existe una raiz en el intervalo [0, 1], calculo f(a)*(f(b)) < 0 y tiene que ser continua.'''

raiz_c = biseccion_con_iteraciones(funcion, 0, 1, 5)
print(raiz_c)


raiz_aprox = biseccion_con_tolerancia(funcion, 0, 1, 10**-4)
print(raiz_aprox)