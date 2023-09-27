from Biseccion import biseccion_con_iteraciones
import math

def funcion(x):
    return (x*(math.e)**x)-1

raiz_aprox = biseccion_con_iteraciones(funcion, 0, 1, 50)
print(f"la raiz aproximada es {raiz_aprox}")
