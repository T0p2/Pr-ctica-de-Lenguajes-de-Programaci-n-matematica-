'''(b) Usar el m´etodo de bisecci´on en el intervalo [1,2]. 
Cu´antas iteraciones hacen 
falta para asegurar 5 decimales exactos?'''
#hace falta 15 iteraciones

from Biseccion import biseccion_con_tolerancia, biseccion_con_iteraciones
import math

def funcion(x):
    return(math.log(x)*x - 1)

#raiz_prox = biseccion_con_tolerancia(funcion, 1, 2, 10**-5)
#print(f"la raiz apriximada de la funcion, es {raiz_prox}")

'''(c) Calcular las primeras 4 iteraciones.''' 

raiz_iteracion = biseccion_con_iteraciones(funcion, 1, 2, 4)

print(f"La raiz con 4 iteraciones es: {raiz_iteracion}")